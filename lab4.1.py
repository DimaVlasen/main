# №Завдання 1:
#Створіть програму, яка буде складати випадкові фрази на основі трьох 
#списків зі словами. З кожного списку вона повинна брати випадковим чином 
#слова і поєднувати їх в одну фразу.
import random



first_list = ['One','Two', 'Three', 'Four', 'Five']
second_list = [ 'Men' , 'Woman' , 'Dog' , 'Bicycle' , 'Book' ]
third_list = [ 'Riding' , 'Flying' , 'Standing' , 'Falling' , 'Reading' ]

list_of_strings_list = [first_list, second_list, third_list]
                                            
def random_phrase():
    result_string = ""
    for i in range(0,3):
        random_index = random.randrange(0,4)   
        result_string = result_string + list_of_strings_list[i][random_index] + " "

    return result_string

print(random_phrase())     
             