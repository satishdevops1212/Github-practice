import numpy as np

# 1. Create a basic 1D and 2D array (Matrix)
print("--- 1. Array Creation ---")
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", array_1d)
print("2D Array:\n", array_2d)
print("Shape of 2D Array:", array_2d.shape)  # Returns (rows, columns)
print()

# 2. Handy built-in array initializers
print("--- 2. Built-in Initializers ---")
zeros = np.zeros((2, 3))       # Array filled with 0s
arange = np.arange(0, 10, 2)   # Numbers from 0 to 8, skipping by 2
linspace = np.linspace(0, 1, 5) # 5 evenly spaced numbers between 0 and 1

print("Zeros:\n", zeros)
print("Arange:", arange)
print("Linspace:", linspace)
print()

# 3. Vectorized Math Operations (Fast & Element-wise)
print("--- 3. Array Mathematics ---")
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Addition (a + b):     ", a + b)
print("Multiplication (a * 2):", a * 2)
print("Exponentiation (b ** 2):", b ** 2)
print()

# 4. Basic Statistical Functions
print("--- 4. Statistics ---")
data = np.array([12, 15, 18, 22, 30, 45, 50])

print("Mean (Average):", np.mean(data))
print("Standard Dev:  ", np.std(data))
print("Maximum Value: ", np.max(data))
print()

# 5. Indexing and Slicing
print("--- 5. Slicing ---")
# Get elements from index 1 up to (but not including) index 4
print("Slice of 1D Array [1:4]:", array_1d[1:4]) 
# Get a specific element from the 2D array (Row 1, Column 2 -> zero-indexed)
print("Specific element [1, 2]:", array_2d[1, 2])
