numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_num = 4
numbers[missing_num] = round((sum(numbers[:missing_num]) + sum(numbers[missing_num + 1:])) / len(numbers) , 2)
print("Измененный список:", numbers)
