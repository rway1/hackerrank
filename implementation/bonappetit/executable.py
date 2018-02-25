import sys



(n, k) = [int(i) for i in input().split(" ")]
c = [int(i) for i in input().split(" ")]
b = int(input())

c.remove(c[k])
if b == sum(c)/2:
    sys.stdout.write("Bon Appetit")
else: sys.stdout.write(str(int(b - sum(c)/2)))