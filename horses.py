for i in range(int(input())):
    n  = int(input())
    skillList =  list(map(int, input().split(' ')))
    skillList = sorted(skillList)
    i = 0
    diff = 9999999999
    for j in range(1, len(skillList)):
        tmp = skillList[j] - skillList[i]
        if tmp < diff:
            diff = tmp
        i += 1
    print(diff)

