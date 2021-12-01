#Завдання 3
#Варіант 6. Визначте максимальну, мінімальну та середню довжину слів, речень та абзаців у тексті.

import re

def avrg_count(x):
    total_chars = len(re.sub(r'[^a-zA-Z0-9]', '', x))
    num_words = len(re.sub(r'[^a-zA-Z0-9 ]', '', x).split())
    print "Characters:{0}\nWords:{1}\nAverage word length: {2}".format(total_chars, num_words, total_chars/float(num_words))


phrase = '***The ?! quick brown cat:  leaps over the sad boy.'

avrg_count(phrase)