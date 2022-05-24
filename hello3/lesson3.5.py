# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(nums):
    """ 3 рандомные шутки"""
    list = []
    for i in range(nums):
        nouns1 = random.choice(nouns)
        adverbs1 = random.choice(adverbs)
        adjectives1 = random.choice(adjectives)
        list.append(f'{nouns1} {adverbs1} {adjectives1}')
    return list


print(get_jokes(1))


# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes1(nums, repeats=True):
    list = []
    if not repeats:
        if nums > min(len(nouns), len(adverbs), len(adjectives)):
            return "no way"
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(nums):
                list.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    else:
        for i in range(nums):
            nouns1 = random.choice(nouns)
            adverbs1 = random.choice(adverbs)
            adjectives1 = random.choice(adjectives)
            list.append(f'{nouns1} {adverbs1} {adjectives1}')
        return list


print(get_jokes1(2))
