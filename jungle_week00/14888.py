import sys
import itertools

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    A = [i for i in map(int, sys.stdin.readline().split())]
    o_count = [i for i in map(int, sys.stdin.readline().split())]

    ans = 0

    operator = []
    for i in range(o_count[0]):
        operator.append('+')
    for i in range(o_count[1]):
        operator.append('-')
    for i in range(o_count[2]):
        operator.append('*')
    for i in range(o_count[3]):
        operator.append('/')

    # def comb(lst,n):
    #     ret = []
    #     if n > len(lst): return ret
        
    #     if n == 1:
    #         for i in lst:
    #             ret.append([i])
    #     elif n>1:
    #         for i in range(len(lst)-n+1):
    #             for temp in comb(lst[i+1:],n-1):
    #                 ret.append([lst[i]]+temp)

    #     return ret

    # def perm(lst,n):
    #     ret = []
    #     if n > len(lst): return ret

    #     if n==1:
    #         for i in lst:
    #             ret.append([i])
    #     elif n>1:
    #         for i in range(len(lst)):
    #             temp = [i for i in lst]
    #             temp.remove(lst[i])
    #             for p in perm(temp,n-1):
    #                 ret.append([lst[i]]+p)

    #     return ret

    operator = list(set(itertools.permutations(operator)))

    def insert_operator(left: int, right: int, oper: list, index: int) -> None:
        # print(f'left: {left}, right: {right}, oper: {oper}, index: {index}')
        global n
        global ans
        global A

        if oper[index] == '+':
            ans = left + right
        elif oper[index] == '-':
            ans = left - right
        elif oper[index] == '*':
            ans = left * right
        else:
            if left < 0 and right > 0:
                ans = -((-left) // right)
            else:
                ans = left // right

        if index == n - 2:
            # print('탈출')
            return

        insert_operator(ans, A[index + 2], oper, index + 1)

    insert_operator(A[0], A[1], operator[0], 0)
    min = max = ans

    for i in range(1, len(operator)):
        insert_operator(A[0], A[1], operator[i], 0)
        if min > ans:
            min = ans
        elif max < ans:
            max = ans

    print(max)
    print(min)    