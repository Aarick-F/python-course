number = "9,258,476,102,001,365"
cleanedNumber = ""

for char in number:
    if char in "0123456789":
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is: {}".format(newNumber))