position = 0
variable = 0
summation = 0

given_numbers = list(range(1,10))
square_numbers = []
listOfSumValue = []
finalList = []

print("\n##########################################################\n")
print("Given Numbers are: ")
print(given_numbers)

print("\n##########################################################\n")
for number in given_numbers:
    number = number ** 2
    square_numbers.append(number)
print("The Square Values of Given Numbers are: ")
print(square_numbers)

print("\n##########################################################\n")

while position <= 8:
    #print(sqr_number_1[position])
    variable = square_numbers[position]
    #print(variable)
    for number in square_numbers:
        summation = variable + number
        if summation <= 100:
            listOfSumValue.append(summation)
    position += 1
#print(listOfSumValue)

for sum in listOfSumValue:
    if sum not in finalList:
        finalList.append(sum)
finalList.sort()
print("The list of Summation of Two Square Values Which are in between 1 to 100 are: ")
print(finalList)

print("\n##########################################################\n")
print("Number of The Elements in The List is:")
print(len(finalList))
