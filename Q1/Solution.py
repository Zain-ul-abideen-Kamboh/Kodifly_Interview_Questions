
def factorial(n):
    if(n==1 or n==0):
        return 1
    return (n*factorial(n-1))


def sumOfDigit(n):
    if(n==0):
        return 0
    return (n%10 + sumOfDigit(int (n/10)))

print("Enter the number : ")
num = input()
fact = factorial(int (num))
result = sumOfDigit(fact)

print(result)