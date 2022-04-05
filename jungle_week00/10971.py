# 반드시 다시 풀자 제대로 된 풀이로
import sys

n = int(sys.stdin.readline())
w = [[] for i in range(n)]
for i in range(n):
    w[i] = list(map(int, sys.stdin.readline().split())) 
print(w)

ans = []
finish = 0
def salesTour2(start: int, dest: list, cost: int):
    # print(f'진입: start:{start}, dest:{dest}, cost:{cost}') 
    global ans
    global finish
    
    if len(dest) == 0:
        cost += w[start][finish]
        # print(f'저장완료, cost:{cost}')
        ans.append(cost)
        return
    
    index = 0

    for i in dest:
        # print(f'index: {index}')
        if w[start][i] == 0:
            # dest.remove(i)
            index += 1
            continue
        
        cost += w[start][i]
        dest.remove(i)            
        salesTour2(i, dest, cost) 
        dest.insert(index, i)
        cost -= w[start][i]
        index += 1  
    
for start in range(n):      
    dest = [a for a in range(n)]
    finish = start
    dest.remove(start)
    # print(f'시작! start:{start}, dest:{dest}')
    salesTour2(start, dest, 0)
    dest.insert(start, start)

# print(ans)
print(min(ans))