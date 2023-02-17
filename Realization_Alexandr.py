# Task 39.
# first_list = [int(input()) for _ in range(int(input()))]
# second_list = [int(input()) for _ in range(int(input()))]

# 1 способ
# for el in first_list:
#     if el not in second_list:
#         print(el)

# 2 способ
# second_list = set(second_list)
# for el in first_list:
#     if el in second_list:
#         print(el)

# Task 41.

# some_list = [int(input()) for _ in range(int(input()))]
# count = 0
# for ind in range(1, len(some_list) - 1):
#     if some_list[ind - 1] < some_list[ind] > some_list[ind + 1]:
#         count += 1
#
# print(count)

# Task 43.

# some_list = []
# while True:
#     numbers = int(input())
#     if numbers == 0:
#         break
#     some_list.append(numbers)
#
# count_dict = {}
#
# for el in some_list:
#     if count_dict.get(el):
#         count_dict[el] += 1
#     else:
#         count_dict[el] = 1
#
# count = 0
# for value in count_dict.values():
#     count += value // 2
#
# print(count)


# Task 45.

def sum_div(n):
    summa = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            summa += i
    return summa

summ_dict = {}


k = int(input())
for number in range(1, k):
    print(number)
    if summ_dict.get(sum_div(number)):
        summ_dict[summ_dict(number)] = number
    else:
        print(number, summ_dict[sum_div(number)])











