start=0
end=0
print("Enter the starting point")
start=int(input())
print("Enter the ending point")
end=int(input())
print("the numbers in range are")
while start<end:
    print(start)
    if start>=end:
        break
    start +=1
