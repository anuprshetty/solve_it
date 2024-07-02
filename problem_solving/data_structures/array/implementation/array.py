class Array:
    # Size vs Capacity:
    # - Size: the number of elements currently stored in the array.
    # - Capacity: the total number of elements the array can hold without resizing.

    # 2 types of array:
    # - Static array: Fixed size array where size doesn't change dynamically.
    # - Dynamic array: Variable size array where size grows or shrinks dynamically.

    # Amortized Analysis:
    # - Amortized analysis is used for algorithms where an occasional operation is very slow, but most of the other operations are faster. In Amortized Analysis, we analyze a sequence of operations and guarantee a worst-case average time that is lower than the worst-case time of a particularly expensive operation.
    def __init__(self):
        self._array = []  # Python List is a dynamic array.

    @property
    def array(self):
        return self._array

    def size(self):
        # complexity:
        # - time --> O(n)
        # - space --> O(1)
        return len(self._array)

    def insert(self, index, value):
        # Fixed size array:
        # complexity:
        # - time --> [best - O(1) (insert at the end of array), worst - O(n)(insert at the start of array), average - O(n)]
        # - space --> O(1)

        # Variable size array: Capacity will be doubled when array is full.
        # complexity:
        # - time --> [best - O(1) (insert at the end of array and array is not full), worst - O(n)(insert at the start of array and array is full), average - O(n)]
        # - space --> [best - O(1) (insert at the end of array and array is not full), worst - O(n)(insert at the start of array and array is full), average - O(1)]
        self._array.insert(index, value)

    def append(self, value):
        # Fixed size array:
        # complexity:
        # - time --> O(1)
        # - space --> O(1)

        # Variable size array: Capacity will be doubled when array is full.
        # complexity:
        # - time --> [best - O(1) (insert at the end of array and array is not full), worst - O(n)(insert at the end of array and array is full), average - O(1)]
        # - space --> [best - O(1) (insert at the end of array and array is not full), worst - O(n)(insert at the end of array and array is full), average - O(1)]
        self._array.append(value)

    def delete(self, value):
        # complexity:
        # - time --> O(n)
        # - space --> O(1)
        self._array.remove(value)  # Removes first occurrence of value in the array.

    def pop(self, index):
        # Fixed size array:
        # complexity:
        # - time --> [best - O(1) (remove at the end of array), worst - O(n)(remove at the start of array), average - O(n)]
        # - space --> O(1)

        # Variable size array: Capacity will be halved when array size is 1/4th of capacity.
        # complexity:
        # - time --> [best - O(1) (remove at the end of array and array size is not 1/4th of capacity), worst - O(n)(remove at the start of array and array size is 1/4th of capacity), average - O(n)]
        # - space --> [best - O(1) (iremove at the end of array and array size is not 1/4th of capacity), worst - O(n)(remove at the start of array and array size is 1/4th of capacity), average - O(1)]

        return self._array.pop(index)  # pop returns the deleted element.

    def fetch(self, index):
        # Accessing an element in the array at the given index.
        # complexity:
        # - time --> O(1)
        # - space --> O(1)
        return self._array[index]

    def update(self, index, value):
        # complexity:
        # - time --> O(1)
        # - space --> O(1)
        self._array[index] = value


array = Array()
array.insert(array.size(), 10)
array.insert(array.size(), 20)
array.append(30)
array.append(40)
array.insert(0, 5)
array.insert(3, 25)
array.insert(
    100, 1000
)  # if index >= size, then element will be inserted at position size.
print(array.array)
array.delete(20)
print(array.array)
print(array.pop(3))
print(array.array)
print(array.fetch(3))
array.update(3, 300)
print(array.fetch(3))
print(array.array)
