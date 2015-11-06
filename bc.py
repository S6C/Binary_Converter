# Get a number from the user to convert
num = input('What is the decimal number to convert? ')
try:
  d = int(num)
except:
  print('Please enter a decimal number')

b = ''
while d > 0:
  r = d % 2
  b = b + str(r)
  d = int(d/2)
  
# reverse b so it reads correct
b = b[::-1]

print(str(num) + ' in binary is ' + str(b))


  
  
  