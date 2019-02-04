shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        print("Do not buy {}".format(item))
        continue
    print("Buy {}".format(item))

meal = ["egg", "bacon", "spam", "sausages"]
nasty = None
for item in meal:
    if item == "spam":
        nasty = item
        break

if nasty:
    print("Ew spam no thank you ma'am")