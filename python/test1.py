def solution(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        while (i < len(B) - 1 and B[i] < a):
            i += 1
        if a == B[i]:
            return a
    return -1

A=[1,5,500,800,25,0]
B =[10,50,5,5,1]
print(solution(A,B))
'''
Example test:    ([1, 3, 2, 1], [4, 2, 5, 3, 2])
OK

Example test:    ([2, 1], [3, 3])
OK
'''
