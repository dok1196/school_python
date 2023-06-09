# def flatten_and_sort(array):
#     result_list = []
#     for sub_list in array:
#         result_list += sub_list
#         result_list.sort()
#         return result_list
#
# data = [ [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], [[], []], [[], [1]], [[1, 3, 5], [100], [2, 4, 6]] ]
# for array in data:
#     print(flatten_and_sort(array))
# def get_max_divisible_by_three(num):
#     num_str = str(num)
#     length = len(num_str)
#     if length == 1:
#         return -1
#     # нет решения
#     if num % 3 == 0:
#         max_num = num for i in range(length):
#             for j in range(0, 10):
#                 new_num_str = num_str[:i] + str(j) + num_str[i+1:]
#                 new_num = int(new_num_str)
#                 if new_num % 3 == 0:
#                     max_num = max(max_num, new_num)
#                     return max_num else:
#                     # разделим число на две половины
#     half_length = (length + 1) // 2
#     first_half = int(num_str[:half_length])
#     second_half = int(num_str[half_length:])
#     if second_half % 3 == 0:
#         return num
#     # можно сразу вернуть исходное число
#     else: max_num = num for i in range(half_length, length):
#             for j in range(0, 10):
#                 if j % 3 == 0:
#                     new_second_half_str = second_half_str[:i-half_length] + str(j) + second_half_str[i-half_length+1:]
#                     new_num_str = str(first_half) + new_second_half_str new_num = int(new_num_str)
#                     if new_num % 3 == 0: max_num = max(max_num, new_num)
#                     return max_num
#

def get_max_divisible_by_three(num):
    num_str = str(num)
    length = len(num_str)
    if length == 1:
        return -1 # нет решения
    if num % 3 == 0:
        max_num = num
        for i in range(length):
            for j in range(0, 10):
                new_num_str = num_str[:i] + str(j) + num_str[i+1:]
                new_num = int(new_num_str)
                if new_num % 3 == 0:
                    max_num = max(max_num, new_num)
        return max_num
    else:
        # разделим число на две половины
        half_length = (length + 1) // 2
        first_half = int(num_str[:half_length])
        second_half = int(num_str[half_length:])
        if second_half % 3 == 0:
            return num # можно сразу вернуть исходное число
        else:
            max_num = num
            for i in range(half_length, length):
                for j in range(0, 10):
                    if j % 3 == 0:
                        new_second_half_str = str(second_half)[:i-half_length] + str(j) + str(second_half)[i-half_length+1:]
                        new_num_str = str(first_half) + new_second_half_str
                        new_num = int(new_num_str)
                        if new_num % 3 == 0:
                            max_num = max(max_num, new_num)
            return max_num