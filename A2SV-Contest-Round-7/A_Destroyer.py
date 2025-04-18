
def check(n, l):
    robot_count = [0] * (max(l)+1)
    for i in l:
        robot_count[i] += 1
    # print(l, robot_count)

    for i in range(len(robot_count)-1):
        # print(i, robot_count[i], robot_count[i+1])
        if robot_count[i] < robot_count[i+1]:
            print("NO")
            return
    print("YES")


t = int(input())  
for _ in range(t):
    n = int(input())  
    l = list(map(int, input().split())) 
    check(n, l)


n=6
l=[0, 1, 2, 0, 1, 0]
n=2
l=[2, 1]
n=9
l=[0,0,0,0,1,1,1,2,2]
n=3
l=[0,0,2]
# check(n, l)

