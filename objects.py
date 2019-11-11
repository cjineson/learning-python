class Myclass(object):
    
    def __init__(self,name):
        self.name = name
        print('Constructor creating object - ', self.name)
        self.prefix = 'Hello'

    def sayhello(self,suffix):
        print(self.prefix + ' ' + suffix)

    def __del__(self):
        print('Destructor deleting object - ', self.name)

myobject = Myclass("myobj")
myobject.sayhello('World!') 
# note implicit call to destructor as program exits...