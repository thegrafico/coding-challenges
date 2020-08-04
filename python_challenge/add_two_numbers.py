"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        done, n1, n2 = False, "", ""

        while not done:
            #Create String of element with each list
            if l1:
                n1 += str(l1.val)
            if l2:
                n2 += str(l2.val)
                
            #Mapping the ListNode
            l1, f1 = self.get_next(l1)
            l2, f2 = self.get_next(l2)
            
            #Get out of the loop
            if f1 and f2:
                done = True
                
        #Reversing string
        val_node1 = int(n1[::-1].strip()) 
        val_node2 = int(n2[::-1].strip())
        
        #Sum of both elements
        result = val_node1 + val_node2
        #print(val_node1, "+", val_node2, "=", result)
        
        #Reversing sum of both numbers
        result = str(result)[::-1]
        
        #Create ListNode
        new_node = self.create_node(result)
        
        return new_node
            
            
    def get_next(self, l:ListNode)-> [ListNode, bool]:
        return [l.next, False] if l else [None, True]

     def create_node(self, numbers: str)-> ListNode:
        print("CREATING NODE WITH =>", numbers)
    
        #Creating list of ListNodes
        list_nodes = [ListNode(int(char)) for char in numbers]
        
        #size of array -1, to don't add the last element
        tam = len(list_nodes) - 1    
        
        #Loop in reverse
        for i in range(len(list_nodes)-1, -1, -1):
            #jump to the other iter if this condition is meet
            if i == tam:
                continue
                
            #Add the elements in reverse order, from last to first
            list_nodes[i].next =list_nodes[i+1] 
        
        #Return the firts one wich have all the elements 
        return list_nodes[0]
    
    def print_listNode(self, l:ListNode) -> None:
        done = False
        while not done:
            if l:
                print(l.val, end=" - ")
            l, done = self.get_next(l)
        print()


#node 1
node1 = ListNode(5)
node1.next = ListNode(0)
(node1.next).next = ListNode(0)
((node1.next).next).next = ListNode(0)
# print(node1.val,((node1.next).val) ,((node1.next).next).val)

#node 2
node2 = ListNode(2)
node2.next = ListNode(0)
(node2.next).next = ListNode(0)
# print(node2.val, ((node1.next).val), ((node2.next).next).val)

solution = Solution()
solution.addTwoNumbers(node1, node2)