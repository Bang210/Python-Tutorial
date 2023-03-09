
h = input('키')
g = input('성별')

def std_weight() :
    if g == '여자' :
        return int(h) * int(h) / 10000 * 21
    if g == '남자' :
        return int(h) * int(h) / 10000 * 22

print('키' + str(h) + 'cm의 표준 체중은' + str(round(std_weight(), 2)) + '입니다.')

