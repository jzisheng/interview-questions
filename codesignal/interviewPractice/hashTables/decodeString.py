def decodeString(s):
  strs = [["",1]]
  num = '0'
  for c in s:
    if c.isdigit():
      num = num+c
    elif c == "[":
      strs.append(["",int(num)])
      num = '0'
    elif c == "]":
      ss, cnt = strs.pop()
      strs[-1][0] += ss*cnt
    else:
      strs[-1][0] += c
  return strs[0][0]

print(decodeString("3[a]2[bc]"))
