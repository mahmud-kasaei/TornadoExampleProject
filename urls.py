__author__ = 'mojtaba.banaie'
from Handlers.index_handler import IndexHandler
from Handlers.category__handler import CategoryHandler, CategoryEditHandler, CategoryDeleteHandler, CategoryNewHandler
from Handlers.author__handler import AuthorHandler, AuthorNewHandler, AuthorDeleteHandler, AuthorEditHandler

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
]