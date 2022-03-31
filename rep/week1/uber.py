class uber:
    
    #Initialise for first iteration
    numberofubers  = 0

    def __init__(self,name,age,bill):
        self.name = name
        self.running = age
        self.bill = bill
        uber.numberofubers  =  uber.numberofubers + 1

    #Returns average price per km
    def rateperkm(self):
        return self.bill/self.running
        
    #Returns number of cabs running         
    @classmethod
    def noofcabs(cls):
        return cls.numberofcabs


def driver():
  firstuber  = uber("Bob", 60, 900) 
  print(firstuber.name)
  print(firstuber.bill)

    

  

if __name__ == "__main__":
  driver()

