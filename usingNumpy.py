import numpy as np

heights = [2,4,6,8,10]
widths = [3, 3, 3, 2, 3]

np_height = np.array(heights)
np_width = np.array(widths)

area = np_height * np_width

small_areas = area[area < 15]

print(area)
print(small_areas)
