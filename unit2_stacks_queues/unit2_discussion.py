"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        # using a list, the end of the list is the top of the stack
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # new items go on the end (the top), so the last one in
        # will be the first one out (LIFO)
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # if the stack is empty there is nothing to remove,
        # so print a message and return None instead of crashing
        if self.is_empty():
            print("Stack is empty, nothing to pop")
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # peek just looks at the top item, it doesn't remove it
        if self.is_empty():
            print("Stack is empty, nothing to peek at")
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        # using a deque because removing from the front is fast
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # new items go to the back of the line, so the first one in
        # will be the first one out (FIFO)
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # same idea as the stack, if it's empty print a message and return None
        if self.is_empty():
            print("Queue is empty, nothing to dequeue")
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # front returns whoever is first in line without removing them
        if self.is_empty():
            print("Queue is empty, no front item")
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("--- UNIT 2: STACKS AND QUEUES ---")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n--- STACK DEMO ---")
    s = Stack()

    # push 4 items
    for item in ["A", "B", "C", "D"]:
        print("Pushing", item)
        s.push(item)

    print("Top of the stack is:", s.peek())

    # pop everything, should come out backwards (LIFO)
    print("\nPopping everything off:")
    while not s.is_empty():
        print("Popped", s.pop())
    print("Last one in (D) came out first, so that's LIFO")

    # edge case: pop and peek on an empty stack
    print("\nTrying to pop from an empty stack:")
    print("Result:", s.pop())
    print("Trying to peek at an empty stack:")
    print("Result:", s.peek())

    # edge case: one item in, one item out
    print("\nPushing one item (X) then popping it")
    s.push("X")
    print("Popped", s.pop())
    print("Is the stack empty now?", s.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n--- QUEUE DEMO ---")
    q = Queue()

    # enqueue 4 items
    for item in ["A", "B", "C", "D"]:
        print("Enqueuing", item)
        q.enqueue(item)

    print("Front of the queue is:", q.front())

    # dequeue everything, should come out in the same order (FIFO)
    print("\nDequeuing everything:")
    while not q.is_empty():
        print("Dequeued", q.dequeue())
    print("First one in (A) came out first, so that's FIFO")

    # edge case: dequeue and front on an empty queue
    print("\nTrying to dequeue from an empty queue:")
    print("Result:", q.dequeue())
    print("Trying to look at the front of an empty queue:")
    print("Result:", q.front())

    # edge case: one item in, one item out
    print("\nEnqueuing one item (X) then dequeuing it")
    q.enqueue("X")
    print("Dequeued", q.dequeue())
    print("Is the queue empty now?", q.is_empty())

    # ---------- EXTRA TEST: MIXING ADDS AND REMOVES ----------
    # instead of adding everything then removing everything,
    # mix them together and see what comes out
    print("\n--- EXTRA TEST: MIXED ADD AND REMOVE ---")
    s = Stack()
    q = Queue()
    for item in [1, 2, 3]:
        s.push(item)
        q.enqueue(item)
    print("Added 1, 2, 3 to both")
    print("Stack removes:", s.pop(), "  Queue removes:", q.dequeue())
    s.push(4)
    q.enqueue(4)
    print("Added 4 to both")
    print("Stack removes:", s.pop(), "  Queue removes:", q.dequeue())
    print("Stack removes:", s.pop(), "  Queue removes:", q.dequeue())
    print("Same inputs, different outputs because stack takes the newest and queue takes the oldest")

    # ---------- REAL WORLD: UNDO BUTTON (STACK) ----------
    # an undo button undoes the most recent thing you did first, so it's a stack
    print("\n--- REAL WORLD: UNDO IN A TEXT EDITOR (STACK) ---")
    history = Stack()
    for action in ["typed 'Hello'", "typed ' World'", "made text bold"]:
        print("You", action)
        history.push(action)
    print("Pressing undo twice...")
    print("Undo:", history.pop())
    print("Undo:", history.pop())
    print("Next thing undo would remove:", history.peek())

    # ---------- REAL WORLD: PRINTER QUEUE (QUEUE) ----------
    # a printer prints jobs in the order they were sent, so it's a queue
    print("\n--- REAL WORLD: PRINTER QUEUE (QUEUE) ---")
    printer = Queue()
    for job in ["essay.docx", "resume.pdf", "photo.png"]:
        print("Sent to printer:", job)
        printer.enqueue(job)
    while not printer.is_empty():
        print("Printing:", printer.dequeue())
    print("All jobs printed in the order they were sent")


if __name__ == "__main__":
    main()
