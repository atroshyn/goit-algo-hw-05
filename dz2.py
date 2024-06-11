def binary_search(arr, target):

    if not arr:
        raise ValueError("Масив не може бути порожнім")

    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            # Точно знаходимо target, знаходимо upper_bound
            upper_bound = arr[mid]
            while mid + 1 < len(arr) and arr[mid + 1] == target:
                mid += 1
            if mid + 1 < len(arr):
                upper_bound = arr[mid + 1]
            return iterations, upper_bound

    # Якщо ми не знайшли точний елемент
    if left < len(arr):
        upper_bound = arr[left]

    return iterations, upper_bound

# Тестування
arr = [3.6, 3.0, 0.5, 10.0, 1.7, 1.2]
target = 1.2
print(binary_search(arr, target))  # Приклад, де елемент знайдено

target = 0.1
print(binary_search(arr, target))  # Приклад, де елемент не знайдено, але виведемо верхню межу
