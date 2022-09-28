# Iterate over a list using Recursion
def Iterate(length=5):
    l = [0,1,2,3,4,5]
    if length < 0 :
        print("Over")
    else:
        print(l[length])
        Iterate(length - 1)

print(Iterate())