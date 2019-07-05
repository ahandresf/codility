# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    L=S.count('L') #two
    O=S.count('O') #two
    A=S.count('A') #one
    N=S.count('N') #one
    B=S.count('B') #one
    L1=[A,N,B] #list of ones reps
    L2=[L,O] #list of two reps
    L1.sort() #list one organize
    L2.sort() #list two organize
    limit1=L1[0] #lower counter of ones equal to limit
    limit2=L2[0]//2 #lower counter of twos normilize to limit
    limit = min(limit1,limit2) #find minimum number of reps
    return limit  #return result
