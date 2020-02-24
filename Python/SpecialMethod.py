 # SPECIAL METHODS
class book():
    def __init__(self,title,author,page):
        self.title = title
        self.author = author
        self.page = page
    def __str__(self):    #__str__ = SPECIAL METHOD
        return "Title: {}, Author: {}, Page: {}".format(self.title,self.author,self.page)

    def __len__(self):
        return self.page

    #def __del__(self):
        print("A book has been deleted")

b = book("python", "jose", 20)
print(b)
print(len(b))
#del b
