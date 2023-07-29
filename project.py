import random
import matplotlib.pyplot as plt

amount = 50

numbers = [random.randint(0, 1000) for _ in range(amount)]


def merge_sort(number_list, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    plt.bar(list(range(amount)), number_list)
    plt.pause(0.001)
    plt.clf()

    merge_sort(number_list, left, mid)
    merge_sort(number_list, mid + 1, right)

    plt.bar(list(range(amount)), number_list)
    plt.pause(0.001)
    plt.clf()

    merge(number_list, left, right, mid)

    plt.bar(list(range(amount)), number_list)
    plt.pause(0.01)
    plt.clf()


def merge(number_list, left, right, mid):
    left_copy = number_list[left:mid + 1]
    right_copy = number_list[mid + 1:right + 1]

    l_counter, r_counter = 0, 0
    sorted_counter = left

    while l_counter < len(left_copy) and r_counter < len(right_copy):
        if left_copy[l_counter] < right_copy[r_counter]:
            number_list[sorted_counter] = left_copy[l_counter]
            l_counter += 1
        else:
            number_list[sorted_counter] = right_copy[r_counter]
            r_counter += 1

        sorted_counter += 1

    while l_counter < len(left_copy):
        number_list[sorted_counter] = left_copy[l_counter]
        l_counter += 1
        sorted_counter += 1

    while r_counter < len(right_copy):
        number_list[sorted_counter] = right_copy[r_counter]
        r_counter += 1
        sorted_counter += 1


plt.bar(list(range(amount)), numbers)
plt.show()
merge_sort(numbers, 0, len(numbers) - 1)
print(numbers)

