'''
class Cookie:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def cookies(self):


cheeseCookie = Cookie()
cheeseCookie.setName("치즈쿠키")

mintChockCookie = Cookie()
mintChockCookie.setName("민트초코쿠키")

print(cheeseCookie.getName(), mintChockCookie.getName())
'''


# class Musician:
#     job = "Rockstar"
#
#     def explanation(self):
#         print("I am a {}!".format(self.job))
#
#
# rockstar = Musician()
# rockstar.job = "rockstar"
# rockstar.explanation()
#
#
# drummer = Musician()
# drummer.job = "drummer"
# drummer.explanation()




class fourCal:
    def setNumber(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first/self.second

a = fourCal()
a.setNumber(10,4)
print(a.add())
print(a.div())
print(a.sub())
print(a.mul())