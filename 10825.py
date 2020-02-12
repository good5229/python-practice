import sys

n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    name, kor, eng, mat = sys.stdin.readline().split()
    arr.append((name, int(kor), int(eng), int(mat)))

arr = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for student in arr:
    print(student[0])
