
# ██╗███████╗    ███████╗██╗     ███████╗███████╗
# ██║██╔════╝    ██╔════╝██║     ██╔════╝██╔════╝
# ██║█████╗█████╗█████╗  ██║     ███████╗█████╗  
# ██║██╔══╝╚════╝██╔══╝  ██║     ╚════██║██╔══╝  
# ██║██║         ███████╗███████╗███████║███████╗
# ╚═╝╚═╝         ╚══════╝╚══════╝╚══════╝╚══════╝

name = input("Please enter your name...")
age = int(input("How old are you, {}?".format(name)))
if age > 21:
    print("Ah, {0} years on you, eh? Let me buy you a drink, {1}."
        .format(age, name)
    )
else:
    print("Oh my, {0}, you aren't quite old enough for a drink. Come back in {1} years"
        .format(name, (21 - age))
    )
