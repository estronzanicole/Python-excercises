import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""


sale_prices = [
  100,
  83,
  220,
  40,
  105,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)

#created a list and stored in variable and counted the amount inside
#took the number of elements divided by to
#then requested the bottom half
#then grabbed the first slice and the second slice and leaving the median alone


# https://bottega.devcamp.com/12/guide/1386
