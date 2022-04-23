'''
set = collection which is unordered, unindexed, no duplicates values
'''

utensils = {"fork", "spoon","kinfe", "plate","kinfe", "kinfe"}
dishes = {"bowl", "plte", "cup"}
'''
utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
'''
dishes.update(utensils)
dinner_table = utensils.union(dishes)
for x in utensils:
    print(x)