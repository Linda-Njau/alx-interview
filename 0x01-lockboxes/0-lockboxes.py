#!/usr/bin/python3
"""canUnlockAll function"""

def canUnlockAll(boxes):
    keys = list(boxes[0])
    unlocked_boxes = [0]

    index = 0
    while index < len(keys):
        current_key = keys[index]
        if current_key not in unlocked_boxes:
            unlocked_boxes.append(current_key)
            keys.extend(boxes[current_key])
        index += 1

    return len(unlocked_boxes) == len(boxes)
