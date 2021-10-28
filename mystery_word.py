

with open("words.txt") as file:
    word_string = file.read()
    word_list = word_string.split("\n")

ycw_easy = []
easy = []
normal = []
hard = []


def sort_by_difficulty(x=word_list):
    for word in x:
        if len(word) < 4:
            ycw_easy.append(word)
        elif 3 < len(word) < 7:
            easy.append(word)
        elif 6 < len(word) < 9:
            normal.append(word)
        elif 8 < len(word):
            hard.append(word)


sort_by_difficulty()

print(len(ycw_easy), len(easy), len(normal), len(hard))
