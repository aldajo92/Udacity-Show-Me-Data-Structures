## Union and Intersection of Two Linked Lists ##

- Union: in the first list, all elements are stored into a set, removing duplicated. The second list do a check if the element is not already on the set, then adding the respective element on the tail. time complexity O(n) space O(n)

- Intersection: in the first list all elements are stored into a set. The second list check if the element is on the set, if pass, the element is added to the linked list. time complexity O(n) space O(n)