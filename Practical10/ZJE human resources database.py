class Staff(object):
    def __init__(self,f_name,l_name,location,role):
        self.f_name=f_name
        self.l_name=l_name
        self.location=location
        self.role=role
    
    def information (self):
        info="full name:"+self.f_name+" "+self.l_name+" "+"location:"+self.location+" role:"+self.role
        print(info)
        return info
#example:
a=Staff("Lisa","Wang","Edinburg","faculty")
Staff.information(a)
