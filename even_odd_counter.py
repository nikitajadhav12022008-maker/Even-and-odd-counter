#python based Even-odd-counter:
#list,input and split nums
nums = list(map(int,input("enter numbers:").split()))
#setting even and odd to 0
even = odd = 0
#for loop running
for n in nums:
    #conditions to check even and odd nums
    if(n % 2 == 0):
        even += 1
    else:
        odd += 1
#finally print even and odd
print("even:",even)
print("odd:",odd)

