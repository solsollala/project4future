# -*- coding: utf-8 -*-

import os
import re
import urllib.request
import urllib.parse

from lxml import etree
from bs4 import BeautifulSoup

from webapp.utils import dbpia_items

# ----------------------------------------------------------------------------
# 상세정보 웹 페이지 내용 분해 (Journal 상세정보 분해)
# ----------------------------------------------------------------------------
def get_detail_info(url, object):
    try:
        raw_response = urllib.request.urlopen(url)  # 검색요청 및 응답수신
        utf8doc = raw_response.read().decode("utf8")

        tree = etree.fromstring(utf8doc, etree.HTMLParser())

        tag_class_list = tree.xpath('//*[@id="detail_tab_panel"]/div[2]/div[1]/@class')
        class_name = "".join(tag_class_list)
        kor_text_list = tree.xpath('//*[@id="detail_tab_panel"]/div[2]/div[1]/text()[1]')

        # xpath에 con_txt 또는 summary_txt가 들어 있어 2차적인 판단이 필요함
        if class_name == "con_txt":
            con_txt = "".join(kor_text_list)  # 문자열 리스트를 단일 문자열로
            object.con_txt = re.sub('[\t\n\r\f#]', '', con_txt)  # 특수문자 제거
            print("내용 ", object.con_txt)

        if class_name == "con_txt summary_txt":
            summary_txt = "".join(kor_text_list)
            object.summary_txt = re.sub('[\t\n\r\f#]', '', summary_txt)
            print("목차 ", object.summary_txt)

        tag_class_list = tree.xpath('//*[@id="detail_tab_panel"]/div[2]/div[2]/@class')
        class_name = "".join(tag_class_list)
        summary_txt_list = tree.xpath('//*[@id="detail_tab_panel"]/div[2]/div[2]/text()')

        # xpath에 con_txt 또는 summary_txt가 들어 있어 2차적인 판단이 필요함
        if class_name == "con_txt summary_txt":
            object.summary_txt = "".join(summary_txt_list)  # 문자열 리스트를 단일 문자열로
            print("목차 ", object.summary_txt)

        #    citeitem_list = tree.xpath('')

        keyword_list = tree.xpath('//*[@id="keyword_tab"]/a/text()')  # 문자열 목록을 가져오는 방법
        for kw in keyword_list:
            object.add_keywords(kw)
            print(kw)

        return
    except urllib.error.HTTPError:
        print("404 error")

# ----------------------------------------------------------------------------
# OpenApi 검색요청 응답 XML 분해 (Jornal 목록 및 기본정보 분해)
# ----------------------------------------------------------------------------
def parse_api_response(api_response, journals):
    tree = etree.fromstring(api_response)
    root = etree.ElementTree(tree).getroot()

    tag_result = root.find("result") # result 명칭의 tag 찾기
    tag_items = tag_result.find("items") # items 명칭의 tag 찾기

    list_tag_item = tag_items.findall("item")

    for tag_item in list_tag_item:
        title = tag_item.findtext("title")
        title = BeautifulSoup(title, "html.parser").getText() # BeautifulSoup를 사용하여 title 내부의 찌꺼기 태그 제거
        print(title)

        tag_authors = tag_item.find("authors")

        try:
            list_tag_author = tag_authors.findall("author")  # 'NoneType' object has no attribute 'findall'
        except Exception as e:
            print(str(e))
            pass

        Author_list = []
        for tag_author in list_tag_author:
            author_order = tag_author.findtext("order")
            author_url = tag_author.findtext("url")
            author_name = tag_author.findtext("name")
            obj = dbpia_items.Author(author_order, author_url, author_name)
            Author_list.append(obj)

        tag_publisher = tag_item.find("publisher")
        publisher_name = tag_publisher.findtext("name")
        tag_publication = tag_item.find("publication")
        publication_name = tag_publication.findtext("name")
        publication_issn = tag_publication.findtext("issn")
        publication_isbn10 = tag_publication.findtext("isbn10")
        publication_isbn13 = tag_publication.findtext("isbn13")
        print(publisher_name, publication_name, publication_issn, publication_isbn10, publication_isbn13)
        tag_issue = tag_item.find("issue")
        issue_name = tag_issue.findtext("name")
        issue_num = tag_issue.findtext("num")
        issue_yymm = tag_issue.findtext("yymm")
        print(issue_name, issue_num, issue_yymm)
        pages = tag_item.findtext("pages")
        print(pages)
        link_url = tag_item.findtext("link_url")
        print(link_url)

        # dbpia_item에 검색결과를 담는다
        d_item = dbpia_items.Dbpia_Item()

        d_item.title = title
        d_item.Authors = list(Author_list)
        d_item.publisher = publisher_name
        d_item.set_publication(publication_name, publication_issn, publication_isbn10, publication_isbn13)
        d_item.set_issue(issue_name, issue_num, issue_yymm)
        d_item.pages = pages
        d_item.link_url = link_url

        # 저널 세부정보를 추가적으로 스크래핑한다
        get_detail_info(link_url, d_item)

        # 검색결과 리스트에 추가한다
        journals.append(d_item)

