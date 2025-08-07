# import math
# def cub(x):
#     print(math.pow(x,2))
# if __name__ == '__main__':
#     print("Не будет")
# # print("Будет")
# name="Sam"
# def sum(a,b):
#     return a+b
# def raz(a,b):
#     return a-b


        # игра "ВИСИЛИЦА"
def hangman(word):
    wrong=0
    stages=["",
    "__________          ",
    "|         |         ",
    "|         ○         ",
    "|        /|\        ",
    "|        / \        ",
    "|                   ",
    ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Добро пожаловать на казнь!")
    while wrong<len(stages)-1:
        print("\n")
        msg="Введите букву: "
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong +=1
        print(("".join(board)))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Вы выйграли! Было загадано слово: ")
            print("".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:e]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))
import random

lis="год человек время дело жизнь день рука работа слово место лицо друг глаз вопрос дом страна мир случай голова ребенок сила конец вид система часть город отношение женщина деньги земля машина вода отец проблема час право нога решение дверь образ история власть закон война бог голос тысяча книга возможность результат ночь стол имя область статья число компания народ жена группа развитие процесс суд условие средство начало свет путь душа уровень форма связь минута улица вечер качество мысль дорога действие месяц государство язык любовь взгляд мама век школа цель общество деятельность организация президент комната порядок момент театр"
track=lis.split()
r = random.randint(0, 95)
hangman(track[r])