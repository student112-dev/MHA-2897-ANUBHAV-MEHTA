# This class implements the Selection Sort algorithm
class SelectionSort:
    def sort(self, data):
        # Make a copy of the original data so that the input is not modified
        arr = data.copy()
        n = len(arr)
        
        # Outer loop iterates through each index in the array
        for i in range(n):
            # Assume the current index is the minimum
            min_idx = i
            
            # Inner loop finds the index of the minimum element in the remaining unsorted part
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            # Swap the found minimum element with the first element of the unsorted part
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Return the sorted array
        return arr
