n  = int(input())

for i in range(0, n):
    n, m = map(int, input().split(" "))
    workList = []
    for i in range(1, n+1):
        workList.append(int(i))

    #print(workList)
    #print(type(workList[0]))

    workDone = list(map(int, input().split()))
    #print(workDone)
    for i in workDone:
        #print("Removing x:{0}[{1}]".format(i,type(i)))
        workList.remove(i)
    
    chefWork = []
    assistentWork  = []
    for i in range(len(workList)):
        if i == 0 or i % 2 == 0:
            chefWork.append(workList[i])
        else:
            assistentWork.append(workList[i])
    for i in chefWork:
        print(i, end=' ')
    print()
    for i in assistentWork:
        print(i, end=' ')
    print()


    


    