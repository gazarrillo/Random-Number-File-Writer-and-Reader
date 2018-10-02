#Importing Random Module
import random
#Intro and Input from User
print('This program writes random numbers to the random.txt file.')
nnum = input('How many numbers would you like to write: ')
#Opening the file
wfile = open('random.txt','w')
#Initializing variable
i = 0
#Writing to the file
while i != int(nnum):
    i += 1
    wfile.write(str(random.randint(1,500)) + '\n')
#Closing File
wfile.close()
#Output
print(str(i) + ' numbers were written to random.txt file')
