Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

    O(1) because using append only overrides values instead of growing the list.

2. What is the space complexity of your ring buffer's `append` function?

    O(1) because capacity remains constant and using append only overrides values instead of growing the list.

3. What is the runtime complexity of your ring buffer's `get` method?

    O(n) because of the list comprehension.

4. What is the space complexity of your ring buffer's `get` method?

    O(n) because of the list comprehension.


5. What is the runtime complexity of the provided code in `names.py`? 

    O(n^2) because of we are nesting one loop inside another loop.

6. What is the space complexity of the provided code in `names.py`?

    O(n) because the list of duplicates will grow based on the values in the inputs since the list can have anywhere from 1 to n duplicates.


7. What is the runtime complexity of your optimized code in `names.py`?

    The initial approach has a runtime complexity of O(n log n) because we need to search for every element in names_2.

8. What is the space complexity of your optimized code in `names.py`?

    The initial approach has a space complexity of O(n^2) because not only will the duplicates list grow based on the values in the inputs but we also need to store all the values from names_1.
