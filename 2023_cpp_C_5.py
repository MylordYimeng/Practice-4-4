a, b = map(int, input().split())
mod = 998244353
def eular(n) -> int:
    prime = []
    ans = 0
    phi = [0] * (n + 1)
    not_prime = [False] * (n + 1)
    for i in range(2, n + 1):
        if not not_prime[i]:
            prime.append(i % mod)
            phi[i] = (i - 1) % mod
        for x in prime:
            if x * i > n:
                break
            not_prime[x * i] = True
            if x % i == 0:
                phi[i * x] = (phi[i] * x) % mod
            else:
                phi[i * x] = (phi[i] * (x - 1)) % mod # phi[i] * phi[x]
    return phi[n]
print(pow(a, b-1, mod) * (eular(a)%mod)%mod)
        
# 应该没啥问题, 但是爆内存
