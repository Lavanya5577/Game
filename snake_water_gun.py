import random
def snake_water_gun(computer,mine):
    if (computer==mine):
        return None
    if (computer=='snake' and mine=='gun'):
        return True
    elif (computer=='water' and mine=='snake'):
        return True
    elif (computer=='gun' and mine=='water'):
        return True
    else:
        return False

choice=('snake','water','gun')
computer=random.randint(0,2)
computer=choice[computer]
mine=input("Choose either snake water or gun:")

win=snake_water_gun(computer,mine)
print(f"you choose {mine} and comuter choose {computer}")
if win is None:
    print("Match Drawn")
if win:
    print("You Won")
else:
    print("You Lost")
