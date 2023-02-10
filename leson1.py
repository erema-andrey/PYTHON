#Задача No1. Решение в группах
#За день машина проезжает n километров.
#Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
#При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
#Input:
#n = 700 m = 750 Output: 2


# n = 700
# m = 750

# print((m+n-1)//n)

# def quick_sort(array):
#     if len(array) <= 1:
#          return array
#     else:
#          pivot = [0]
#     less = [i for i in array[1:]if i <= pivot]
#     greater = [i for i in array[1:]if i > pivot]
             
#     return quick_sort(less) + [pivot] + quick_sort(greater)
   
# print(quick_sort([1, 2, 3, 6, 9, 2, 23, 16, 24,]))


def merge_sort(nums):
    if len(nums) > 1:
       mid = len(nums) // 2
       left = nums[:mid ]
       right = nums[mid:]
       merge_sort(left)
       merge_sort(right)
       i = j = k = 0
       while i < len(left) and j < len(right):
         if left[i] < right[j]:
            nums[k] = left[i]
         i += 1
       else:
         nums[k] = right[j]
         j += 1
         k += 1
       while i < len(left):
         nums[k] = left[i]
         i += 1
         k += 1
       while j < len(right):
         nums[k] = right[j]
         j += 1
         k += 1
list_1 = [38, 27, 43, 3, 9, 82, 10]
merge_sort(list_1)
print(list_1)
      
      
      