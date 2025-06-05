import time
import random

def generate_sorted_array(size):
    return sorted(random.sample(range(1, size * 2), size))  # Создаем отсортированный массив

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    array_size = 10000000  # Размер массива
    arr = generate_sorted_array(array_size)
    target = arr[-1]  # Ищем последний элемент

    # Замер времени выполнения
    start_time = time.time()
    linear_search(arr, target)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Время в миллисекундах
    print(f"Время выполнения линейного поиска: {execution_time:.2f} мс")
