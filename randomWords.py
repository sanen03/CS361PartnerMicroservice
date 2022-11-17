import random
import json

verb_list = ["close"
             "tremble",
             "communicate",
             "present",
             "manage",
             "detect",
             "guide",
             "shade",
             "trap",
             "analyze",
             "bump",
             "flood",
             "wait",
             "slap",
             "slow",
             "doubt",
             "agree",
             "spark",
             "sound",
             "alert",
             "back",
             "film",
             "rock",
             "plant",
             "crash",
             "fold",
             "serve",
             "boil",
             "belong",
             "complain",
             "treat",
             "rule",
             "occur",
             "fence",
             "jog",
             "arrive",
             "sparkle",
             "judge",
             "cheat",
             "flow",
             "tip",
             "dress",
             "plug",
             "replace",
             "saw",
             "argue",
             "admit",
             "march",
             "push",
             "mourn"]

noun_list = ["corn",
             "thing",
             "calculator",
             "advertisement",
             "stove",
             "stem",
             "hand",
             "cover",
             "jelly",
             "sound",
             "ship",
             "expansion",
             "laborer",
             "route",
             "pet",
             "respect",
             "dress",
             "chance",
             "memory",
             "blow",
             "girls",
             "grade",
             "ground",
             "price",
             "size",
             "cows",
             "hat",
             "advice",
             "pies",
             "change",
             "whistle",
             "rate",
             "wound",
             "zephyr",
             "development",
             "snail",
             "neck",
             "caption",
             "discussion",
             "stranger",
             "friend",
             "earth",
             "club",
             "van",
             "fireman",
             "branch",
             "representative",
             "hope",
             "skin",
             "balance"]

adjective_list = [
    "impossible",
    "encouraging",
    "outstanding",
    "lamentable",
    "fascinated",
    "kindly",
    "left",
    "defeated",
    "tedious",
    "lovely",
    "luxuriant",
    "exciting",
    "absent",
    "deadpan",
    "high",
    "aboriginal",
    "verdant",
    "rich",
    "woozy",
    "maddening",
    "scandalous",
    "coherent",
    "complete",
    "glossy",
    "quack",
    "far",
    "past",
    "needless",
    "marvelous",
    "sordid",
    "obscene",
    "gleaming",
    "smiling",
    "foolish",
    "loud",
    "light",
    "adventurous",
    "supreme",
    "alleged",
    "adamant",
    "prickly",
    "guttural",
    "free",
    "finicky",
    "available",
    "nauseating",
    "cold",
    "unaccountable",
    "complex",
    "various"]

output = {"Nouns:": [], "Verbs:": [], "Adjectives:": []}


def giveWords(noun, verb, adjective):
    noun_out = []
    verb_out = []
    adjective_out = []
    for i in range(0, noun):
        num = random.randint(0, 48)
        noun_out.append(noun_list[num])
    for i in range(0, verb):
        num = random.randint(0, 48)
        verb_out.append(verb_list[num])
    for i in range(0, adjective):
        num = random.randint(0, 48)
        adjective_out.append(adjective_list[num])
    output["Nouns:"] += noun_out
    output["Verbs:"] += verb_out
    output["Adjectives:"] += adjective_out
    return json.dumps(output)


noun_num = int(input("How many nouns do you want? "))
verb_num = int(input("How many verbs do you want? "))
adjective_num = int(input("How many adjectives do you want? "))
final_output = giveWords(noun_num, verb_num, adjective_num)
with open("output.txt", "w") as f:
    f.write(final_output)
