# Program for Bubble Sort Algorithm
'''def bubbleSort(arr):
	
	n = len(arr)
	
	for i in range(n):
		for j in range(0, n - i - 1):    # Range of the array is from 0 to n-i-1
			
			if arr[j] > arr[j + 1]:      # Swap the elements if the element found
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [2,10,4,6]
	
bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("%d" % arr[i])'''

# Selection Sort algorithm in Python
'''def selectionSort(array, size):
	
	for s in range(size):
		min_idx = s
		
		for i in range(s + 1, size):
			if array[i] < array[min_idx]:
				min_idx = i
		(array[s], array[min_idx]) = (array[min_idx], array[s])

arr = [ 7, 2, 1, 6 ]
size = len(arr)
selectionSort(arr, size)

print('Sorted Array in Ascending Order is :')
print(arr)'''

	

