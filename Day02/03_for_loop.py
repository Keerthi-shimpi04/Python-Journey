#for_loop 

for i in range(1,6): #here 6 is not included 
    print(i)

# Three forms of range:
'''
1. range(stop)

for i in range(5):
 print(i)  #0 1 2 3 4


 2. range(start, stop):
    
 for i in range(1,6): #here 6 is not included 
    print(i)

3. range(start, stop, step):

 for i in range(2, 10, 2):  #step=2 means will skip one number or character
  print(i)

  

  #LOOPING THROUGH STRINGS:

  example:word="python"
  for character in word:
   print(character)
'''
word="python"
for character in word:
 print(character)