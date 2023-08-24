def get_first_and_third_chars(items):
    result = []
    for elem in items:
        if len(elem) >= 3:
            result.append(elem[0] + elem[2])
        else:
            result.append(elem)
    return result


color_list = ["red", "blue", "green", "gray"]
check = get_first_and_third_chars(color_list)
print(check)
