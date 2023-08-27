#!/usr/bin/python3

"""
Write a method that determines if all the boxes can be opened.
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes
"""


def canUnlockAll(boxes):
    """
    Write a method that determines if all the boxes can be opened.
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes
    """
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    for current_box in range(num_boxes):
        if unlocked_boxes[current_box]:
            for key in boxes[current_box]:
                if key < num_boxes and not unlocked_boxes[key]:
                    unlocked_boxes[key] = True

    return all(unlocked_boxes)
