Microsoft Interview Round 1<br />
Candidate Name: L.Swetha <br />
Email: klswethas@gmail.com<br />
Position: Developer Community Product Manager<br />
HR in contact: Cecilia Maria Melany S <ceciliama@microsoft.com><br />

Index: 
1.  [Given Exercise Question](#given-exercise-question)
2.  [Short Answer Explanation](#short-answer-explanation)
3.  [Algorithm](#algorithm)
4.  [Time And Space Complexity](#time-and-space-complexity)
5.  [Sharing Online Compiler to run](#online-compiler)/ [Click Here To Run Code](https://onlinegdb.com/JOwTqrbFj)
6.  [Code](https://github.com/LSwethanara/Microsoft_Interview_Round1/blob/main/main.py)
7.  [Code Index](#code-index)
8.  [TestCases](#testcases)
9.  [Dry Run Screenshots](#dry-run-screenshots)
10. [Alternative Methods](#alternative-methods)
11. [Conclusion](#conclusion)
12. [Thank You Note](#thank-you-note)

### Given Exercise Question
<a name = '#given-exercise-question'></a>

Merge and Sort two sorted linked lists using any language
Write a SortedMerge() function that takes two linked lists, each of which is sorted in increasing order, and merges the two together into one list which is in increasing order. SortedMerge() should return the new list. The new list should be made by splicing together the nodes of the first two lists.
For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20, then SortedMerge() should return a pointer to the head node of the merged list 2->3->5->10->15->20.



### Short Answer Explanation
<a name = '#short-answer-explanation'></a>
Merging and sorting two sorted lists can be done in [many ways](#alternatives), but the most Optimal way is to use [**In-Place Iterative Merge**](#algorithm) as it optimizes both Time & Space Complexity

a. [Time Complexity](#complexity): O(N + M), where N and M are lengths of the input sorted lists
b. [Space Complexity](#complexity): O(1), does not take any extra space since it is sorted in place using the space of one of given list var 



### Algorithm
<a name = '#algorithm'></a>
Algoithm Explanation: In-Place Method
1. User inputs two lists
2. Within the SortedMerge() function, Compare ListA's head & ListB's head 
3. Assign head1 to the lowest, and head2 to the higher of the two heads
4. Assign a 'result' list to point to head1(which we will sort), to return later
5. Use a tmp var to point to current list as we sort
6. Which means at first tmp points to head1
7. Move head1 to next element. Compare head1 & head2 iteratively, and point tmp to head1
8. If head1 has higher value, loop is broken, point tmp's next to head2
7. and swap head1 and head2(So head1 always points to least)
8. Once this is done iteratively, return result to get the final sorted list
TDLR: We will iterate the head1 of the list to point to the lowest while traversing both the list. 




### Time And Space Complexity
<a name = '#time-and-space-complexity'></a>
**Time Complexity** for the [Code](https://github.com/LSwethanara/Microsoft_Interview_Round1/blob/main/main.py) is: **O(N + M)**, where N and M are the length of the two lists since it traverses through both the list to sort. 
**Space Complexity** for the [Code](https://github.com/LSwethanara/Microsoft_Interview_Round1/blob/main/main.py) is: **O(1)**. That is it does not use any extra space. The code uses one of the given list(the one with the lowest first value) as its anchor and modifies the same list. This is the best and most optimal way save space. 

Overall this algotrithm is the **most optimal solution** keeping the time and space complexity to the least. 



### Online Compiler
<a name = '#online-compiler'></a>
The user can directly go to the following link to execute the code: 
[Click Here To Run the Code](https://onlinegdb.com/JOwTqrbFj)



### Code
<a name = '#code'></a>
The code is uploaded here in github as well: [main.py](https://github.com/LSwethanara/Microsoft_Interview_Round1/blob/main/main.py)



### Code Index
<a name = '#code-index'></a>
The following code index is commented in the code as well. This is for readability. 
The code has the following five parts 
1. Time and Space Complexity - Why In-place interative merge is the best method
2. Code Starts -> Define List Node
3. List Operation Class
4. SortedMerge Function using the Best method: in-place
5. TestCases for User Input with suggested TCs and any other input
     - suggested testcases are commented in the code and is prompted in the I/O as well


### TESTCASES
<a name = '#testcases'></a>
The following are the suggested exhaustive testcases. 
Please feel free to use your own inputs as well. The code will work for any int input given 

1. **TEST CASE 1(TC1)**: EXAMPLE LIST FROM QUESTION PROMPT 
   TC1_listA = 5->10->15; TC1_listB = 2->3->20

2. **TEST CASE 2(TC2)**: LISTS WITH DUPLICATES 
   TC2_listA = 5->10->15->20; TC2_listB = 2->5->20

3. **TEST CASE 3(TC3)**: UNSORTED INPUT LISTS THROWS ERROR (INVALID INPUT) 
   TC3_listA = 10->5->15; TC3_listB = 2->5->20

4. **YOUR INPUT**: Please feel free to test as you like. 



### Dry Run Screenshots
<a name = '#dry-run-screenshots'></a>

1. **TEST CASE 1(TC1)**: EXAMPLE LIST FROM QUESTION PROMPT 
   TC1_listA = 5->10->15; TC1_listB = 2->3->20
   ![TESTCASE1](https://user-images.githubusercontent.com/13202839/165770961-3126026a-f3dd-46f6-b95a-c2b6630e15e9.PNG)

2. **TEST CASE 2(TC2)**: LISTS WITH DUPLICATES 
   TC2_listA = 5->10->15->20; TC2_listB = 2->5->20
   ![TESTCASE2](https://user-images.githubusercontent.com/13202839/165771035-b0683e60-472d-42e5-83da-c1db276e5c7f.PNG)
   
3. **TEST CASE 3(TC3)**: UNSORTED INPUT LISTS THROWS ERROR (INVALID INPUT) 
   TC3_listA = 10->5->15; TC3_listB = 2->5->20
   ![TESTCASE3](https://user-images.githubusercontent.com/13202839/165771105-77ecbd8a-4cf4-423b-b4c4-9a7a4262aa3f.PNG)


### Alternative Methods
<a name = '#alternative-methods'></a>

There are other ways to solve the same execise. But they are not the most optimal ways. 
1. Second Best: Recursive In-Place Method: 
    In this method, a SortedMerge() function is written where the current node of both the lists are compared. The node with the smaller value is added to the Output       list. This function is recursively called to merge the remaining list. 
    
    - **Time Complexity:** O(N + M), where N and M are the lengths of the two lists
    - **Space Complexity:** O(N + M), where N and M are the lengths of the two lists **{not the most optimal}**
   
2. Not Great: Using Pointer: 
     Use a Dummy node, that will hold the smaller value after comparing the values of the nodes that is pointed during iterating through both the list. This Dummy node      will be apended to the Output 
     
    - **Time Complexity:** O(N + M), where N and M are the lengths of the two lists
    - **Space Complexity:** O(N + M), where N and M are the lengths of the two lists **{not the most optimal}**

3. Worst: Join the list and sort
      We can brute force the problem, by joining the lists and then sorting them. But this will have the worst time complexity 
     
    - **Time Complexity:** O((N + M)^2), where N and M are the lengths of the two lists since it combines and then sorts **{not optimal at all}**
    - **Space Complexity:** O(1), insertion sort   
     
### Conclusion
<a name = '#conclusion'></a>
Thus we can conclude that In-Place Iterative Merging is the best way to Merge & Sort two sorted input lists since it has the least time & space complexity  

### Thank You Note
<a name = '#thank-you-note'></a>
Thank you for taking the time to go through my work. Please use the [compiler](#online-compiler) to take a look at the code & run the code.
Or take a look at the code as mentioned in the section ['Code'](#code)

This was written entirely by the author: L.Swetha - the candidate for the Mocrosoft Interview Round 1 for the position Developer Community Product Manager. 
Please feel free to contact me using the follwoing : klswethas@gmail.com
Phone Number: 9840318244

