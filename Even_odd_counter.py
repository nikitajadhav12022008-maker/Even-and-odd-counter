nums = list(map(int,input("enter numbers:").split()))
even = odd = 0
for n in nums:
    if(n%2 == 0):
        even += 1
    else:
        odd += 1

print("even:",even)
print("odd:",odd)