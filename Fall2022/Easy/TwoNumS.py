def twoNumberSum(array, targetSum):
	array.sort()
	left=0
	right = len(array) - 1
	while left < right:
		curr = array[left] + array[right]
		if curr == targetSum:
			return [array[left], array[right]]
		elif curr < targetSum:
			left +=1
		elif curr > targetSum:
			right -= 1
		
	return []

# assuming .sort() takes O(n log n) time, this will take O(nlogn) time and O(1) space