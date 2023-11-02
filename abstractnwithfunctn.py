#abstraction with function

class Employee:
    __firstName: str = "thulasi"
    __lastName: str = "tendu"
    def __fullName(self):
        return self.__firstName+" "+self.__lastName
emp = Employee()
emp.__firstName = "ABC"
print(emp. __fullName())

class Employee:
    __firstName: str = "Thulasi"
    __lastName: str = "tendu"
   def fullName(self):
       return self.__nameFormat(self.__firstName, self.__lastName)
   def _nameFormat(self, fName: str, lName: str, ):
       return f" = {fName} {lName}"
emp = Employee()
emp._firstName = "ABC"
print(emp.fullName())
print(emp.__nameFormat('Thulasi', 'tendu'))



