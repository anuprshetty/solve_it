class Set:
    def __init__(self):
        self._set = {}

    def __str__(self):
        if self._set:
            set_str = ", ".join(
                f'"{key}"' if isinstance(key, str) else str(key)
                for key in self._set.keys()
            )
            return "{" + set_str + "}"
        else:
            return "set()"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._set)

    def add(self, ele):
        self._set[ele] = None

    def remove(self, ele):
        del self._set[ele]

    def discard(self, ele):
        self._set.pop(ele, None)

    def clear(self):
        self._set.clear()

    def to_tuple(self):
        return tuple(self._set.keys())

    # time complexity: O(len(set1) + len(set2))
    def union(self, other_set):
        union_set = Set()
        for ele in self.to_tuple():
            union_set.add(ele)
        for ele in other_set.to_tuple():
            union_set.add(ele)

        return union_set

    # same as union method. But here self set is updated instead of creating new union_set.
    def update(self, other_set):
        for ele in other_set.to_tuple():
            self.add(ele)

    def __contains__(self, ele):
        return ele in self._set

    # time complexity: O(min(len(set1), len(set2)))
    def intersection(self, other_set):
        loop_set, check_set = (
            (self, other_set) if len(self) < len(other_set) else (other_set, self)
        )

        intersection_set = Set()
        for ele in loop_set.to_tuple():
            if ele in check_set:
                intersection_set.add(ele)

        return intersection_set

    def intersection_update(self, other_set):
        intersection_set = self.intersection(other_set)

        self.clear()
        for ele in intersection_set.to_tuple():
            self.add(ele)

    # time complexity: O(len(set1))
    def difference(self, other_set):
        difference_set = Set()

        for ele in self.to_tuple():
            if ele not in other_set:
                difference_set.add(ele)

        return difference_set

    def difference_update(self, other_set):
        difference_set = self.difference(other_set)

        self.clear()
        for ele in difference_set.to_tuple():
            self.add(ele)

    # time complexity: O(len(set1) + len(set2))
    def symmetric_difference(self, other_set):
        difference_set_1 = self.difference(other_set)
        difference_set_2 = other_set.difference(self)
        symmetric_difference_set = difference_set_1.union(difference_set_2)

        return symmetric_difference_set

    def symmetric_difference_update(self, other_set):
        symmetric_difference_set = self.symmetric_difference(other_set)

        self.clear()
        for ele in symmetric_difference_set.to_tuple():
            self.add(ele)

    # time complexity: O(min(len(set1), len(set2)))
    def isdisjoint(self, other_set):
        return False if self.intersection(other_set) else True

    # time complexity: O(len(set1))
    def issubset(self, other_set):
        for ele in self.to_tuple():
            if ele not in other_set:
                return False

        return True

    # time complexity: O(len(set2))
    def issuperset(self, other_set):
        return other_set.issubset(self)


_set = Set()
print(f"{_set = }")

elements = (2, 3, 6, 7, "anup")
for ele in elements:
    _set.add(ele)
print(f"{_set = }")
print(f"{len(_set) = }")

# _set.remove(4) # Key Error
_set.remove(6)
print(f"{_set = }")
_set.discard(4)
print(f"{_set = }")
_set.discard(3)
print(f"{_set = }")
_set.clear()
print(f"{_set = }")

set1_elements = (3, 4, 5, 6, 13, 14, 15)
set2_elements = (1, 2, 3, 4, 5, 7, 8, 9)

set1 = Set()
for ele in set1_elements:
    set1.add(ele)
set2 = Set()
for ele in set2_elements:
    set2.add(ele)

print("Set Union: ")
print(f"{set1 = }")
print(f"{set2 = }")
set3 = set1.union(
    set2
)  # In python built-in set, union operation syntax: set1.union(set2) OR set1 | set2
print(f"{set3 = }")
set3 = set2.union(set1)
print(f"{set3 = }")

print(f"{set1 = }")
print(f"{set2 = }")
set1.update(
    set2
)  # same as union method. But here self set is updated instead of creating new union_set.
print(f"{set1 = }")
print(f"{set2 = }")

set1_elements = (3, 4, 5, 6, 13, 14, 15)
set2_elements = (1, 2, 3, 4, 5, 7, 8, 9)

print("Set Intersection: ")
set1 = Set()
for ele in set1_elements:
    set1.add(ele)
set2 = Set()
for ele in set2_elements:
    set2.add(ele)

print(f"{set1 = }")
print(f"{set2 = }")
set3 = set1.intersection(
    set2
)  # In python built-in set, intersection operation syntax: set1.intersection(set2) OR set1 & set2
print(f"{set3 = }")
set3 = set2.intersection(set1)
print(f"{set3 = }")

print(f"{set1 = }")
print(f"{set2 = }")
set1.intersection_update(
    set2
)  # same as intersection method. But here self set is updated instead of creating new intersection_set.
print(f"{set1 = }")
print(f"{set2 = }")

set1_elements = (3, 4, 5, 6, 13, 14, 15)
set2_elements = (1, 2, 3, 4, 5, 7, 8, 9)

print("Set Difference: ")
set1 = Set()
for ele in set1_elements:
    set1.add(ele)
set2 = Set()
for ele in set2_elements:
    set2.add(ele)

print(f"{set1 = }")
print(f"{set2 = }")

set3 = set1.difference(
    set2
)  # In python built-in set, difference operation syntax: set1.difference(set2) OR set1 - set2
print(f"{set3 = }")
set3 = set2.difference(set1)
print(f"{set3 = }")

print("Set Symmetric Difference: ")

print(f"{set1 = }")
print(f"{set2 = }")

set3 = set1.symmetric_difference(
    set2
)  # In python built-in set, symmetric_difference operation syntax: set1.symmetric_difference(set2) OR set1 ^ set2 (XOR).
print(f"{set3 = }")
set3 = set2.symmetric_difference(set1)
print(f"{set3 = }")

print("Set isdisjoint: ")

print(f"{set1 = }")
print(f"{set2 = }")
set2.isdisjoint(set1)
print(f"{set2.isdisjoint(set1) = }")
print(f"{set1.isdisjoint(set2) = }")

print("Set issubset and issuperset: ")

print(f"{set1 = }")
print(f"{set2 = }")
set1.issubset(
    set2
)  # In python built-in set, issubset operation syntax: set1.issubset(set2) OR set1 <= set2.
set2.issuperset(
    set1
)  # # In python built-in set, issuperset operation syntax: set1.issuperset(set2) OR set1 >= set2.
print(f"{set1.issubset(set2) = }")
print(f"{set2.issuperset(set1) = }")
