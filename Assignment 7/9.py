def elements(list):
    dict = {}  
    for item in list:
        dict.setdefault(item, []).append(item)
    return dict
list1 = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
output1 = elements(list1)
print("Output for test_list1:", output1)