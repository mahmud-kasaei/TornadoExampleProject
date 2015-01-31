import tornado
from  models import *
import peewee
from auth__handler import  BaseHandler

__author__ = 'mojtaba.banaie'

class CategoryHandler(BaseHandler):
     @tornado.web.authenticated
     def get(self):
        categories = Category.select()
        self.render('categories.html', categories = categories)


class CategoryEditHandler(BaseHandler):
     @tornado.web.authenticated
     def get(self, *args):
       cat_id=args[0]
       catInfo = Category.select().where(Category.id == cat_id).get()
       self.render("category-edit.html", category=catInfo)


     def post(self, *args):
       cat_id=args[0]
       catInfo = Category.select().where(Category.id == cat_id).get()


       catInfo.name = self.get_argument("category-name")
       catInfo.save()


       self.redirect("/category")



class CategoryDeleteHandler(BaseHandler):
     @tornado.web.authenticated
     def get(self, *args):
       cat_id=args[0]
       catInfo = Category.select().where(Category.id == cat_id).get().delete_instance()
       self.redirect("/category")
       print "hello world."


class CategoryNewHandler(BaseHandler):
     @tornado.web.authenticated
     def get(self, *args):
       self.render("category-new.html")


     def post(self, *args):

       catName = self.get_argument("category-name")
       catInfo = Category.create(
           name=catName
       )

       self.redirect("/category")