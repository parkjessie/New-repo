class ListNode:
    def __init__(self, y):
        self.val = y
        self.next = None
        
class Solution:
    def __init__(self,seq):
       
        self.head = None
        for item in seq:
            node = ListNode(item)
            node.next = self.head
            self.head = node


    def palindrome(self):
        
        node = self.head
        var = node 
        prev = None 
    
      
        while var and var.next:
            var = var.next.next
            temp = node.next   
          
            node.next = prev
            prev = node
            node = temp
    
        if var:  # in case of odd num elements
            tail = node.next
        else:    # in case of even num elements
            tail = node
    
        while prev:
          
            if prev.val == tail.val:
                tail = tail.next
                prev = prev.next
            else:
                return False
        return True

if __name__ == "__main__":
  
 list_1 = Solution([7, 8, 6 ,  3 , 7 ,3 , 6, 8, 7])
 print([7, 8, 6 ,  3 , 7 ,3 , 6, 8, 7],end='->')
 print(list_1.palindrome())
 list_2 = Solution([6 , 3 , 4, 6])
 print([6 , 3 , 4, 6],end='->')
 print(list_2.palindrome())
 list_3 = Solution([3, 7 ,3 ])
 print([ 3 , 7, 3],end='->')
 print(list_3.palindrome())
 list_4 = Solution([1])
 print([1],end='->')
 print( list_4.palindrome())

