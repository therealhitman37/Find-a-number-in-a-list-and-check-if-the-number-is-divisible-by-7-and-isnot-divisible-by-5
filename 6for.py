#Find a number in a list and check if the number is divisible by 7 and isnot divisible by 5

l1 = list(map(int, input(" Enter the list: ").split(",")))

l2 = []
    
for x in l1:
    if (x%7== 0) and (x%5!= 0):
        l2.append(str(x))


print(','.join(l2))



