from  abc import  ABCMeta,abstractmethod

class Builder():
    __metaclass__= ABCMeta

    @abstractmethod
    def draw_arm(self):
        pass

    @abstractmethod
    def draw_leg(self):
        pass

    @abstractmethod
    def draw_head(self):
        pass
class Thin(Builder):
    def draw_arm(self):
        print("画瘦子手")

    def draw_leg(self):
        print("画瘦子腿")

    def draw_head(self):
        print("画瘦子头")

class Fat(Builder):
    def draw_arm(self):
        print("画胖子手")

    def draw_leg(self):
        print("画胖子腿")

    def draw_head(self):
        print("画胖子头")

class Director(object):
    def __init__(self,person):
        self.person =person

    def draw(self):
        self.person.draw_arm()
        self.person.draw_leg()
        self.person.draw_head()

if __name__ == '__main__':
    thin =Thin()
    fat = Fat()
    director_thin = Director(thin)
    director_thin.draw()
    director_fat = Director(fat)
    director_fat.draw()



