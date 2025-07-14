import numpy as np

original_array = np.arange(0, 101)
squares_array = original_array ** 2
cubes_array = original_array ** 3

print(original_array)
print(squares_array)
print(cubes_array)
#--------------
import numpy as np
arr1 = np.random.randint(1, 101, size=50)
arr2 = np.random.randint(1, 101, size=50)
combined = np.concatenate((arr1, arr2))
div_by_2 = combined[combined % 2 == 0]
div_by_5 = combined[combined % 5 == 0]
print(arr1)
print(arr2)
print(div_by_2)
print(div_by_5)

