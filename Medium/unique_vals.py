def unique(numbers):
    my_dict = {}

    for i in numbers:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1

    # for i in my_dict:
    #     if my_dict[i] == 1:
    #         print(i)

    for k, v in my_dict.items():
        if v == 1:
            print(k, v, sep=' : ')


unique([1, 1, 2, 2, 2, 3, 3, 3, 5, 4])
