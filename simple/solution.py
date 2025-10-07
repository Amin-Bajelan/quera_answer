import math

def calculator(n, m, li):
    number_calculate = math.ceil(n / m)
    final_list = []
    start = 0
    end = m

    for _ in range(number_calculate):
        final_list.append(sum(li[start:end]))
        start += m
        end = min(end + m, n)

    final_num = final_list[0]
    for i in range(1, len(final_list)):
        if i % 2 == 0:
            final_num += final_list[i]
        else:
            final_num -= final_list[i]

    return final_num

