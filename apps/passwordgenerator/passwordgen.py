from random import randrange

def generate():
    l=randrange(20,30)
    password=''
    for i in range(l):
        a=randrange(33,126)
        password+=chr(a)
        a=0
    return password

def displaypass(pa):
    print(pa)

def main():
    res=generate()
    displaypass(res)

if __name__ == "__main__":
    main()