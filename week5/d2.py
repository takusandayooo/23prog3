class Input:
    def input():
        lists=[]
        while(1):
            x=int(input("Input? "))
            if(x<0):
                break
            else:
                lists.append(x)
        return lists
s = Input.input()
print("")
print(s)
