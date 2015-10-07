import random


shakespeare = "methinks it is like a wease"

"""
    Task from http://interactivepython.org/runestone/static/pythonds/index.html.
    Infinity monkeys. Every time they print a random string. What time they need to print the right string.
    We write a three functions.
    First functions would be generate a random string from 26 symbols and space

"""
#For easiest way, i decide to write my list by those path
split_alphabet = "a b c d e f g h i j k l m n o p q r s t u v x w y z"
alphabet = split_alphabet.split(' ')
alphabet.append(' ')




def generator(alphabet):
    clock = 0
    random_list = []

    while clock != 27 :
        i = random.randint(0,26)
        random_list.append(alphabet[i])
        clock += 1

    gen_string = "".join(random_list)
    return gen_string

high_point = [x for x in generator(alphabet)] 


# The second function should compare strings that we generate with string from Shakespeare
def compare(gen_string):

    per = 0
    for clock in range(0,27):

        if gen_string[clock] == shakespeare[clock]:
           per += 1

    percent = (per/len(gen_string))*100
    return percent

def compare_to_high(gen_string):


    for clock in range(0,27):
        if gen_string[clock] == shakespeare[clock]:
            high_point[clock] = gen_string[clock]






# Third function would call fist two functions while we don't have 100% alignment
def monkey_work():
    clock = 1
    best_string = generator(alphabet)
    best_chance = compare(best_string)
    compare_to_high(best_string)
    while best_chance != 100.0 :
        clock += 1
        clock_string = generator(alphabet)
        clock_chance = compare(clock_string)
        compare_to_high(clock_string)

        if clock_chance > best_chance :
            best_string = clock_string
            best_chance = clock_chance
        if clock%2 == 0:
            print(best_string)
            print(best_chance)
            print(clock)
            print("".join(high_point))




monkey_work()





