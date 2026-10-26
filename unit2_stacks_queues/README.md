# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

---

## How to Run

```
python3 unit2_discussion.py
```

## How It Works

**Stack (LIFO - Last In, First Out)**

I built the stack to work like a pile of plates. Items were added to the top and taken from the top, so the last item added was the first one removed.

- I used a Python list, with the end of the list as the top of the stack.
- `push` added to the end with `append`.
- `pop` removed from the end with `pop()`.
- `peek` returned the last item (`items[-1]`) without removing it.

**Queue (FIFO - First In, First Out)**

I built the queue to work like a line at a store. Items joined at the back and left from the front, so the first item added was the first one removed.

- I used a `deque` instead of a list because removing from the front of a list is slow (everything has to shift over), while a deque removes from the front quickly.
- `enqueue` added to the back with `append`.
- `dequeue` removed from the front with `popleft()`.
- `front` returned the first item (`items[0]`) without removing it.

## Edge Cases

- **Removing from an empty stack/queue:** Instead of crashing, `pop` and `dequeue` printed a message saying the structure was empty and returned `None`.
- **Peeking at an empty stack/queue:** `peek` and `front` did the same thing, printed a message and returned `None`.
- **One item:** I added one item, removed it, and checked `is_empty()`. It returned `True`, so the structure went back to empty correctly.

I chose to return `None` instead of raising an error so the program kept running and all the demos could finish.

## Extra Test

I added the same numbers (1, 2, 3) to a stack and a queue, then mixed adding and removing. The stack always removed the newest item and the queue always removed the oldest, so the same inputs gave different outputs.

## Real-World Uses

- **Stack - Undo button:** I made a small text editor history where undo removed the most recent change first. That was LIFO, so I used a stack.
- **Queue - Printer:** I made a printer queue where three jobs printed in the order they were sent. That was FIFO, so I used a queue.

## Memory Usage

Both structures used O(n) space, meaning memory grew as more items were added. Every push or enqueue stored one more item, and every pop or dequeue freed one. Neither structure had a set size limit, so they kept growing as long as items were added.
