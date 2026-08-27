#BREAK STATEMENT:Sometimes you want to stop a loop immediately.

for i in range(1, 11):

    if i == 5:
        break

    print(i) # 1,2,3,4



#CONTINUE:Skip the current iteration and continue with the next one

for i in range(1, 6):

    if i == 3:
        continue

    print(i) #1,2,4,5

#break    → STOP the loop
#continue → SKIP this iteration