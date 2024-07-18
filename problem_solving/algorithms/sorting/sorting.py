# Factors while choosing a sorting algorithm:
# - Size of data: Data can be large (size > 30) or small(size ~ 30)
# - Randomness of data: is data completely random, partially sorted or almost sorted?
# - Time and Space complexity:
# - Stability: will it retain the relative order of equal elements in the data (stable or non-stable)? Stability is important and significant only when the objects have multiple fields. Ex: Person(name, age)

# Sorting Algorithms:

# Normal Sorting Algorithms:
# 1. Bubble Sort:
# - Size of data: Suitable for small data
# - Randomness of data: Suitable when data is almost sorted.
# - Time and Space complexity:
# -- Time[Worst - O(n^2), Avg - , Best - O(n)]
# -- Space[]
# - Stability: True
# Advantages:
# -

# 2. Insertion Sort:
# - Size of data: Suitable for small data
# - Randomness of data: Suitable when data is almost sorted.
# - Time and Space complexity:
# -- Time[Worst - O(n^2), Avg - , Best - O(n)]
# -- Space[]
# - Stability: True
# Advantages:
# -

# 3. Selection Sort:
# - Size of data: Suitable for small data
# - Randomness of data: Suitable when data is almost sorted.
# - Time and Space complexity:
# -- Time[Worst - O(n^2), Avg - , Best - O(n^2)]
# -- Space[]
# - Stability: False
# Advantages:
# - It retains first k smallest/largest elements in its first k iterations/passes. So we can use this property when we have to paginate our sorted data.

# Optimized Sorting Algorithms:
# 4. Merge Sort: Divide and Conquer Algorithm (Divide + Conquer + Combine)
# - Size of data: Suitable for large data
# - Randomness of data:
# - Time and Space complexity:
# -- Time[Worst - O(nlogn), Avg - O(nlogn), Best - O(nlogn)]
# -- Space[Worst - O(n), Avg - O(n), Best - O(n)]
# - Stability: True
# Advantages:
# - Well-suited for linked lists because it works with a space complexity of O(1).
# - Well-suited for external sorting (bring in parts of array and then sort these parts).

# 5. Quick Sort: Divide and Conquer Algorithm
# - Size of data: Suitable for large data and case where it never leads to worst case scenario.
# - Randomness of data:
# - Time and Space complexity:
# -- Time[Worst - O(n^2), Avg - O(nlogn), Best - O(nlogn)]
# -- Space[Worst - O(n), Avg - O(n), Best - O(n)]
# - Stability: False
# Advantages:
# - It is well-suited for arrays.

# 6. Heap Sort: Binary Tree data structure
# - Size of data:
# - Randomness of data:
# - Time and Space complexity:
# -- Time[Worst - O(nlogn), Avg - O(nlogn), Best - O(nlogn)]
# -- Space[Worst - O(1), Avg - O(1), Best - O(1)]
# - Stability: False
# Advantages:
# -

# Miscellaneous Sorting Algorithms:
# - Counting Sort
# - Radix/Bucket Sort
# - Shell Sort

# Extra Info:
# C++ --> Uses Randomized Quick Sort
# Python --> Uses Tim Sort (Timsort is a hybrid stable sorting algorithm) = Merge Sort + Insertion Sort


# todo:
# In my experience, from most to least commonly mentioned in interviews:
# 1. quicksort: implement it, explain it
# 2. mergesort: implement it, talk about space complexity as well as time complexity
# 3. insertion sort: explain when it can be better than the above two
# 4. heapsort: explain how it works, and how heaps work in general
# 5. bubble sort: why it's awful
# 6. radix/counting/bucket sort: when it's useful
# 7. selection sort: usually thrown in as an example when asked to list sorting algorithms you know

# Pretty much everything else is trivia.
# I also like to throw in Python's "Tim Sort" in these conversations.

# It's getting increasingly less common, in my experience, to need to know how to implement any sorting algos in the context of an interview -- and if you do need to implement one within an interview, just knowing one (quicksort is a good default, with few edge cases) usually suffices. However, knowing their asymptotic runtimes and what each is good for (is it stable / unstable? good for very large data sets like mergesort, or best for in-memory usage like quicksort?) is pretty useful.

