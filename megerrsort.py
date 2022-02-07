# an array of numbers is given, and the numbers are to be merged in such a way that the resulting array is sorted.
# The array is given as a list of numbers.

def merge_sort(lst):
    if len(lst) > 1:
        return merge(merge_sort(lst[0:len(lst)//2]), merge_sort(lst[len(lst)//2:]))
    else:
        return lst

def merge(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])


if __name__ == '__main__':
    print(merge_sort([1,2,3,4,8,9,18,19,20,5,6,7]))
    print(merge_sort([3,4,5,6,7,8,9,4,5,6,79,1,2,3,4,8,9,18,19,20,5,6,7]))
 
     