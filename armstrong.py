num = int(input("Enter a number: "))
# initialize sum
sum = 0
# find the sum of the cube of each digit
temp = num
for i in range(num):
   digit = num% 10
   sum = digit ** 3 +sum  
   num //= 10
# display the result
if temp == sum:
   print(temp,"is an Armstrong number")
else:
   print(temp,"is not an Armstrong number")