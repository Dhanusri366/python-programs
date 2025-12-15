yesOrNo = "yes"
dict ={}
while yesOrNo == "yes":
    print("\n"*100)
    name = input("enter your name:")
    bid = int(input("enter your bid:"))
    dict[name]=bid
    yesOrNo = input("want other to bid")
print(max(dict.items(),key = lambda x:x[1]))