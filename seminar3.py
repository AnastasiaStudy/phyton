# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.



# str ='aaabbbddddccceee'
# count = 0

# for i in str:
#     count = 0
#     for j in range(len(str)):
#         if i == str[j]:
#             count += 1
#     # print(f"{i} {count}")
#     print(f"{i} {count}", end=" ")


some_str = input()
# for letter in  set(some_str):
#     print(letter, some_str.count(letter))

for letter in set(some_str):
    amount = 0
    for letter1 in some_str:
        if letter == letter1:
            amount +=1
    print(letter, amount)

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# my_list = set("Сегодня была хорошая погода")
# count = 0
# for i in my_list:
#     if i == range (my_list[i]):
#         count += 1
# print(count+1)

# text = "mango mango peach apple apple banana"
# words = text.split()

# for word in words:
#     if text.count(word) == 1:
#         print(word)
#     else:
#         pass

