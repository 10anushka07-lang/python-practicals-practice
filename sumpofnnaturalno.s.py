n=int(input("enter the no.of elements till you want the sum to be calculated"))
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
print(sum(n))