from typing import List

def find_missing_num(N: int, arr: List[int]) -> int:
    return set(range(1, N + 1)).difference(set(arr)).pop()
    
if __name__ == '__main__':
    assert find_missing_num(5, [1, 2, 4, 5]) == 3
    assert find_missing_num(3, [1, 3]) == 2
