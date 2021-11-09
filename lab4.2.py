import os
#Завдання 2:
#Візьміть текстовий файл, що містить Вашу улюблену художню книгу.
#1. Визначте загальну кількість символів у тексті з пробілами та без пробілів.
#2. Визначте загальну кількість слів у тексті, загальну кількість різних слів 
#(без повторів) та кількість унікальних слів, що зустрічаються тільки один раз.

def total_amout_of_words_in_file():
    num_words =0 #слова
    num_chars =0
    #words_set = set() #amount of different words
    num_uniq = 0 #amount of unique words
    words_array = []
    filename = "text_for_task_3.txt"
    exclude = ",.@#$"
    with open(filename, 'r') as f:
         for line in f:
            words = line.split()
            for word in words:
                char = list(words)
                words_array = words_array + num_chars
            num_words += len(words)
            num_chars += len(line)
    print ("Amout of words:", num_words)
    print ("With spaces:", num_chars)
    num_uniq =  len(set(words_array)-set(exclude))
    print ("Total amount of unique words:", num_uniq)    


#print("Without spaces : ", num_words)
#print("Total amount of different words : ", num_words)
#print("Total amount of unique words : ", num_words)