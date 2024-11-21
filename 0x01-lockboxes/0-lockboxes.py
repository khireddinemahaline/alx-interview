#!/usr/bin/python3
"""open n box in same time
    we need to use linked list for our problem 

    box [ key_sec_box ]
    0 = [3, 2 , 4]
    1 = [2,4,1]
    2 = [4,6]

    [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]


    
"""


def canUnlockAll(boxes):
    """of listes [[],[],[]] """
    visited = set()  # To keep track of visited nodes
    open_box = []
    i = 0

    
    while i < len(boxes):
        open_box.append(boxes[i])
        for ele in open_box[i]:
            if ele in 
        





    



