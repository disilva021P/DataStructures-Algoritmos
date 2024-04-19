def RussianDoll(doll):
    if doll==1:
        return "all the dolls are open"
    else:
        print(doll)
        return RussianDoll(doll-1)

print(RussianDoll(10))