def countArrangement(n: int) -> int:
    def check(num, idx):
        if num in visited or (num % idx and idx % num):
            return False
        else:
            return True

    def backtrack(idx, num_of_beat_arrt):
        if idx == n + 1:
            num_of_beat_arrt += 1
        else:
            for num in range(1, n+1):
                if check(num, idx):
                    visited.add(num)
                    num_of_beat_arrt = backtrack(idx+1, num_of_beat_arrt)
                    visited.remove(num)
        return num_of_beat_arrt
    
    num_of_beat_arrt = 0
    visited = set()
    idx = 1
    for num in range(1, n+1):
        if check(num, idx):
            visited.add(num)
            num_of_beat_arrt = backtrack(idx+1, num_of_beat_arrt)
            visited.remove(num)
    return num_of_beat_arrt
    
if __name__ == '__main__':
    n = 10
    print(countArrangement(n))

