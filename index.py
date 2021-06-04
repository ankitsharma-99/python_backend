import tornado.web
import tornado.ioloop
import json


class mainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if num.isdigit():
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer.")


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        self.write(f"Welcome {studentName} you are viewing course {courseId}")


class jsonListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))

    def post(self):
        fh = open("list.txt", "a")
        fruit = self.get_argument("fruit")
        fh.write(f"\n{fruit}")
        fh.close()
        self.write(json.dumps({"message": "fruit added successfully."}))


if __name__ == "__main__":
    app = tornado.web.Application(
        [
            (r"/", mainRequestHandler),
            (r"/animals", listRequestHandler),
            (r"/isEven", queryParamRequestHandler),
            (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler),
            (r"/list", jsonListRequestHandler),
        ]
    )

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()