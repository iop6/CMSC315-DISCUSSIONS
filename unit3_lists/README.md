# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

---

## How It Works

I wrote three small functions that work on a normal Python list.

- `insert_at` uses `insert` to put a value at a given index. Every element after that spot shifts one position to the right to make room.
- `delete_at` checks that the index is valid, then uses `pop` to remove the element and return it. The elements after it shift one position to the left. If the index is not valid it prints a message and returns `None`.
- `search_value` is a linear search. It starts at the front and checks each element one at a time until it finds a match and returns that index. If it reaches the end without a match it returns -1.

In `main()` I tested inserting and deleting at the beginning, middle and end of a list of numbers, and searched for a value that was in the list and one that was not.

## Edge Cases

- **Deleting with an invalid index:** `delete_at` printed that the index was not in the list and returned `None` instead of crashing.
- **Deleting from an empty list:** Same result, since index 0 does not exist in an empty list.
- **Inserting into an empty list:** The value became the only element in the list.

I chose to return `None` instead of raising an error so the program kept running and all the tests could finish.

## Real-World Example

I used a grocery list. I added milk to the end of the list, searched for eggs and removed them once I had them, then searched for bread to see where it was and for cheese to show what happens when an item is not on the list.

## Performance

Where you insert or delete matters. Adding or removing at the end is fast because nothing has to move. Adding or removing at the beginning is the slowest because every element in the list has to shift over, so the bigger the list the longer it takes. Searching is also slower on bigger lists since in the worst case it has to check every element.
