##Anchors
#question

Microsoft Interview Round 1
Candidate Name: L.Swetha 
Email: klswethas@gmail.com
Position: Developer Community Product Manager
HR in contact: Cecilia Maria Melany S <ceciliama@microsoft.com>

Index: 
1. [Given Exercise Question](question)

Question: Merge and Sort two sorted linked lists using any language

Write a SortedMerge() function that takes two linked lists, each of which is sorted in increasing order, and merges the two together into one list which is in increasing order. SortedMerge() should return the new list. The new list should be made by splicing together the nodes of the first two lists.
For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20, then SortedMerge() should return a pointer to the head node of the merged list 2->3->5->10->15->20.


Answer In Short: This can be done in many ways, but the most Optimal way is to use In-Place Iterative Merge as it optimizes both Time and Space Complexity
Time Complexity: O(N + M), where N and M are lengths of the input sorted lists
Space Complexity: O(1), does not take any extra space since it is sorted in place using the space of one of given list var  
