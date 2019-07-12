class Target(object):
    def request(self):
        print("普通请求")

class Adaptee(object):
    def special_request(self):
        print("特殊请求")

class Adapter(Target):
    def __init__(self):
        self.adaptee = Adaptee()
    def request(self):
        self.adaptee.special_request()

if __name__ == '__main__':
    target = Adapter()
    target.request()
