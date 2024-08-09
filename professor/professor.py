import random


def main():
    level = get_level()
    score = simulate_game(level)
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = input("Level: ")
            if level.isdigit() and 1 <= int(level) <= 3:
                return int(level)  # Convert level to integer before returning
        except:
             pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


def simulate_round(x,y):
    count_tried = 1
    while count_tried < 3:
        try:
             answer = int(input(f"{x} + {y} = "))
             if answer == x + y:
                 return True
             else:
                  count_tried += 1
                  print("EEE")
        except:
             count_tried += 1
             print("EEE")
    print(f"{x} + {y}= {x + y}")
    return False

def simulate_game(level):
    score = 0
    count_round = 1
    while count_round <= 10:
        x,y = generate_integer(level)
        if simulate_round(x,y):
            score += 1
        count_round += 1
    return score


if __name__ == "__main__":
    main()




