# Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

#Input:
#The first line of input contains an integer T denoting the number of test cases.
#For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.

#Output:
#Print the missing number in array.



#get input

T = int(input()) # number of test cases

for i in range(0,T):
    n = int(input()) # size of array
    arr = list(map(int,input().split())) # array
    
    complete_arr = list(range(1,n+1)) # list of all elements from 1 to n
    
    missing = list(set(complete_arr) - set(arr)) # missing element
    
    print(str(missing)[1:-1])  # print w/o brackets
