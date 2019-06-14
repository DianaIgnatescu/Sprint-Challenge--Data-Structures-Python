import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []

# Attempting a second approach using the built-in set datatype.
# Construct new set from the given list and use the intersection method.
# Return a new set of elements that only contains elements common to all sets.
# This approach runs in 0.0056 seconds.

duplicates = set(names_1).intersection(names_2)

# STRETCH - this approach runs in 1.773 seconds so it's much slower than both of the solutions attempted.
# duplicates = [name for name in names_1 if name in names_2]


# Initial approach runs in 0.259 seconds
# bst = BinarySearchTree(names_1[0])
# for name in names_2:
#     bst.insert(name)
#
# for name in names_1:
#     if bst.contains(name):
#         duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# Original implementation runs in 8.572246 seconds on my machine
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
