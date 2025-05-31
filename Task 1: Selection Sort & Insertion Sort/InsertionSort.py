# This class implements the Insertion Sort algorithm
class InsertionSort:
    def sort(self, data):
        # Make a copy of the original data
        arr = data.copy()
        
        # Start from the second element and insert it into the sorted part
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            # Move elements of arr[0..i-1], that are greater than key, one position ahead
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            
            # Insert the key at the correct position
            arr[j + 1] = key
        
        return arr
