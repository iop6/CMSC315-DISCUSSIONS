"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    # Elements after the index shift right, so inserting at the front is slower than at the end
    lst.insert(index, value)


def delete_at(lst, index):
    # Validate the index first to avoid an IndexError and keep the program running
    if index < 0 or index >= len(lst):
        print("Index", index, "is not in the list")
        return None
    # Remove the element and return it, elements after it shift left
    return lst.pop(index)


def search_value(lst, value):
    # Linear search, each element is checked in order until a match is found
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================

    print("\n=== INSERTION TESTS ===")

    # Start with a small list of numbers
    numbers = [10, 20, 30, 40]
    print("Original list:", numbers)

    # Insert at the beginning (index 0), every element has to shift right
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Insert in the middle (index 3), only the elements after it shift
    insert_at(numbers, 3, 25)
    print("After inserting 25 in the middle:", numbers)

    # Insert at the end, nothing has to shift
    insert_at(numbers, len(numbers), 50)
    print("After inserting 50 at the end:", numbers)

    # ===============================
    # DELETION TESTS
    # ===============================

    print("\n=== DELETION TESTS ===")
    print("Starting list:", numbers)

    # Delete from the beginning, the rest of the list shifts left
    removed = delete_at(numbers, 0)
    print("Removed", removed, "from the beginning:", numbers)

    # Delete from the middle
    middle = len(numbers) // 2
    removed = delete_at(numbers, middle)
    print("Removed", removed, "from the middle:", numbers)

    # Delete from the end, nothing has to shift
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed", removed, "from the end:", numbers)

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")
    print("Searching in:", numbers)

    # Search for a value that is in the list
    index = search_value(numbers, 20)
    print("Searching for 20: found at index", index)

    # Search for a value that is not in the list, should return -1
    index = search_value(numbers, 99)
    print("Searching for 99: returned", index, "(not found)")

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge case 1: delete using an index that does not exist
    print("Trying to delete index 10 from", numbers)
    removed = delete_at(numbers, 10)
    print("Returned:", removed)

    # Edge case 2: delete from an empty list
    empty = []
    print("Trying to delete from an empty list")
    removed = delete_at(empty, 0)
    print("Returned:", removed)

    # Edge case 3: insert into an empty list
    insert_at(empty, 0, 1)
    print("After inserting 1 into the empty list:", empty)

    # ===============================
    # REAL WORLD: GROCERY LIST
    # ===============================

    print("\n=== REAL WORLD: GROCERY LIST ===")

    groceries = ["eggs", "bread", "apples"]
    print("Grocery list:", groceries)

    # Remembered milk, add it to the end of the list
    insert_at(groceries, len(groceries), "milk")
    print("Added milk:", groceries)

    # Grabbed the eggs, so take them off the list
    index = search_value(groceries, "eggs")
    delete_at(groceries, index)
    print("Got the eggs:", groceries)

    # Check if bread is still on the list
    index = search_value(groceries, "bread")
    print("Bread is at position", index)

    # Check for something that was never on the list
    index = search_value(groceries, "cheese")
    print("Searching for cheese returned", index, "so it is not on the list")


if __name__ == "__main__":
    main()
