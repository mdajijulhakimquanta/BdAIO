def solve(sen):
    lenght = len(sen)
    for i in range(lenght - 1):
        if sen[i] == sen[i + 1]:
            print(i + 1, i + 2)
            return

    print(-1, -1)

s = input().strip()
solve(s)