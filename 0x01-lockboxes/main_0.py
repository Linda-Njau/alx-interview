#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

# Test case 1: All boxes can be opened
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected: True

# Test case 2: All boxes can be opened
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected: True

# Test case 3: Not all boxes can be opened
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected: False

# Test case 4: Single box with no keys
boxes = [[]]
print(canUnlockAll(boxes))  # Expected: True

# Test case 5: Single box with a key to itself
boxes = [[0]]
print(canUnlockAll(boxes))  # Expected: True

# Test case 6: Multiple boxes with keys pointing to the same box
boxes = [[1, 2], [0, 2], [1, 0]]
print(canUnlockAll(boxes))  # Expected: True

# Test case 7: No boxes
boxes = []
print(canUnlockAll(boxes))  # Expected: False

