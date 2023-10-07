
class BubbleSort:
    
    def __init__(self, arr,n) -> None:
        self.arr = arr
        self.arr_length = n

    def bubble_sort_(self):
        
        for i in range(self.arr_length): # n times
            for j in range(self.arr_length-i-1): # n-i-1 times
                if self.arr[j] > self.arr[j+1]: # n-i-1 times
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    
    def sorted_Arr(self) -> str:
        print("Sorted Array:",self.arr)

arr = list(map(int, input().split()))
bubble_sort = BubbleSort(arr, len(arr)) # creating an instance of BubbleSort
bubble_sort.bubble_sort_() # calling bubble sort function 
bubble_sort.sorted_Arr() # calling sorted_arr function to print sorted array

"""
Approach:
    Bubble sort compares adjacent elements and place
    the element in it appropriate position.After every
    iteration one element is placed at it correct position.
    Example: 
        arr = [4,3,1,2]
            i = 0
            j = 0
            4  >  3:
                4, 3 = 3, 4
            j = 1
            4 > 1:
                4, 1 = 1, 4
            j = 2
            4 > 2:
                4, 2 = 2, 4
        After 1st iteration 
        arr = [3,1,2,4] 4 is placed at the coorect position

Time Complexity:
    The Time complexity of bubble sort is O(n^2), because the 
    outer runs n times and the inner loop runs n-i-1 times.
    so in total the will run for n*(n-i-1) times. After removing
    the abstract values it becomes O(n^2).

Space Complexity:
    The space complexity of the bubble sort is the size of the 
    Array as it doesn't take any any additional space.

For Further Info: https://www.programiz.com/dsa/bubble-sort
"""