class computer:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def show(self):
        print("a= ",self.a,"b= ",self.b)

comp1=computer(3,4)
comp2=computer(5,6)

comp1.show()
comp2.show()