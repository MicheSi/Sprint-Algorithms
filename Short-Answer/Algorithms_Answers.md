#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - as size of n increases, the run time will grow at the same rate


b) O(n log n) - the for loop is O(n) and the while loop is O(log n)


c) O(n) - run time grows at the same rate as the size of bunnies

## Exercise II
define function drop_egg with parameters n for # of stories & f for floor #
    set variable for number of eggs broken
    loop through # of stories n
        if n is >= f:
            egg breaks - increase # of eggs broken
        if n < f:
            eggs broken stays the same
    return total # of eggs broken

run time - O(log n) using binary search

