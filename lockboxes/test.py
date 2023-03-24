#!/usr/bin/python3
"""checking if the box can be opened or not"""

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
n = len(boxes)
unlocked = [False] * n  # keep track of unlocked boxes
unlocked[0] = True     # first box is already unlocked
queue = [0]            # start with the first box
while queue:
        box = queue.pop(0)
        print ("box:",box)
        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
                print ("queue:", queue)
print(unlocked)
