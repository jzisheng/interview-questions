def maxPathSum(tree):
    # Write your code here.
	if not tree: return 0
	maxsum = float('-inf')
	def explore(node):
		nonlocal maxsum
		if node == None:
			return 0
		nval = node.value
		ls = explore(node.left)
		rs = explore(node.right)
		
		asRoot = max(nval+ls+rs, nval+ls, nval+rs, nval)
		maxsum = max(maxsum,asRoot)
		
		return max(nval+ls,nval+rs)
	rmp = explore(tree)
	maxsum = max(maxsum,rmp)
	return maxsum
print("hello")
