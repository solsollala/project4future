# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# DBpia 객체내 Author 클래스
# ----------------------------------------------------------------------------
class Author:
    def __init__(self, order="", url="", name=""):
        self.order = str(order)
        self.url = str(url)
        self.name = str(name)

    def get_author_info(self):
        return self.order + ":" + self.name + ":" + self.url

# ----------------------------------------------------------------------------
# DBpia 객체내 Publication 클래스
# ----------------------------------------------------------------------------
class Publication:
    def __init__(self, name="", issn="", isbn10="", isbn13=""):
        self.name = str(name)
        self.issn = str(issn)
        self.isbn10 = str(isbn10)
        self.isbn13 = str(isbn13)

# ----------------------------------------------------------------------------
# DBpia 객체내 Issue 클래스
# ----------------------------------------------------------------------------
class Issue:
    def __init__(self, name="", num="", yymm=""):
        self.name = str(name)
        self.num = str(num)
        self.yymm = str(yymm)

# ----------------------------------------------------------------------------
# DBpia 객체 클래스
# ----------------------------------------------------------------------------
class Dbpia_Item:
    def __init__(self):
        self.title = ""
        self.Authors = []
        self.publisher = ""
        self.publication = Publication()
        self.issue = Issue()
        self.pages = ""
        self.link_url = ""
        self.con_txt = ""
        self.summary_txt = ""
        self.keywords = []
        self.dreg_name = ""  # KCI등재여부 등
        pass

    def set_publication(self, name="", issn="", isbn10="", isbn13=""):
        self.publication.name = str(name)
        self.publication.issn = str(issn)
        self.publication.isbn10 = str(isbn10)
        self.publication.isbn13 = str(isbn13)
        pass

    def set_issue(self, name="", num="", yymm=""):
        self.issue.name = str(name)
        self.issue.num = str(num)
        self.issue.yymm = str(yymm)
        pass

    def add_keywords(self, keyword):
        self.keywords.append(keyword)
        pass

    def get_authors_nameonly(self):
        out = ""
        for obj in self.Authors:
            out += ("," + obj.name)
        return out.lstrip(',')

    def get_authors(self):
        out = ""
        for obj in self.Authors:
            out += ("," + obj.get_author_info())
        return out.lstrip(',')

    def get_publication(self):
        str = self.publication.name + ":" + self.publication.issn + ":" + self.publication.isbn10 + ":" + self.publication.isbn13
        return str

    def get_issue(self):
        str = self.issue.name + ":" + self.issue.num + ":" + self.issue.yymm
        return str

    def get_keywords(self):
        keywords = "".join(self.keywords)
        keywords = keywords.replace("#",":") # 키워드 앞에 붙어 있는 #을 콤머로 대체
        return keywords.lstrip(':') # 맨 앞의 : 제거

    # ----------------------------------------------------------------------------
    def append_to(self, path):
        try:
            f = open(path, "a", encoding='utf8', newline="\r\n")
            print("%s#%s#%s#%s#%s#%s#%s#%s#%s#%s" \
                  % (self.title, self.get_authors_nameonly(), self.publisher, self.get_publication(), self.get_issue(), \
                  self.pages, self.link_url, self.con_txt, self.summary_txt, self.get_keywords()), file=f)
            f.close()
        except Exception as e:
            print("File I/O error ", e)

    # ----------------------------------------------------------------------------
    def printout(self):
        try:
            print("%s#%s#%s#%s#%s#%s#%s#%s#%s#%s" \
                  % (self.title, self.get_authors_nameonly(), self.publisher, self.get_publication(), self.get_issue(), \
                  self.pages, self.link_url, self.con_txt, self.summary_txt, self.get_keywords()))
        except Exception as e:
            print("Print error ", e)

    # ----------------------------------------------------------------------------






