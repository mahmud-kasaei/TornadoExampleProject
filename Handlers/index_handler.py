import tornado
from auth__handler import BaseHandler
__author__ = 'mojtaba.banaie'


class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
            self.render('index.html',UN= "Hello!")
        # else :
        #     session.set('LoggedIn', {"_id":"12222222","name":"ali"})
        #     self.render('index.html',UN="U Are Not Logged In..")
