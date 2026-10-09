import numpy as np

# 1. Create an array consisting of linearly spaced elements between 0 to 9
# (Using 10 evenly spaced points from 0 to 9 inclusive)
arr = np.linspace(0, 9, 10)
print("Original Array:")
print(arr)

# 2. Replace all odd numbers in this array with -1 without modifying the original array
# Creates a copy where elements with an odd integer value are replaced with -1
new_arr = arr.copy()
new_arr[new_arr % 2 != 0] = -1

print("\nArray with Odd Numbers Replaced by -1:")
print(new_arr)

print("\nOriginal Array (Unmodified):")
print(arr)

# 3. Create a new array that contains the original 1-dimensional array converted into a 2-dimensional array with two rows
arr_2d = arr.reshape(2, 5)
print("\n2-Dimensional Array (2 rows, 5 columns):")
print(arr_2d)

# 4. Iterate through the original array and find out sum of all evens
even_sum = 0
for element in arr:
    if element % 2 == 0:
        even_sum += element

print("\nSum of all even elements in the original array:")
print(even_sum)