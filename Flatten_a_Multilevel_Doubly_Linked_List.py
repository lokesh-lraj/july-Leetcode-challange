"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: 

The input multilevel linked list is as follows:

 1---2---3---4---5---6---Null 
         |
         7---8---9---10---Null
             |
             11---12---Null
             
Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
  
Example 3:

Input: head = []
Output: []

Constraints:

Number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        nxt = []
        temp = head
        
        while temp:
            
            if temp.child:
                
                if temp.next:
                    nxt.append(temp.next)
                temp.next = temp.child
                temp.next.prev = temp
                temp.child = None
                
            elif temp.next == None and len(nxt) > 0:
                temp.next = nxt.pop()
                temp.next.prev = temp
                
            temp = temp.next
            
        return head
            
