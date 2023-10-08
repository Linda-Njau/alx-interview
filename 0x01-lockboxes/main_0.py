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

# Test case 8: Boxes with keys pointing to non-existent boxes
boxes = [[1], [2], [3], [5]]
print(canUnlockAll(boxes))  # Expected: False

# Test case 9: Circular dependency between boxes
boxes = [[1], [2], [0]]
print(canUnlockAll(boxes))  # Expected: True

# Test case 10: Multiple disconnected sets of boxes
boxes = [[1, 2], [3, 4], [5], [6], [7], [], [8], [], [9]]
print(canUnlockAll(boxes))  # Expected: False

# Test case 11: Large number of boxes
boxes = [[i+1] for i in range(10**6)]
boxes.append([])
print(canUnlockAll(boxes))  # Expected: True

# Test case 12: All boxes locked except the first box
boxes = [[] for _ in range(10**6)]
boxes[0] = [1]
print(canUnlockAll(boxes))  # Expected: False

