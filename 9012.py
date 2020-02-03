import sys

n = int(sys.stdin.readline().strip())
ans = []
for i in range(n):
    s = sys.stdin.readline().strip()
    stack = []
    if s.count("(") == s.count(")"):
        for j in range(len(s)):
            if s[j] == "(":
                stack.append(s[j])
            elif stack and s[j] == ")":
                del stack[-1]
            else:
                ans.append("NO")
                break
        if not stack:
            if len(ans) == i:
                ans.append("YES")
    else:
        ans.append("NO")

for i in range(len(ans)):
    print(ans[i])

