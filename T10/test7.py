import time
import random
from memory_profiler import profile

def generate_sorted_array(size):
    return sorted(random.sample(range(1, size * 2), size))  # Создаем отсортированный массив

@profile
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    array_size = 10000000  # Размер массива
    arr = generate_sorted_array(array_size)
    target = arr[-1]  # Ищем последний элемент

    # Замер времени выполнения
    start_time = time.time()
    binary_search(arr, target)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Время в миллисекундах
    print(f"Время выполнения бинарного поиска: {execution_time:.2f} мс")
