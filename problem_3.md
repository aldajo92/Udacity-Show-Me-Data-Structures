## Huffman Coding

Here I will show each step needed to complete the algorithm and their time/space complexity and at the end the final time/space.

### Characters Frequencies ###
This method get the input and count how many times is each caracter on the input data, then this information is stored on a map using the char as key and frequencie as value, time and space complexity O(n)

### Sort Frequencies ###
Takes the output from the previous function and sort it time complexity (n)*log(n) space complexity O(n)

### MapFrequenciesToNodes ###
Each item on the sorted list is mapped to a list of nodes, doing it this way its easier to manipulate the data, time and space O(n)

### Huffman Encoding ###
Method whose responsibility is to create the tree, the previous named functions are used here, then start creating the tree, it takes the sorted list and start removing the elements from the top of the list until there is only one element left , this operation takes O(1) * O(n-1) which is O(n)

### Encode Tree ###
Once the elements are placed on the tree, this method generates the code for each char in the tree, placing a 0 if traverses to the left or 1 to the right, finally returns a map with each generated code , time and space O(n)

the whole encode operation takes O(n) * log(n) as worst case scenario

to decode the tree recurssion is used, the method iterates through the entire encoded string and traverses the tree finding the desired value on the branch the time and space complexity for this operation is O(n)

### Conclusion ###
- Encode -> O((n) * log(n))
- Decode O(n)