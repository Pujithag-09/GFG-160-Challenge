class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        first = second = float('-inf')  # Corrected variable names

        for i in range(n):
            if arr[i] > first:  # Update first largest
                second = first  # Update second largest before updating first
                first = arr[i]  
            elif arr[i] > second and arr[i] != first:  # Correct condition for second largest
                second = arr[i]

        return second if second != float('-inf') else -1  # Return second largest or -1 if not found

# Example usage
arr = [12, 35, 1, 10, 34, 1]
sol = Solution()
print(sol.getSecondLargest(arr))  # Output: 34
