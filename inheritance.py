class Address:
    _address: str = ""
    def addAddress(self, address):
        self._address = address
    def getAddress(self):
        return self._address
class Employee(Address):
    _firstName: str = ""
    _lastName: str = ""
    _surName: str = ""
   def setName(self, fName: str, lName: str, sName: str = ""):
       self._firstName = fName
       self._surName = sName
       self._lastName = lName
   def _nameFormat(self):
       return f'{self._firstName} {self._lastName} {self._surName}'
   def getfullName(self):
       return self._nameFormat()
emp = Employee()
emp.setName(fName="Thulasi", sName="d", lName="tendu")
emp.addAddress("Tirupati")
print(emp.getFullName())
print(emp.addAddress())