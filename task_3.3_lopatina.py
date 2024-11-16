# TODO  Напишите функцию count_letters
def count_letters(text_str):
    letters_dict = {}
    for letter in text_str:
        if letter.isalpha():
            letter = letter.lower()
            letters_dict[letter] = letters_dict.get(letter, 0) + 1
    return letters_dict

# TODO Напишите функцию calculate_frequency

def calculate_frequency(letters_dict):
    letters_amount = sum(letters_dict.values())
    frequency_dict = {}
    for letters in letters_dict:
        frequency_dict[letters] = letters_dict[letters]/ letters_amount
    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

letters_dict = count_letters(main_str)
freq_cal = calculate_frequency(letters_dict)
for item in freq_cal.items():
    print(f"{item[0]}: {item[1]:.2f}")