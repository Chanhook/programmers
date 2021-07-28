def solution(lottos, win_nums):
    dic = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    rank = 6
    count = 0
    zero_count = 0
    lottos = sorted(lottos, reverse=True)
    # print(lottos)

    for lotto in lottos:
        if lotto in win_nums:
            count += 1
        elif lotto == 0:
            zero_count += 1

    # print(count,zero_count)

    answer = [dic.get(count+zero_count), dic.get(count)]
    return print(answer)


solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