# More important, though, is just having a solid toolbox that you can pull from for solving a wide variety of problems. Most of the time you can get by with one really solid sorting algorithm (quicksort makes sense, since it's intuitively similar to binary search, which is an algo you need to know), so long as you know the ins and outs of other data structures and algorithms. If you know how to use a heap, you don't need to memorize heapsort explicitly -- you already have a basic version at your disposal (just stick all your values in a heap and them pull them off until the heap is empty). If you can effectively use a binary search tree, you can use it to sort and search any data set that fits in memory. And if you need unordered key/value semantics, HashMap is more efficient than any sorted structure. Concentrating less on mastering all possible sorts and making sure your toolbox is well-rounded will help you much more in interviews than being an expert in sorting.

# There is only one: sort function from your standard library. You should be able to call it. And you should know difference between stable and unstable sort.

# It’s important to have a good understanding of these algorithms, their time and space complexity, and when to use them.

# Introsort or introspective sort:
# - Introsort, also known as introspective sort, is a hybrid sorting algorithm that uses a combination of quicksort, heapsort, and insertion sort to sort an array from low to high or high to low.
# - Introsort is considered one of the fastest comparison sorting algorithms in use today. It's used in the STL library in C++ and for array sorting in the Swift programming language.
# - Recursion depth: The maximum recursion depth depends on the number of elements in the collection and is usually 2 * log(n).
# - Not stable: Introsort is not stable.
# - Introsort or introspective sort is a hybrid sorting algorithm that provides both fast average performance and (asymptotically) optimal worst-case performance. It begins with quicksort, it switches to heapsort when the recursion depth exceeds a level based on (the logarithm of) the number of elements being sorted and it switches to insertion sort when the number of elements is below some threshold. This combines the good parts of the three algorithms, with practical performance comparable to quicksort on typical data sets and worst-case O(n log n) runtime due to the heap sort. Since the three algorithms it uses are comparison sorts, it is also a comparison sort.

# Quick Sort:
# - The key part is partitioning [Hoare (non-stable), Lomuto (non-stable), Naive (stable but auxiliary space)].
# - tail recursive, cache friendly.
# - In quicksort the auxiliary space required is O(1) whereas it is O(n) in merge sort where we need extra array for merging.

# Is quicksort in-place algorithm? (opposite word is out-of-place algorithm)
# - There are 2 definitions of in-place algorithm.
# - 1. An algorithm is said to be in-place if it does not uses any extra space or auxiliary space (space complexity - O(1)).
# -- By this definition, quicksort is NOT in-place algorithm as it requires extra space for recursion call stack.
# - 2. An algorithm is said in-place if it does not copy input element to any other location.
# -- By this definition, quicksort is in-place.
# - Auxiliary space required:
# -- O(log n) --> best case (recursion call stack)
# -- O(n) --> worst case (recursion call stacks)

# Cycle Sort:
# - O(n^2) worst case algorithm.
# - Minimum memory writes and can be used for cases where memory writes are costly.
# - Ex: minimum swaps needed to sort an array.
# In-place and non-stable algorithm.

# Counting Sort:
# - It is used when we know that the input array has elements upto range 0-k (zero to k).
# - Not a comparison based algorithm.
# - O(n+k) time, O(n+k) space.
# - stable
# - used as a subroutine in radix sort.
# - only useful when k is really small.

# Radix Sort:
# - Radix sort supports linear time even for larger range.
# - Counting sort used as a subroutine.
# - O(n*(n+b)) time, O(n+b) space.

# Bucket Sort:
# - Situation where numbers are uniformly distributed in range from 1 to 10^8.
# - Similar is the case with floating-point numbers. Range is 0.0 to 1.0.

# Shell Sort:
# - Variation of insertion sort, we initialize gap as n/2 and then decrease it to 1.
# - Use to bring smaller elements to left with less number of comparisons.
