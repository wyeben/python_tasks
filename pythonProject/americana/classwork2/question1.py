
color_list1 = ["white", "black", "red"]
color_list2 = ["green", "red"]


set_color_list1 = set(color_list1)
set_color_list2 = set(color_list2)


colors_not_in_list2 = set_color_list1 - set_color_list2

print("Colors in color_list1 that are not in color_list2:", colors_not_in_list2)