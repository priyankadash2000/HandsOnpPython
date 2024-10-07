x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")


# This function outputs an addition table. It is written to end after
# printing 5 lines of the addition table, but it will break out of the
# loop if the "my_sum" variable exceeds 20.

# The function accepts a "given_number" variable through its
# parameters.
def addition_table(given_number):

	# The "iterated_number" and "my_sum" variables are initialized with
	# the value of 1. Although the "my_sum" variable does not need any
	# specific initial value, it still must be assigned a data type
	# before being used in the while loop. By initializing "my_sum"
	# with any integer, the data type will be set to int.
	iterated_number = 1
	my_sum = 1

	# The while loop will run while it is True that the
	# "iterated_number" is less than or equal to 5.
	while iterated_number <= 5:

		# The "my_sum" variable is assigned the value of the
		# "given_number" plus the "iterated_number" variables.
		my_sum = given_number + iterated_number

		# Test to see if the "my_sum" variable is greater than 20.
		if my_sum > 20:
			# If True, then use the break keyword to exit the loop.
			break

		# If False, the Python interpreter will move to the next line
		# in the while loop after the if-statement has ended.

		# The print function will output the "given_number" plus
		# the "iterated_number" equals "my_sum".
		print(str(given_number), "+", str(iterated_number), "=", str(my_sum))

		# Increment the "iterated_number" before the while loop starts
		# over again to print a new "my_sum" value.
		iterated_number += 1


addition_table(5)
addition_table(17)
addition_table(30)

# Expected output:
# 5 + 1 = 6
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 5 + 5 = 10
# 17 + 1 = 18
# 17 + 2 = 19
# 17 + 3 = 20
# None

for outer_loop in range(2, 6+1):
    for inner_loop in range(outer_loop):
        if inner_loop % 2 == 0:
            print("printing "+str(inner_loop))
            

for sum in range(5):
    sum += sum
    print(str(sum)+"Printing...")
    
string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”
print(string1[0::2]) # Prints “Getns atlns”
print(string1[::-1])
print(string1[-10:])
print(string1[55:])

print(string1[0::2])# Prints “Getns atlns”
print(string1[::-1])# Prints “sgnilhtraE ,sgniteerG”
greetings = ["Hello", "world"]
print(" ".join(greetings)) # Prints "Hello world"
#You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!")# Prints "Hello, Alice!"

for n in range(6,18+1,3):
  print(n*2)
  
def format_phone(phonenum):
	area_code = "(" + phonenum[:3] + ")"
	exchange = phonenum[3:6]
	line = phonenum[-4:]
	return area_code + " " + exchange + "-" + line

print(format_phone("2025551212")) # Outputs: (202) 555-1212


for n in range(19):
    if n % 2 == 0:
        print(n)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&") 

for n in range(0,18+1,2):
     print(n*2)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&") 
for n in range(18+1):
	 print(n**2)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&") 
for n in range(10):
  print(n+n)
print([c for c in "input" if c.lower() in ['a', 'e', 'i', 'o', 'u']])