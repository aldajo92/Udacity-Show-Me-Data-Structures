## Active Directory ##

This problem was resolved using recurssion, starting from the root, checking if user is present for each group visited, if the user matches then it returns.

The worst case is if the user is not present on any group and the group structure has the same subgroups on each, taking O(n!) worst case, since a stack if used for recurssion the space complexity would be O(n)