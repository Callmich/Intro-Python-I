# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(numb):
    print (numb % 2 == 0)

is_even(0)
is_even(1)
is_even(2)


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def print_ev_od(num):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")

print_ev_od(num)
