import user
import json
class Student(user.User,list):
    def __init__(self):
        self.items=[];
        # user.User.__init__(self)
        """[for new version of python]
          call supper method for new version
        """
        super(Student,self).__init__() 
        self.classname="student"
    def append(self,item):
        self.items.append(item)
    def printInfo(self):
        print(json.dumps({"name":self.name or "appdemo","type":self.type,"version":self.version,"classname":self.classname}))
