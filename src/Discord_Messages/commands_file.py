from collections import defaultdict
import random


def return_joke() -> str:
    with open("Text_Files/quotes_f.txt", "r") as file:
        jokes = file.readlines()

        random_joke = random.choice(jokes).replace("@", "\n").split("$sep$")
        return f"{random_joke[0].strip()}\n\t-{random_joke[1].strip()}"


def roll_die(count: int):
    res = [random.randint(1, 6) for i in range(count)]
    return " ".join([str(x) for x in res])


if __name__ == "__main__":
    jokes = defaultdict(str)

    with open("quotes_npp.txt") as new_file:
        for i in new_file:
            i.strip()
            name, joke = i.split(":", 1)
            name = name.strip()
            joke = joke.strip()
            jokes[name] = joke

    with open("Text_Files/quotes_f.txt", "w") as new_file:
        for key, value in jokes.items():
            new_file.write(f"{value}$sep${key}\n")

    print(roll_die(10))
