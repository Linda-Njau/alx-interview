#!/usr/bin/python3
"""canUnlockAll function"""

def canUnlockAll(boxes):
    if not boxes:
        return False
    keys = set(boxes[0])
    unlocked_boxes = {0}
    num_boxes = len(boxes)

    while keys:
        new_keys = set()
        for key in keys:
            if key in unlocked_boxes or key >= num_boxes:
                continue
            unlocked_boxes.add(key)
            new_keys.update(boxes[key])
        keys = new_keys

    return len(unlocked_boxes) == len(boxes)

