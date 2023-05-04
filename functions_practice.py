
def hello():
    print("Hello, welcome to Wolfe's first python file!")

def pack(wolves, condiments, gum):
    return("wolves", "condiments", "gum")

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")


hello()
print(pack("wolves", "condments", "gum"))
eat_lunch([])
eat_lunch(["sushi"])
eat_lunch(["pineapple", "sushi", "chocolate"])
