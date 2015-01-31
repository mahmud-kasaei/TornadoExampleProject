import tornado
from models import Author
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

    def GetAuthorIdByEmail(self,author_email):
        try:
            author = Author.get(Author.email == self.get_secure_cookie("user") )
            return author.id
        except Author.DoesNotExist:
            return None

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = self.current_user
        self.write("Hello, " + name+ " ----- "+str(self.GetAuthorIdByEmail(name)))

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        # if self.get_argument(au-mail) with the same self.get_argument(au-pass)in author table then author is satisfy
        if self.get_author():
            self.set_secure_cookie("user", self.get_argument("au-mail"))
            self.redirect("/test")
        else:
            self.write("does no exist.")
    def get_author(self):
        try:
            author = Author.get(Author.email == self.get_argument("au-mail"), Author.password == self.get_argument("au-pass"))
            return author
        except Author.DoesNotExist:
            return None


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.write("You are now logged out")