__author__ = 'mojtaba.banaie'
from Handlers.index_handler import IndexHandler
from Handlers.category__handler import CategoryHandler, CategoryEditHandler, CategoryDeleteHandler, CategoryNewHandler
from Handlers.author__handler import AuthorHandler, AuthorNewHandler, AuthorDeleteHandler, AuthorEditHandler
from Handlers.auth__handler import LoginHandler, MainHandler, LogoutHandler
from Handlers.news__handler import NewsNewHandler, NewsEditHandler, NewsCategoryHandler, NewsDeleteHandler

urlList  = [
    (r'/', IndexHandler),
    (r'/category$', CategoryHandler),
    (r'/category/edit/(\d+)$', CategoryEditHandler),
    (r'/category/delete/(\d+)$', CategoryDeleteHandler),
    (r'/category/new$', CategoryNewHandler),
    (r'/author/new$', AuthorNewHandler),
    (r'/author', AuthorHandler),
    (r'/author/delete/(\d+)$', AuthorDeleteHandler),
    (r'/author/edit/(\d+)$', AuthorEditHandler),
    (r"/login", LoginHandler),
    (r"/test", MainHandler),
    (r"/logout", LogoutHandler),
    (r"/news/new/(\d+)$", NewsNewHandler),
    (r"/news/edit/(\d+)$", NewsEditHandler),
    (r"/news/category/(\d+)$", NewsCategoryHandler),
    (r"/news/delete/(\d+)$", NewsDeleteHandler),
]