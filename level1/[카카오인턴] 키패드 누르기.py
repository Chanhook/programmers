def solution(numbers, hand):
    answer = ''
    l_hand = [0, 0]
    r_hand = [2, 0]
    dic = dict()
    for number in numbers:
        if number == 1:
            dic[number] = [0, 3]
        elif number == 2:
            dic[number] = [1, 3]
        elif number == 3:
            dic[number] = [2, 3]
        elif number == 4:
            dic[number] = [0, 2]
        elif number == 5:
            dic[number] = [1, 2]
        elif number == 6:
            dic[number] = [2, 2]
        elif number == 7:
            dic[number] = [0, 1]
        elif number == 8:
            dic[number] = [1, 1]
        elif number == 9:
            dic[number] = [2, 1]
        elif number == 0:
            dic[number] = [1, 0]
    # print(dic)

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            l_hand = dic.get(number)
        elif number in [3, 6, 9]:
            answer += 'R'
            r_hand = dic.get(number)
        else:
            x, y = dic.get(number)
            x1, y1 = l_hand
            x2, y2 = r_hand
            d1 = abs(x-x1)+abs(y-y1)
            d2 = abs(x-x2)+abs(y-y2)
            # 대칭
            if d1 == d2:
                if hand == "right":
                    answer += 'R'
                    r_hand = [x, y]
                else:
                    answer += 'L'
                    l_hand = [x, y]
            # 비대칭
            elif d1 > d2:
                answer += 'R'
                r_hand = [x, y]
            else:
                answer += 'L'
                l_hand = [x, y]
        # print(l_hand,r_hand)
        # 7->2 와 0->2는 같다..
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# LRLLLRLLRRL
