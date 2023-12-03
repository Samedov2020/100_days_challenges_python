target=int(input())
even=0
for n in range(1,target+1,):
    if n%2==0:
        even=even+n
print(even)
