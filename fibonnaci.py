nums = int(input("How many terms? "))
F1, F2 = 0, 1
count = 0
if nums <= 0:
   print("Please enter a positive integer")
elif nums == 1:
   print("Fibonacci sequence upto",nums,":")
   print(F1)
else:
   print("Fibonacci sequence:")
   while count < nums:
       print(F1)
       nth = F1 + F2
       
       F1 = F2
       F2 = nth
       count += 1