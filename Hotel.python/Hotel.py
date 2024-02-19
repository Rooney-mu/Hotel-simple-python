#in hotel you order,get served,receive the bill and pay and get receipt
#create a class called Hotel
print("Welcome to our hotel\n we have:\nchips@100\nugali@30\ncoffe@50\nTea@78")

class Hotel:
    def __init__(self,name,table,order):
        self.name=name
        self.table=table
        self.order=order
        self.balance=0
        self.pay=0
        print(f"hello,{self.name}")
    def tables(self):
      
        if self.table<0:
            print("table not availaable")
        else:
            print("table reserved")
    def orders(self):
        chips=100
        ugali=30
        coffe=50
        print(f"{self.order}")
        if self.order=="chips":
            print(f"chips are ksh:{chips}")
            self.balance+=chips
        elif self.order=="ugali":
            print(f"ugali is ksh:{ugali}")
            self.balance+=ugali
        elif self.order=="coffe":
              print(f"tea is ksh:{coffe}")
              self.balance+=coffe
              
        else:
            print(f"not available!{chips}")
    def serving(self):
        if self.order=="chips":
            print("your order shall take 2min")
        elif self.order=="ugali":
            print("your order shall take 4min")
        elif self.order=="coffe":
              print("your order shall take 1min")
        else:
            print("")
    def balances(self):
        print(f"pay:{self.balance}")
    def pays(self,money):
        self.pay=money
        if self.pay==self.balance:
            print("payed")
        else:
            print("not payed")
    def thank(self):
        print(f"thankyou,{self.name} come back later")

        
