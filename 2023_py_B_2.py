t, n = map(int, input().split())
opn = [list(map(int, input().split())) for _ in range(t)]

def check(t) -> bool:
    rng = []
    for l, s in opn:
        rng.append((l-(t-s), l+(t-s)))

    rng.sort()
    if rng[0][0] > 1:
        return False
    r = rng[0][1]
    for cur_l, cur_r in rng:
        if cur_l <= r + 1:
            r = max(cur_r, r)
        else:
            break
    return r >= n

l, r = 1, 10 ** 10
while l < r:
    mid = (l + r) >> 1
    if check(mid):
        r = mid
    else:
        l = mid + 1
print(l)

