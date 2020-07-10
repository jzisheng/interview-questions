def genPerfSquares(n):
    result = []
    for i in range(1, n//2):
        if i*i > n:
            break
        result.append(i*i)
    return result[::-1]


def numSquares(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    
    result = float('inf')
    
    def bfs(curr, count, squares):
        nonlocal result
        if curr < 0:
            return
        elif curr == 0:
            result = min(result, count)
            return
        else:
            for s in squares:
                bfs(curr-s, count+1, squares)
                if curr-s > 0:
                    break
            pass
        pass
    
    squares = (genPerfSquares(n))
    bfs(n, 0, squares)
    return result
    pass


print(numSquares(12))
