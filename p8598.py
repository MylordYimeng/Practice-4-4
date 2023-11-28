n = int(input())
read = ""
while (n != 0):
    n -= 1
    read += input() + ' '
read = read.split()
read = [int(i) for i in read]
read.sort()
n = len(read)
a, b = n, n
for i in range(1,n,1):
    if read[i] == read[i-1]:
        b = read[i]
    elif read[i] != read[i-1] + 1:
        a = read[i] - 1
print(f"{a} {b}")