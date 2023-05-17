import random
listWords = [{"post": "This is an action you usually do with your social profile"}, {
    "pool": "This thing is large & has water"}, {"adult": "I can watch 18+ films when i am..."}]
dictKeyword = random.choice(listWords)
keyword = list(dictKeyword)[0].upper()
hint = list(dictKeyword.values())[0]
print("Hint: ", str(hint))
keywordPass = []
for i in range(len(keyword)):
    keywordPass.append("*")
print("Your Keyword has ", len(keyword),
      "letters: ", " ".join(len(keyword)*"*"))
name = input("Your name please: ")
id = random.randrange(100, 10000000)
result = bool
turnMax = 12
turn = 1
l = ""
while turn <= 12:
    guessWord = input(
        f"Guess {turn} time (You have {turnMax - turn} turns left!): ")
    guessWord = guessWord.upper()
    i = -1
    for letter in keyword:
        i += 1
        if letter == guessWord:
            keywordPass[i] = keyword[i].upper()
    if guessWord in keywordPass:
        k = keywordPass.count(guessWord)
        if k == 1:
            print(f"There is a letter in your Word \n", *keywordPass)
        else:
            print(
                f"There are {k} {letter} letters in your Word \n", *keywordPass)
    else:
        print("That's not a good choice")
    printedWord = "".join(keywordPass)
    if printedWord == keyword:
        print("You Win!")
        result = True
        break
    turn += 1
else:
    print("Oops, you lose. Try again to get lucky! Your Word: ", keyword)
    result = False
listPlayers = [id, name, result]

import csv
with open("results.csv", "a", encoding="utf8", newline="") as f:
    data = csv.writer(f)
    data.writerow(listPlayers)

print(listPlayers)