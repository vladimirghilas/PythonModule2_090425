# Задача "Игра "Камень, ножницы, бумага"

# Создайте функцию, которая имитирует игру "Камень, ножницы, бумага" между пользователем и компьютером.
# Компьютер должен делать случайный выбор (камень, ножницы или бумага).
# Пользователь должен ввести свой выбор.
# Определите победителя и выведите результат.
import random
<<<<<<< HEAD

def play_random():
list1 = ["камень", "ножницы", "бумага"]
choise_comp = random.choice(list1)
choise_pers =("сделай свой выбор: 1:камень 2:ножницы 3:бумага")
=======
<<<<<<< HEAD
>>>>>>> afc805d945eea0ba1b7417347f6bb8cd93ab8091
=======
>>>>>>> edff1afe7cf57e833d31e25131a00c7047c43c8c
>>>>>>> patch3

def winner_rock_paper_scissors(player_choice: str, comp_choice: str) -> str:
    """
    Камень -> Ножницы
    Ножницы -> Бумага
    Бумага -> Камень
    """
    # "Игрок" | "Компьютер" | "Ничья"
    wins_against = {
        "Камень": "Ножницы",
        "Ножницы": "Бумага",
        "Бумага": "Камень"
    }

    if player_choice == comp_choice:
        return "Ничья"
    elif wins_against[player_choice] == comp_choice:
        return "Игрок"
    else:
        return "Компьютер"

pl_choice = input("Сделайте свой выбор: ")
comp_choice = random.choice(["Камень", "Ножницы", "Бумага"])

print(f"Компьютер выбрал: {comp_choice}")
print(f"Победил {winner_rock_paper_scissors(pl_choice, comp_choice)}")
# print(winner_rock_paper_scissors("Камень", "Бумага")) # "Компьютер"
# print(winner_rock_paper_scissors("Бумага", "Бумага")) # "Ничья"
# print(winner_rock_paper_scissors("Ножницы", "Бумага")) # "Игрок"