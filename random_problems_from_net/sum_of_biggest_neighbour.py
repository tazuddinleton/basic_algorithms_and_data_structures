def sum(input_array):
    checked = dict()
    for i in range(0, len(input_array)):
        if input_array[i] in checked:
            checked[input_array[i]].append(input_array[i])
        else:
            checked[input_array[i]] = [input_array[i]]
    # print(checked)
    max_repeat = 0
    for key, value in checked.items():
        i = len(value)
        if i >= max_repeat:
            max_repeat = i
    filtred_items = []
    for key, value in checked.items():
        i = len(value)
        print(value, i, max_repeat-1)
        if i >= max_repeat-1:
            filtred_items.append(value)

    max_item = 0
    max_item_count = 0
    for i in range(0, len(filtred_items)):
        if filtred_items[i][0] >= max_item:
            max_item = filtred_items[i][0]
            print(filtred_items)
            max_item_count = len(filtred_items[i])

    # print(max_repeat, filtred_items, max_item_count, max_item)
    return max_item * max_item_count