# ----------------------------------------------------------------------------
# dbpia에 전송할 검색 문장완성 및 검색요청
# ----------------------------------------------------------------------------
def call_api(request_string):
    try:
        # 검색요청 및 응답수신
        raw_data = urllib.request.urlopen(request_string)
        api_response = raw_data.read().decode("utf8")
        return api_response
    except Exception as e:
        print( str(e) )
        raise Exception('call_api() exception')

    return ''

# ----------------------------------------------------------------------------
#
# 외부에서 DBpia 검색을 위해 호출하는 메인 함수
#
# ----------------------------------------------------------------------------

def dbpia_search_main(search_keyword, search_count, api_key, out_file):
    journal = []

    # 검색 키워드를 HTTP 전송을 위해 ascii 형태로 변환
    keyword_to_ascii = urllib.parse.quote(search_keyword)

    request_string = 'http://api.DBpia.co.kr/v1/search/search.xml?searchall=' + keyword_to_ascii + \
                     '&target=se_adv&key=' + api_key + \
                     '&pagecount=' + search_count

    try:
        api_response = call_api(request_string)

        if( api_response == '' ):
            return -1
    except Exception as e:
        return -1

    parse_api_response(api_response, journal)

    # 동일명 파일 삭제 후 저장
    try:
        os.remove(out_file)
    except Exception as e:
        print("File Remove error ", e)

    cnt = 0
    for j in journal:
        j.append_to(out_file)
        cnt += 1

    return cnt

# ----------------------------------------------------------------------------
# 검색할 키워드 입력
# ----------------------------------------------------------------------------
def get_search_keyword():
    kw = urllib.parse.quote_plus(str(input("검색어를 입력하세요: ")))
    kw.replace(" ", "+")
    return kw

# ----------------------------------------------------------------------------
# 검색할 갯수 입력
# ----------------------------------------------------------------------------
def get_total_count():
    return input("검색할 갯수를 입력하세요:")

# ----------------------------------------------------------------------------
# __main__
# ----------------------------------------------------------------------------

if __name__ == '__main__':
    journals = []

    search_keyword = get_search_keyword()
    search_count = get_total_count()
    api_key = "23eb10cd1ceea4cc8c763ad62d34a7c4"
    out_file = "c:/temp/temp.txt"

    keyword_to_ascii = urllib.parse.quote(search_keyword)

    request_string = 'http://api.DBpia.co.kr/v1/search/search.xml?searchall=' + keyword_to_ascii + \
                     '&target=se_adv&key=' + api_key + \
                     '&pagecount=' + search_count

    api_response = call_api(request_string)
    parse_api_response(api_response, journals)

    try:
        os.remove(out_file)
    except Exception as e:
        print("File Remove error ", e)

    for j in journals:
        j.printout()
        j.append_to(out_file)





