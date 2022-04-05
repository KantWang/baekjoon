import sys

# 출력시간, 메모리 최적화!
if __name__ == '__main__':
    n, M = map(int, sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split())) 

    # 검색 중단할 지점을 잡기 위해 오름차순 정렬
    cards.sort()

    def blackJack(arr: list, M: int) -> int:
        sum = arr[0] + arr[1] + arr[2]
        temp = 0
        l = len(arr)
        # i, j, k가 커질수록 temp 감소
        for i in range(l - 1, 1, -1):
            temp += arr[i]
            for j in range(i - 1, 0, -1): 
                temp += arr[j]
                for k in range(j - 1, -1, -1): 
                    temp += arr[k]
                    print(f'i: {i}, j: {j}, k: {k}, temp: {temp}')
                    if temp <= M and temp > sum:
                        sum = temp
                        temp -= arr[k]
                        break
                    elif temp <= sum:
                        temp -= arr[k]
                        break
                    temp -= arr[k]
                temp -= arr[j]
            temp -= arr[i]
        return sum

    print(blackJack(cards, M))