class UniqObject(object):
    
    __instance = None
    
    def __init__(self):
        
        if UniqObject.__instance:
            print("instance exists")
        
        else:
            print("__init__ call")
    
    @classmethod
    def create_object(cls):
        if not cls.__instance:
            cls.__instance = UniqObject()
        return cls.__instance

x = UniqObject()
y = UniqObject()
print("UniqObject instances: ")
print(x.create_object(),y.create_object())
