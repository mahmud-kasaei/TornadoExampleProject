import tornado
from models import *
import peewee

class AuthorHandler(tornado.web.RequestHandler):
    def get(self):
        authors = Author.select()
        self.render('authors.html', authors=authors)

class AuthorNewHandler(tornado.web.RequestHandler):
     def get(self, *args):
       self.render("author-new.html")


     def post(self, *args):

       auName = self.get_argument("author-name")
       auFa = self.get_argument("author-family")
       # auEmai=self.get_argument("author-email")
       # auPass=self.get_argument("author-password")

       catInfo = Author.create(
           fn=auName,
           ln=auFa,

       )

       self.redirect("/author")
class AuthorDeleteHandler(tornado.web.RequestHandler):
    def get(self, *args):
        aut_id=args[0]
        autInfo=Author.select().where(Author.id==aut_id).get().delete_instance()
        self.redirect("/author")

class AuthorEditHandler(tornado.web.RequestHandler):
    def get(self,*args):
        au_id=args[0]
        autInfo = Author.select().where(Author.id == au_id).get()
        # print autInfo.fn
        # return
        self.render("author-edit.html",author=autInfo)
        print "hello"

    def post(self, *args):
        aut_id = args[0]
        aut_info = Author.select().where(Author.id == aut_id).get()
        aut_info.fn = self.get_argument("fn")
        aut_info.ln = self.get_argument("ln")
        aut_info.save()
        self.redirect("/author")