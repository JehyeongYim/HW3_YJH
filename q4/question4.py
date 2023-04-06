def fact(a):
    fac = 1
    if(a==0):
        fac = 1
    else:
        while(a>0):
            fac=fac*a
            a = a-1
    return fac

def main():
    print(fact(0))
    print(fact(2))
    print(fact(4))
    print(fact(6))
    print(fact(8))
    print(fact(10))
    print(fact(12))
    print(fact(14))
    return 0


if __name__=='__main__':
    main()

   
