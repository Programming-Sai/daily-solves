


# m =[
# [0,0,0,0,0],
# [0,0,0,0,0],
# [0,1,0,0,0],
# [0,0,0,0,0],
# [0,0,0,0,0],
# ]
# print(search_matrix(m))



def search_matrix(m):
    r=0
    c=-1
    for i in m:
        try:
            c=i.index(1)
            break
        except:
            r += 1
    return r,c


def count_distance(m):
    one_loc = search_matrix(m)
    mid_loc = (2,2)
    return (abs(mid_loc[0] - one_loc[0])) + (abs(mid_loc[1] - one_loc[1]))

m=[]
for i in range(5):
    m.append(list(map(int, input().split())))

print(count_distance(m))


