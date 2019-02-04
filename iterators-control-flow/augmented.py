number = "9,852,741,456,112,321"
clean = ""

if not clean:
    print("clean is falsey")

for i in range(0, len(number)):
    if number[i] in "0123456789":
        clean += number[i]

newNum = int(clean)
print("the number is {}".format(newNum))