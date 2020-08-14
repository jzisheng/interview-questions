
def nQueens(n):
    return find(n)

def find(n,state=[],col=1):
    if col > n: return [state]
    res = []
    for i in range(1, n+1):
        if invalid(state, i): continue
        for sol in find(n, state + [i], col+1): res += [sol]
    return res

def invalid(s,r2):
    if not s: return False
    if r2 in s: return True
    c2 = len(s) + 1
    return any(abs(c1-c2) == abs(r1-r2) for c1, r1 in enumerate(s,1))
    
                    
    
print(nQueens(6))
