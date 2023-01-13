def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input("What is your name? ").title()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input("Enter remainder of your divided by 3: "))
    rem5 = int(input("Enter remainder of your divided by 5: "))
    rem7 = int(input("Enter remainder of your divided by 7: "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input("Enter any number to count: "))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    correct_answer = 2
    
    while True:
        print("Why do we use methods?")
        print("1. To repeat a statement multiple times.")
        print("2. To decompose a program into several small subroutines.")
        print("3. To determine the execution time of a program.")
        print("4. To interrupt the execution of a program.")

        #User answer
        user_answer = abs(int(input("Choose an answer (1-4): ")))
        
        if user_answer == correct_answer:
            print("2. To decompose a program into several small subroutines.")
            break
        else:
            print("Please, try again")
        
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Habot', '2023')
remind_name()
guess_age()
count()
test()
end()