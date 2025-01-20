from typing import List

def wave_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        if (i % 2 == 0 and arr[i] < arr[i - 1]) or (i % 2 == 1 and arr[i] > arr[i - 1]):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr

if __name__ == '__main__':
    assert wave_sort([10, 5, 6, 3, 2, 20, 100, 80]) == [10, 5, 6, 2, 20, 3, 100, 80]
    assert wave_sort([1, 2, 3, 4, 5, 6]) == [2, 1, 4, 3, 6, 5]
