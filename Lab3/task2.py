def find_common_participants(group1, group2, separator=','):

    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    common = set(participants1) & set(participants2)

    return sorted(common)

participants_group1 = "Иванов,Петров,Сидоров"
participants_group2 = "Петров,Сидоров,Смирнов"
print("С разделителем-запятой:",
      find_common_participants(participants_group1, participants_group2))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("\nС разделителем '|':",
      find_common_participants(participants_first_group, participants_second_group, '|'))

print("\nДополнительные примеры:")

print("С разделителем ';':",
      find_common_participants("Иванов;Петров", "Петров;Сидоров", ';'))

print("Без общих участников:",
      find_common_participants("Иванов,Петров", "Сидоров,Смирнов"))