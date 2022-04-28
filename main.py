#Algo Explanation: In-Place Method
#1. User inputs two lists
#2. Within the SortedMerge() function, Compare ListA's head & ListB's head 
#3. Assign head1 to the lowest, and head2 to the higher of the two heads
#4. Assign a 'result' list to point to head1(which we will sort), to return later
#5. Use a tmp var to point to current list as we sort
#6. Which means at first tmp points to head1
#7. Move head1 to next element. Compare head1 & head2 iteratively, and point tmp to head1
#8. If head1 has higher value, loop is broken, point tmp's next to head2
#7. and swap head1 and head2(So head1 always points to least)
#8. Once this is done iteratively, return result to get the final sorted list

# CODE INDEX
###### 1. Time and Space Complexity - Why In-place interative merge is the best method
###### 2. Code Starts -> Define List Node
###### 3. List Operation Class
###### 4. SortedMerge Function using the Best method: in-place
###### 5. TestCases for User Input with suggested TCs and any other input

###### 1. Time and Space Complexity - Why In-place interative merge is the best method
# Using In-Place iterative(Best) method, Python3 program to merge two sorted linked lists.

"""With the following time & Space complexity, in-place merge is the best mehtod

TIME COMPLEXTITY = O(N + M)
SPACE COMPLEXITY = O(1)
where, N & M are length of the two lists """


############################ 2. Code Starts -> Define List Node ##########
############################ Define List Node ############################
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
############################ 3. List Operation Class #########################        
############################ List Operation Class ############################
# 2. Class for List operations: DefineList, PrintList, AddToList(creation), CheckInputList

class LinkedList:
    def __init__(self):
        self.head = None
 
    # Function To Display List
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
 
    # Function To Add Element To List (creating the list)
    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
 
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
        if newData < last.data:
            print("Input list is not sorted, please enter sorted list\n")
            exit()
            
############################ 4. SortedMerge Function using the Best method: in-place ###
############################ SortedMerge Function ######################################        
# SortedMerge function merges two sorted lists in-Place iteratively
# This is done by continually comparing and swaping Head nodes iteratively
# We do not use any external list as dummy here to optimize for space

def SortedMerge(head1, head2):
    if (head1 == None):
        return head2
    if (head2 == None):
        return head1
    #Initial comparison, swap to keep head1.data the least    
    if (head1.data > head2.data): 
        switch = head1.data
        head1.data = head2.data
        head2.data = switch
    #Assign the result to this, so we can return it at last once we sort     
    result = head1
    while head1!=None and head2!=None:
        tmp = None
        while head1!=None and head1.data<=head2.data:
            tmp = head1
            head1 = head1.next
        tmp.next = head2
    #swap
        swap = head1
        head1 = head2
        head2 = swap
        
    return result

############################ 5. TestCases for User Input with suggested TCs and any other input ###
############################ TESTCASES #############################         
print("In-Place Merge(best): Time Complexity=O(n+m), Space Complexity=O(1)\n")
print("SUGGESTED TESTCASES: \n")
print("TC1: Question Prompt:                listA = 5->10->15; listB = 2->3->20\n")
print("TC2: Duplicate Values:               listA = 5->10->15->20; listB = 2->5->20\n")
print("TC3: Invalid(Unsorted) Input List:   listA = 10->5->15->20; listB = 2->3->20\n")
print("TC4: Any other Input of your choice\n")

##### TESTCASES IN DRY RUN: Suggested TESTCASES

#TC1
# TEST CASE 1(TC1): EXAMPLE LIST FROM QUESTION PROMPT 
# TC1_listA = 5->10->15; TC1_listB = 2->3->20

#TC2
# TEST CASE 2(TC2): LISTS WITH DUPLICATES 
# TC2_listA = 5->10->15->20; TC2_listB = 2->5->20

#TC3
# TEST CASE 3(TC3): Unsorted input list throws error 
# TC3_listA = 10->5->15; TC3_listB = 2->5->20

#YOUR INPUT 
#Any other input of your choice can be tried 



######## Get User Inputs #########
######## LIST A ##########
print("\nGive Your Inputs: ")
#Get user_listA from user
input_string = input('Enter elements of listA separated by space ')
print("\n")
user_listA = input_string.split()

# Convert each user_listA elements to int type
for i in range(len(user_listA)):
    user_listA[i] = int(user_listA[i])
    
#Create LinkedList for listA
listA = LinkedList()

# Add given elements to listA 
for i in range(len(user_listA)):
    listA.addToList(user_listA[i])

######## LIST B ##########
#Get user_listB from user
input_string = input('Enter elements of listB separated by space ')
print("\n")
user_listB = input_string.split()

# Convert each user_listB elements to int type
for i in range(len(user_listB)):
    user_listB[i] = int(user_listB[i])

#Create LinkedList for listB
listB = LinkedList()

# Add given elements to listB 
for i in range(len(user_listB)):
    listB.addToList(user_listB[i])    

############ MERGE #################
# Call the SortedMergemerge function
listA.head = SortedMerge(listA.head, listB.head)

# Print Sorted Merged list
print("Merged List given by SortedMerge()is:")
listA.printList()
print("\n")
############# By merging in-place iteratively, we have optimized maximum    ##############
############# Time Complexity: O(n + m)[n, m = length of lists]             ##############
############# Space Complexity: O(1)                                        ##############