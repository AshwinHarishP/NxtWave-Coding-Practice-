def adding_in_dictionaries_1(values_dict_1,keys_dict_1):
    dict_a = dict()
    for i in range(len(keys_dict_1)):
        values_1 = int(values_dict_1[i])
        keys_1 = keys_dict_1[i]
        dict_a[keys_1] = values_1
    return dict_a

keys_dict_1 = input().split(" ")
values_dict_1 = input().split(" ")

keys_dict_2 = input().split(" ")
values_dict_2 = input().split(" ")

dictionaries_1 = adding_in_dictionaries_1(values_dict_1,keys_dict_1)
dictionaries_2 = adding_in_dictionaries_1(values_dict_2,keys_dict_2)

dictionaries_1.update(dictionaries_2)
dictionaries_1 = dictionaries_1.items()
dictionaries_1 = sorted(dictionaries_1)

print(dictionaries_1)
