# get input
T = int(input())
for i in range(0,T):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(1) # since there is only one element
    else:
        # checks if the sum of the elements before equal the sum of the elements following the element 
        result = [i+1 for i in range(1,len(arr)) if sum(arr[:i]) == sum(arr[i+1:])]
        if result == []: # if empty, there is no equilibrium point 
            print(-1)
        else:
            print(*result)
      
