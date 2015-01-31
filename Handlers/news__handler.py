import tornado
from auth__handler import BaseHandler
from models import News, Category

class NewsNewHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args):
        # print str(*args[0])
        # return
        # self.render("news-new.html")
        cat_id=args[0]
        # print "category id is: "+cat_id
        catInfo = Category.select().where(Category.id == cat_id).get()
        self.render("news-new.html",category=catInfo)

    def post(self, *args):
        cat_id = args[0]
        news_title=self.get_argument("news-title")
        news_body=self.get_argument("news-body")
        news_date=self.get_argument("news-date")
        au_id=self.GetAuthorIdByEmail(self.current_user)
        News.create(
            title=news_title,
            body=news_body,
            date=news_date,
            author=au_id,
            category=cat_id,
        )
        self.write("Item saved...")
        self.redirect("/category")
class NewsEditHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,*args):
        news_id=args[0]
        news_info = News.select().where(News.id == news_id).get()
        self.render("news-edit.html", news=news_info)

    def post(self, *args):
        news_id = args[0]
        news_info = News.select().where(News.id == news_id).get()
        news_info.title = self.get_argument("title")
        news_info.body = self.get_argument("body")
        news_info.date = self.get_argument("date")
        news_info.save()
        self.write("Saved Changes.")

class NewsCategoryHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args):
        cat_id=args[0];
        news_cat=News.select().join(Category).where(Category.id==cat_id)
        # print(cat_news)
        self.render('news-category.html', news_category = news_cat)


class NewsDeleteHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args):
        news_id=args[0]
        news_Info = News.select().where(News.id == news_id).get().delete_instance()
        self.redirect("/category")
        print str(news_id)

class NewsHandler(BaseHandler):
    pass

