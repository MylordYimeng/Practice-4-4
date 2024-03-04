n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

def f(A, B, C) -> int:
    ans = 0
    summ = 0
    other = []
    for i in range(n):
        diff = A[i] - B[i] - C[i]
        if diff >= 0:
            ans += 1
            summ += diff
        else:
            other.append(diff)
    other = sorted(other, reverse=True) # diff为负数
    for x in other:
        summ += x
        if summ > 0:
            ans += 1
        else:
            break
    return ans

print(max(f(A, B, C), f(B, A, C), f(C, A, B)))
        
