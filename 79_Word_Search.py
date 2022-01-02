def exist(board: list[list[str]], word: str) -> bool:
    def check(i, j, idx):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[idx]:
            return False
        else:
            return True

    def backtrack(i, j, path, idx):
        if path == word:
            return True
        if len(path) < len(word):
            for d in directions:
                next_i, next_j = i + d[0], j + d[1]
                if check(next_i, next_j, idx):
                    visited[next_i][next_j] = 1
                    path += board[next_i][next_j]
                    if backtrack(next_i, next_j, path, idx+1):
                        return True
                    else:
                        path = path[:-1]
                        visited[next_i][next_j] = 0
        return False
    
    m = len(board)
    n = len(board[0])
    visited = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(0)
        visited.append(row)
    
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    idx = 0
    for i in range(m):
        for j in range(n):
            if check(i, j, idx):
                path = board[i][j]
                visited[i][j] = 1
                if backtrack(i, j, path, idx+1):
                    return True
                else:
                    path = path[:-1]
                    visited[i][j] = 0
    return False

if __name__ == '__main__':
    board = [["a","a","b","a","a","b"],["b","a","b","a","b","b"],["b","a","b","b","b","b"],["a","a","b","a","b","a"],["b","b","a","a","a","b"],["b","b","b","a","b","a"]]
    word = "aaaababab"
    print(exist(board, word))
