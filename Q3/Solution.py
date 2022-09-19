

def findmedian(num1, num2):
    num3 = num1 + num2
    num3 = sorted(num3)
    mid = len(num3)//2

    if(len(num3)%2!=0):
        return num3[mid]
    else:
        mid = float (num3[mid-1]) + float (num3[mid])
        return float (mid/2)

print(findmedian([1,3], [2]))