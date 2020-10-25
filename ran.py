# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
 
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
