



class Abbb:
    def __init__(self,name='',age='10'):
        self.name = name
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if  0< int(age) <= 150:
            self.__age = age

        else:
            raise  'age is Error'

class Anitor:
    def __init__(self,name,age,heigh):
        self.age = age
        self.name = name
        self.heigh = heigh

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if 0<value<150:
            self.__age = value
        else:
            raise 'value is Error'

    @property
    def heigh(self):
        return self.__heigh

    @heigh.setter
    def heigh(self, value):
        if 0 < value < 20:
            self.__heigh = value
        else:
            raise 'value is Error'
#
# A = Abbb('cdcd','5')
# print(A.get_age())
s = Anitor('aa',15,15)
print(s.age)
print(s.heigh)
print(s.name)
print(s.__dict__)

