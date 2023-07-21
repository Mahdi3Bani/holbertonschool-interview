#!/usr/bin/python3
'''comment'''

def rain(walls):
    """comment"""

    n = len(walls)
  
    
    res = 0
  
    for i in range(1, n - 1):
  
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
  
        right = walls[i]
  
        for j in range(i + 1, n):
            right = max(right, walls[j])
  
        res = res + (min(left, right) - walls[i])
  
    return res