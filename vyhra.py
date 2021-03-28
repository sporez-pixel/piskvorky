# class winchecker:
#     # def __init__(self, list, x, y, hrac):
#     #     self.list = list
#     #     self.x = x
#     #     self.y = y
#     #     self.hrac = hrac

def vyhra(list, x, y, hrac):
    if (hrac==1):
        hrac = 2
    else:
        hrac = 1
    d1 = diagonala1(list, x, y, hrac)
    d2 = diagonala2(list, x, y, hrac)
    r = radek(list, x, y, hrac)
    s = sloupec(list, x, y, hrac)

    if (d1):
        return True
    elif (d2):
        return True
    elif (r):
        return True
    elif (s):
        return True
    else:
        return False

def diagonala1(list, x, y, hrac):
    count = 0
    for i in range(1,5):
        if (x+i < 14 and y+i < 14):
            if (hrac==list[y+i][x+i]):
                count += 1
            else:
                break
    for i in range(1,5):
        if (x-i >= 0 and y-1 >= 0):
            if (hrac==list[y-i][x-i]):
                count += 1
            else:
                break
    if (count >= 4):
        return True
    return False    

def diagonala2(list, x, y, hrac):
    return False

def radek(list, x, y, hrac):
    count = 0
    for i in range(1,5):
        if (x+1 <= 14):
            if (hrac==list[y][x+i]):
                count += 1
            else:
                break
    for i in range(1,5):
        if (x-i >= 0):
            if (hrac==list[y][x-i]):
                count += 1
            else:
                break
    if (count >= 4):
        return True
    return False

def sloupec(list, x, y, hrac):
    return False
        