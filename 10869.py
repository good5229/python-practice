import sys

# a, b = map(int, sys.stdin.readline().split())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)

a, b, c = map(int, sys.stdin.readline().split())
print((a + b) % c)
print((a % c + b % c) % c)
print((a * b) % c)
print((a % c * b % c) % c)
