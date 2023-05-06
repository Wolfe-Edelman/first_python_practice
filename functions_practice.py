
#Python Function Fun: Part 1
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


#Python Function Fun: Part 2

#arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for w in args:
        print(w)

#inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
def inner_function(8, 11):
    def inner_1():
        return 8+11
    def inner_2():
        return 8-11
    print(inner_1()+inner_2())

#lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(student_name, lunch_preference="Mystery Meat"):
    print(student_name, lunch_preference)

#sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(w, e):
    return w+e, w*e

#alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args

#arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*args):
    total = 0
    for a in args:
        total +=a
    print(a/len(args))

#arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*args):
    long = 0
    longest = ""
    for a in args:
        if len(a) > long:
            long = len(a)
            longest = a
    return longest


#Python Function Fun: Part 3

#name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.
def name_args(**kwargs):
    for k in kwargs.keys():
        print(f"{k}:{kwargs[k]}")
#Trial
name_args(name="Wolfe", weather="cloudy", location="beach", time="8")

#all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
def all_true(iter):
    return all(iter)
print(all_true[true, true, true])
print (all_true[true, false])

#one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.
def one_true(iter):
    return any(iter)
print(one_true[true, true, true])
print(one_true[false, false, false])
print(one_true[true, false])

#recursive_factorial - Uses recursion to find the factorial of an integer.
def recursive_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
#Trial
print(recursive_factorial(8))
print(recursive_factorial(11))

#recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
    #Input: AABBCCDD
    #Output: ABCD

def recursive_duplicate(str, i=0):
    if len(str <= 1) or i == len(str)-1:
        return str
    else:
        if str[i] == str[i+1]:
            return recursive_duplicate(str[0:i]+str[i+1:],i)
        else:
            return recursive_duplicate(str, i+1)
#Trial
print(recursive_duplicate("awawawa"))
print(recursive_duplicate("banana"))
print(recursive_duplicate("volleyball"))
print(recursive_duplicate("rose"))

#recursive_reverse - Uses recursion to reverse a string.
def recursive_reverse(str, i=0):
    if len(str) == 0:
        return ""
    elif:
        return str[-1-i] + recursive_reverse(str, i+1)
#Trial
print(recursive_reverse("awawawa"))
print(recursive_reverse("banana"))
print(recursive_reverse("volleyball"))
print(recursive_reverse("rose"))
