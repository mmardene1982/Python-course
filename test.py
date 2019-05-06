from datetime import date

now = date.today()
now = int(now.strftime('%Y'))

class person:

    def __init__(self, Fname,Sname , db):
        self.Fname=Fname
        self.Sname= Sname
        self. db= db
    def getAge(self):
        return now - self.db
    def __str__(self):
        return '{} {} ({})'.format(self.Sname, self.Fname, self.getAge())

class employee(person):
    def __init__(self,Fname,Sname, db):
        person.__init__(self, Fname,Sname,db)
        self.imployeeNr='300'
    def getImpNr(self):
        return self.imployeeNr+'262'
    def __str__(self):
        return '{} {} Your ID number is {}'.format(self.Fname, self.Sname, self.getImpNr())



maher=person('Maher', 'Mardini',1982)
maher1=employee('Maher', 'Mardini',1982)
print(maher)
print(maher1)