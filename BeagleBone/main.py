import tornado.ioloop
import tornado.web
import os.path

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.render("template.html", title="My title",
        self.render("EventCreator.html")

    def post(self):

        data = self.get_argument('eventName', 'No data received')
        print data
        self.write("Thank You for submitting an event." + data);

settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "template"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )

app = tornado.web.Application([
    (r"/", MainHandler)
], **settings)

if __name__ == "__main__":
    print 'Server Running...'
    print 'Press ctrl + c to close'
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
