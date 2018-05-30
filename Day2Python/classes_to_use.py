# let's create our first class

class OperateOnTwoNumbers :
    def __init__(self, num1, num2, operation='division'):
        '''we initialize this class object with two numbers. these are two attributes in the class'''
        self.num1 = num1
        self.num2 = num2
        self.operation=operation
    
        
    def divide_me(self) :
        return self.num1/self.num2
    def multiply_me(self) :
        return self.num1*self.num2
    def add_me(self) :
        return self.num1+self.num2
    def subtract_me(self) :
        return self.num1-self.num2
    def execute_operation(self) :
        if self.operation =='division' :
            return self.divide_me()
        elif self.operation == 'multiplication' :
            return self.multiply_me()
        elif self.operation == 'addition' :
            return self.add_me()
        elif self.operation == 'subtraction' :
            return self.subtract_me()
        else :
            print 'Invalid Operation'
