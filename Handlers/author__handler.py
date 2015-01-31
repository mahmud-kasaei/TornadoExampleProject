import tornado
from models import *
import peewee
from auth__handler import BaseHandler

class AuthorHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        authors = Author.select()
        self.render('authors.html', authors=authors)


class AuthorNewHandler(tornado.web.RequestHandler):
     # @tornado.web.authenticated
     def get(self, *args):
       self.render("author-new.html")


     def post(self, *args):
       auName = self.get_argument("author-name")
       auFa = self.get_argument("author-family")
       auEmai=self.get_argument("author-email")
       auPass=self.get_argument("author-password")

       catInfo = Author.create(
           fn=auName,
           ln=auFa,
           email=auEmai,
           password=auPass,
       )

       self.redirect("/author")
class AuthorDeleteHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args):
        aut_id=args[0]
        autInfo=Author.select().where(Author.id==aut_id).get().delete_instance()
        self.redirect("/author")

class AuthorEditHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,*args):
        au_id=args[0]
        autInfo = Author.select().where(Author.id == au_id).get()
        self.render("author-edit.html",author=autInfo)

    def post(self, *args):
        aut_id = args[0]
        aut_info = Author.select().where(Author.id == aut_id).get()
        aut_info.fn = self.get_argument("fn")
        aut_info.ln = self.get_argument("ln")
        aut_info.save()
        self.redirect("/author")

# class get_author