def find_common_participants(first_group, second_group, separator = ','):
    first_list = first_group.split(separator)
    second_set = set(second_group.split(separator))
    
    common_part = second_set.intersection(first_list)
    common_part.sort()
    
    return list(common_part)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
