from itertools import permutations as A

def judge(a1, b1, a2, b2, a3, b3)->int:
    per4= [[1,0,0],[1,1,0],[1,1,1],[0,0,0]]
    per6 = [[1,0],[1, 1], [0, 0]]
    for m1, m2, m3 in A(((a1, b1), (a2, b2), (a3, b3))):
        print(m1, m2, m3)
        for x in per4:
            if (m1[x[0]] == m2[x[1]] == m3[x[2]])\
                or ((m1[x[0]] + m2[x[1]] == m3[0] or m1[x[0]] + m2[x[1]] == m3[1]) and m1[x[1]] == m2[x[0]]):
                return 4
    
    # 必须用两次全排列
    for m1, m2, m3 in A(((a1, b1), (a2, b2), (a3, b3))):
        for x in per6:
            if (m1[x[0]] == m2[x[1]])\
                or ((m1[x[1]] + m2[x[0]] == m3[0]) or (m1[x[1]] + m2[x[0]] == m3[1])):
                return 6
    return 8


n = int(input())
while n != 0:
    n -= 1
    a1, b1, a2, b2, a3, b3 = map(int, input().split())
    print(judge(a1, b1, a2, b2, a3, b3))
