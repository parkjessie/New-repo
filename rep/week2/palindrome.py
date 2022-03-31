
class palindrome :

    # initializing
    def __init__(self,number) :
        self.num = number
        
    
    def isPalindrome(self) :

       
        temp = self.num


        result = 0

        
        while(temp != 0) :
            
            rem = temp % 10

            result =  result * 10 + rem

            # integer division
            temp //= 10

      
        if self.num == result :
            print(self.num,"is Palindrome")
        else :
            print(self.num,"is not Palindrome")



def palinprint() :
    
 
    num = 151
    
    
    palindrome_Palindrome = palindrome(num)
    palindrome_Palindrome.isPalindrome()
    
if __name__ == "__main__":
   palinprint()

