#!/usr/bin/python3
"""canUnlockAll function"""

def canUnlockAll(boxes):
    if not boxes: 
        return False
    keys = set()
    unlocked_boxes = set()
    
    keys.update(boxes[0])
    unlocked_boxes.add(0)
        
    while keys:
        new_keys =set()
        for key in keys.copy():
            unlocked_boxes.add(key)
            new_keys.update(boxes[key])
            keys = new_keys - unlocked_boxes
        print(f'unlocked boxes:{unlocked_boxes}')
        print(f'keys:{keys}')
        
    return len(unlocked_boxes) ==  len(boxes)
    

