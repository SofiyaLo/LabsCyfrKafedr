# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, separator = ','):
    first_list = first_group.split(separator)
    second_set = set(second_group.split(separator))
    common_part = second_set.intersection(first_list)
    return list(common_part)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))