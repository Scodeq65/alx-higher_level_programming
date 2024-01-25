#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0

        try:
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0

            if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                if element_2 != 0:
                    result = element_1 / element_2
                else:
                    print("division by 0")
            else:
                print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
