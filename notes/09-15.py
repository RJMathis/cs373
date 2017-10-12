# -----------
# Fri, 15 Sep
# -----------

"""
exceptions
types

finish the overview of types
operators

look up in a set is O(1)

look up of a key   in a dict is O(1)
look up of a value in a dict is O(n)

like a set, dict can not have duplicate keys
dict keys must be hashable

list has a FRONT-loaded array
costs
    insertion at the back:   O(1), amortized
    insertion anywhere else: O(n)
    indexing:                O(1)

stack (LIFO) using list
fine as long as I use the back

queue (FIFO) using list
not very attractive

a deque has a MIDDLE-loaded array
costs
    insertion at the back:   O(1), amortized
    insertion at the front:  O(1), amortized
    indexing:                O(1)

functions that take other functions as arguments
are called higher-order functions
"""

def f (...) :
    ...

sort(..., f)
sort(..., lambda ...)

"""
in Java   the names of the constructors are the names of the classes
in Python the name  of the constructor  is __init___

Java has overloading
Python does not
"""

i = 2
j = 3
k = (i + j)
k = (2 + 3)

"""
l-value is the name of the something that can be on the
left hand side of an assignment (e.g, i, j, NOT 2, 3)

r-value is the name of the something that can NOT be on the
left hand side of an assignment (e.g. 2, 3)

+ takes two r-values, produces an r-value
"""

i += j
i += 3
2 += 3 # not ok

"""
+= takes an l-value and an r-value, produces no value
"""

k = (i + j)
(i + j) = k # not ok

k = (i += j) # not ok in Python; ok in C, C++, Java

(i += j) = k # not ok in Python; not ok in C and Java; ok in C++

# in Java
j = ++i; # pre-increment
j = i++; # post-increment

# Python does not have ++
# Containers are any object that holds an arbitrary number of other objects

"""
Questions
    How are list and deque implemented? list is frontloaded deque is middle loaded
    What are the costs of list and deque? 
    	list: insert front o(n), insert back o(1) amortized
    	deque: "      "  o(1) amortized, back o(1) amortized
    Of the containers list and deque, which can back a stack? Why or why not?
    	list as long as you use the back bc it will have more room at the back when
    	adding to the stack
    Of the containers list and deque, which can back a queue? Why or why not?
    	deque because as a first in first out, we push onto the front and pop off the back
    	so we do not want to push onto the front of a frontloaded datastructure
    What is a lambda?
    	lambda is a keyword used to define anon functions
    What is a higher-order function?
    	a function that takes in a function as a parameter
    What is an l-value, r-value?
    In terms of l-values and r-values, what does +  take and produce?
    In terms of l-values and r-values, what does ++ take and produce?
    Why doesn't Python have ++?
"""
