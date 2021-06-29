def isValidChessBoard(dict1):
    dict2={}
    dict2.setdefault('bqueen',1)
    dict2.setdefault('bking',1)
    dict2.setdefault('bbishop',2)
    dict2.setdefault('bknight',2)
    dict2.setdefault('bpawn',8)
    dict2.setdefault('brook',2)
    dict2.setdefault('wqueen',2)
    dict2.setdefault('wking',2)
    dict2.setdefault('wbishop',2)
    dict2.setdefault('wknight',2)
    dict2.setdefault('wpawn',8)
    dict2.setdefault('wrook',2)
    for key in dict1.keys():
        if int(key[0])>8 or int(key[0])<1:
            return False
        if key[1] not in "abcdefgh":
            return False 
    for value in dict1.values():
        if value[0] not in "bw":
            return False
        if value in dict2.keys():
            dict2[value]-=1
    for val in dict2.values():
        if val<0:
            return False
    return True


if __name__=='__main__':
    dictionary={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
    print(isValidChessBoard(dictionary))