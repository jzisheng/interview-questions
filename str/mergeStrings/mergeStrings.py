'''
merge strings

get counts of characters in string
# maps of counts of each string
cs1
cs2

res = ''

"dce" 
 i
"cccbd"
 j

ord('a')
while i < len(cs1) and j < len(cs2):

if counts1[c1] == counts[c2]:
  if chrLt(c1, c2):
    res += c1
    i+=1
  else:
    res += c2
    j+=1
else:
  if counts1[c1] < counts[c2]:
    res += c1
    i += 1
  else:
    res += c2
    j += 1
if i < len(cs2) .. append rest of str
if j < len(cs2) .. append rest of str
'''

from collections import defaultdict
def chrLt(a,b):
  return ord(a)-ord('a') < ord(b)-ord('a')

def chrEq(a,b):
  return ord(a)-ord('a') == ord(b)-ord('a')
#
def getCounts(s):
  counts = defaultdict(int)
  for c in s:
    counts[c] += 1
  return counts
  pass

def mergeStrings(s1,s2):
  res = ''
  counts1 = getCounts(s1)
  counts2 = getCounts(s2)
  
  i=j=0
  while i < len(s1) and j < len(s2):
    c1, c2 = s1[i], s2[j]
    # print("{} {}".format(c1, c2))
    if counts1[c1] == counts2[c2] and chrEq(c1,c2):
      res += c1
      i+= 1
    elif counts1[c1] == counts2[c2]:
      if chrLt(c1, c2):
        res += c1
        i += 1
      else:
        res += c2
        j += 1
    else:
      if counts1[c1] < counts2[c2]:
        res += c1
        i += 1
      else:
        res += c2
        j += 1
  if i < len(s1): res += s1[i:]
  if j < len(s2): res += s2[j:]
  return res

s1 = "super"
s2 = "tower"

s1 = "dce"
s2 = "cccbd"



s1 = "ougtaleegvrabhugzyx"
s2 = "wvieaqgaegbxg"
print("owvieaqugtaleegvrabhugzyxgaegbxg")
print(mergeStrings(s1, s2))
