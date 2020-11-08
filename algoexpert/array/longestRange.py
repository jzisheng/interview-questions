def largestRange(array):
    # Write your code here.
	array.sort()
	maxCount = 0
	curCount = 0
	
	start = array[0]
	curr = array[0]
	
	res = []
	
	i = 0
	for i in range(len(array)):
		a = array[i]
		b = None if i+1 >= len(array) else array[i+1]
		if a and b:
			curr = a
			if a+1 != b:
				res.append([start,curr])
				start = b
		else:
			res.append([start,curr])
	print(res)
	return [0,0]
