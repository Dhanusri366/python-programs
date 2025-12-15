def calci(n1,op,n2 ):
    if op == '+':
        res = n1 + n2
    elif op == '-':
        res = n1-n2
    elif op == '*':
        res = n1*n2
    elif op == '/':
        res = n1/n2
    else:
        print("invalid")
    print(res)
    return res
n1 = int(input("enter n1"))
op = input("enter operation")
n2 = int(input("enter a n2"))
res = calci(n1,op,n2)

yesOrNo =input("do you want to continue y or n")
if(yesOrNo == 'y'):
    op = input("enter operation")
    n2 = int(input("enter a n2"))
    res = calci(res,op,n2)
    print(res)
