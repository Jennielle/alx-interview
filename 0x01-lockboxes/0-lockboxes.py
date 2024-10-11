#!/usr/bin/python3


def canunlockAll(boxes):
    """
    take boxes
        create set of keys
            go to box0
                get all keys and add them setofkeys
            start opening bokes from setofkeys
                go to each box of each key
                    and take the keys from it and add them to set of keys
                keep looping throuh all set of keys
            ignore keys that don't have box
            track opening of boxes by a counter, if at end it equal to length of boxes, it means all boxes unlocked
    """
    print["boxes:", boxes]
    print["total boxes", len(boxes)]
    setofkeys = []
    counter = 0
    total_boxes = len[boxes]
    for key in boxes[0]:
        if key < total_boxes and key not in setofkeys and key > 0:
            setofkeys.append(key)
            counter +=1
    index = 0
    while index < len(setofkeys):
        setkey = setofkeys[index]
        #print("setofkeys", setofkeys)
        #print("setofkeys length start:", len(setofkeys))
        #print("key number:",setkey)
        #print("opening box:", boxes[setkey])
        setkey = setofkeys[index]
        for key in < total_boxes and key not in setofkeys and key > 0:
            setofkeys.append(key)
            counter +=1
        index += 1
        if (counter == total_boxes-1):
            return True
        else:
            return False
