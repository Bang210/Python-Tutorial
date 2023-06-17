import sys
input = sys.stdin.readline

num_tests = int(input())
ans = 0

for i in range(num_tests) :
    group = list()
    word = input().rstrip()
    check = 1
    for j in range(len(word)) :
        if j == 0 :
            group.append(word[j])
        else :
            if word[j] == word[j - 1] :
                pass
            elif word[j] not in group :
                group.append(word[j])
            else :
                check = 0
                break
    if check == 1 :
        ans += 1
print(ans)