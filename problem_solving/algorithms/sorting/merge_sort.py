# User function Template for python3
class Solution:
    def merge(self, left_arr, right_arr):
        merged_arr = []

        left_arr_size = len(left_arr)
        right_arr_size = len(right_arr)

        i, j = 0, 0
        while i < left_arr_size and j < right_arr_size:
            if left_arr[i] > right_arr[j]:
                merged_arr.append(right_arr[j])
                j += 1
            else:
                merged_arr.append(left_arr[i])
                i += 1

        while i < left_arr_size:
            merged_arr.append(left_arr[i])
            i += 1

        while j < right_arr_size:
            merged_arr.append(right_arr[j])
            j += 1

        return merged_arr

    def mergeSort(self, arr, begin, end):
        if end - begin <= 1:
            return arr[begin:end]

        mid = begin + (end - begin) // 2

        left_arr = self.mergeSort(arr, begin, mid)
        right_arr = self.mergeSort(arr, mid, end)
        merged_arr = self.merge(left_arr, right_arr)
        return merged_arr

    def sortArr(self, arr, n):
        # code here
        sorted_arr = self.mergeSort(arr, 0, n)
        return sorted_arr


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        ans = obj.sortArr(arr, n)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends
