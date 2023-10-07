def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 

sorted_data = [10, 20, 30, 40, 50, 60, 70, 80, 90]

target_data = 40

result_index = binary_search(sorted_data, target_data)

if result_index != -1:
    print(f"The data {target_data} is found at index {result_index}.")
else:
    print(f"The data {target_data} is not found in the list.")
