# Given an array A of N elements. Find the majority element in the array. 
# A majority element in an array A of size N is an element that appears more than N/2 times in the array.

#Input:  
#The first line of the input contains T denoting the number of testcases. 
#The first line of the test case will be the size of array and second line will be the elements of the array.

#Output: 
#For each test case the output will be the majority element of the array. Output "-1" if no majority element is there in the array.

from collections import Counter
#get input

T = int(input()) # number of test cases

for i in range(0,T):
    n = int(input()) # size of array
    arr = list(map(int,input().split())) # array
    
    occurences = dict(Counter(arr))
    
    if any(value > (n/2) for value in list(occurences.values())) == True: # checks if there is any majority
       
        majority = [number for number,count in occurences.items() if count > (n/2)] # returns number if count> n/2
        print(str(majority)[1:-1])
    else: # if there is no majority
        print(-1)
    
