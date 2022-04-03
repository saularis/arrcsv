# arrcsv
A python package for converting array to csv

## Install
```cmd
pip install arrcsv
```

## Use
```python
from arrcsv import arr_to_csv

arr = [1, 2, 3, 4, 5, 6]
csv = arr_to_csv(arr)
print(csv) # 1,2,3,4,5,6

# Works with 2D array as input
arr2 = [[1, 2, 3], [4, 5, 6]]
csv = arr_to_csv(arr2)
print(csv) # 1,2,3
           # 4,5,6

# Works with 3D array as input
arr3 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
csv = arr_to_csv(arr3)
print(csv) # 1,2,3
           # 4,5,6
           # 7,8,9
           # 10,11,12 
```