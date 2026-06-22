#longest repeating substring
s = input()
seen = {}
start = 0
max_len = 0
for i in range(len(s)):
    if s[i] in seen and seen[s[i]] >= start:
        start = seen[s[i]] + 1
    seen[s[i]] = i
    max_len = max(max_len, i - start + 1)
print(max_len)


#warehouse shipment
n = int(input())
warehouse = set()
for _ in range(n):
    x = int(input())
    if x > 0:
        warehouse.add(x)
    else:
        warehouse.discard(-x)
print(len(warehouse))


#smart server money allocation
n = int(input())
arr = list(map(int, input().split()))
limit = int(input())
left = 0
curr = 0
ans = 0
for right in range(n):
    curr += arr[right]
    while curr > limit:
        curr -= arr[left]
        left += 1
    ans = max(ans, right - left + 1)
print(ans)

#logistics route
n = int(input())
arr = list(map(int, input().split()))
if len(set(arr)) == n:
    print("YES")
else:
    print("NO")

#manufacturing quality inspection
n = int(input())
arr = list(map(int, input().split()))
seen = set()
for num in arr:
    if num in seen:
        print(num)
        break
    seen.add(num)