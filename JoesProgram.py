###Initial task
###how about writing a program to solve this:
#
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
###

#oldMagicNumber = 10 # Joes number to test

magicNumber = 1000
multiples1 = 3
multiples2 = 5
listOfDivNums = []
total = 0

#Find natural numbers below magicNumber that are multiples of multiples1 or multiples2 and add to listOfDivNums
for num in range(1, magicNumber-1):
    if num % multiples1 == 0 or num % multiples2 == 0:
        listOfDivNums.append(num);

#Find total
for number in listOfDivNums:
    total = total + number;

#Print list of numbers
#print(listOfDivNums)

#Print total
print(total)
