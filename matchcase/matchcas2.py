choice = input("presss y for enter press n for exit press o for open menu")

match choice:
    case "y" | "Y" | "yes":
        print("welcome")
    case "n" | "N":
        print("thanks")    
    case _:
        print("invalid choice")    