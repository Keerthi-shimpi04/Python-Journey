

'''
Random module is a in-built module which we can generate the random numbers...
import random

methods():
randint(a,b) here both a and b are included
randrange(a,b) but here b is excluded
random() it usually returns the floating value btw 0.0 to 1.
uniform()
choice()
shuffle()
'''

import random
list=[10,20,30,-4,-5]

random_number=random.randint(0,5)
print(random_number)

#random.shuffle(list)
#print(list)    #[-4, 20, 10, 30, -5]

a=random.uniform(1,3) #It always gives me the floating points btw the range...
print(a)


choice_1=random.choice(list)
print(choice_1)






