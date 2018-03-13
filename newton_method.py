#This class is writen by Pengfei Xiong to do OR504 final problem 5.
class newton(object):

    def __init__(self, f, df,  guess=1, update=100, percision=1e-6):
        self.f = f
        self.df = df
        self.percision = percision
        self.x = guess

    def enough(self, old, new):
        return abs(old-new) <= self.percision

    def renew(self):
        self.x -= self.f(self.x)/self.df(self.x)

    def newton_method(self, max_update=100):
        k = 0
        while not self.enough(self.f(self.x),0) and k <= max_update:
            self.renew()
            k+=1
        return self.x

