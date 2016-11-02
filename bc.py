# Get a number from the user to convert
num = input('What is the decimal number to convert? ')

# Test that we can convert to an integer
try:
  d = int(num)
except:
  print('Please enter a decimal number')

# empty string to store binary number
b = ''

#while loop keeps dividing until number is 0
while d > 0:
  r = d % 2 # Gets the remainder
  b = b + str(r) # Adds the remainder to the empty string
  d = int(d/2) # Gets how many times the number can be divided by two (but not the remainder)
  
# reverse b so it reads correct
b = b[::-1]

#print the answer
print(str(num) + ' in binary is ' + str(b))

