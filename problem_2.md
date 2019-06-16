## Finding Files ##

This problem use a combination of recursion and iteration over each folder, because we don't know the structure of the folder. We need to go through the entire file directory to verify each file and adding to the list if is correct. So time complexity is O(n) and since recurssion is used the previous recursive calls will be stored on a stack giving us O(n) in terms of space.