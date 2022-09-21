import math


manuitems = int(input("Amount of items manufactured"))
item_box = int(input("Number of items packed per box"))

computation = math.ceil(manuitems /item_box)


print(f"For {manuitems} items, packing {item_box}"
    f" items in each box, you will need {computation} boxes.")
