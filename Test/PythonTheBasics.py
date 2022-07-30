print("Hello World..!")

# VARIABLES (case sensisitve, letters (a-z), underscore, numbers (0-9)

x = 5
y = "Automation"
print(x)
print(y)

print("Hello " + y)

x = 10
y = 20
print(x + y)

# SYNTAX

if 10 > 5:
    print("10 is greater than 5")

# FUNCTION

def sum(a,b):
    print(a+b)

x = sum(20,30)

# COMMAND LINE RUNNING
# Copy test path > go to CMD > CD (paste test path) remove the test name > hit enter and type "python testname.py > Enter

# NUMBER
x = 5
y = 2.5
z = 5j

print(type(x))
print(type(y))
print(type(z))

# CASTING
x = int(2) #2
y = int(2.5) #2
z = float(1) #1.0
p = str(10) #"10"

print(x)
print(y)
print(z)
print(p)

# STRING

x = "Hello,World..!"
#print(x.strip()) #stripping all spaces in variable
# print(x[6:11])
#print(x.lower())
#print(x.upper())
#print(x.replace("Hello","Hi"))
print(x.split(","))

# INPUTS
print("Enter your name : ")
x = input()
print("Hello,"+x)