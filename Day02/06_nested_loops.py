#A loop inside another loop.
'''
n = int(input("Enter the size: "))

for i in range(n):

    for j in range(n):
        print("*", end=" ")

    print()
    '''
n = int(input("Enter the size: "))

for i in range(n):

    for j in range(n):
        print("*",end="")

    print()