def convert_to_math(my_str):

    array = [i for i in my_str]
    for i in range(len(array)):
        if array[i] == '?':
            array[i] = '*'
    print(array)        
    final_str = ''
    for j in array:
        final_str += j
    final_answer = eval(final_str)
    return final_answer
