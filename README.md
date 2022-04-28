Microsoft Interview Round 1
Candidate Name: L.Swetha 
Email: klswethas@gmail.com
Position: Developer Community Product Manager
HR in contact: Cecilia Maria Melany S <ceciliama@microsoft.com>

Index: 
1.  [Given Exercise Question](#given-exercise-question)
2.  [Short Answer Explanation](#short-answer-explanation)
3.  [Algorithm](#algorithm)
4.  [Time And Space Complexity](#time-and-space-complexity)
5.  [Sharing Online Compiler to run](#online-compiler)/ [Click Here To Run Code](https://onlinegdb.com/4xgTAhYJo)
6.  [Code](https://github.com/LSwethanara/Microsoft_Interview_Round1/blob/main/main.py)
7.  [Code Index](#codeindex)
8.  [TestCases](#testcases)
9.  [Dry Run Screenshots](#dry-run-screenshots)
10. [Alternative Methods][#alternatives]

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
[Click Here To Run the Code](https://onlinegdb.com/4xgTAhYJo)



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
   ![TESTCASE1](https://user-images.githubusercontent.com/13202839/165770502-995499f1-f0a9-459a-a7d8-b51586ed4730.PNG)

   
