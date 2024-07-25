class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n // 2, -1, -1):
            self.heapify(nums, n, i)
        for i in range(n - 1, 0, -1):
            (nums[i], nums[0]) = (nums[0], nums[i]) 
            self.heapify(nums, i, 0)
        return nums
    
    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i]) 
            self.heapify(arr, n, largest)
