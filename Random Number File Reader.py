#Importing Module
import sys
#Intro
print('The following numbers were read from the random.txt file:')
#Initializing Variables
i = 0
sum_total = 0
#Opening File
rfile = open('random.txt', 'r')
#Reading File
for linefromfile in rfile:
#Printing Each Number
    sys.stdout.write(linefromfile)
    num = int(linefromfile)
#Summing all Numbers
    sum_total += num
#Calculating the number of numbers
    i += 1
#Outputting Results
print('The total of the numbers is: ' + str(sum_total))
print('The file contained ' + str(i) + ' numbers')
#Closing File
rfile.close()
