def game():
    return 65
score=game()
with open("highscore.txt", "r") as f:
    highscore= int(f.read())

if score>highscore:
    with open("highscore.txt", "w") as f:
        f.write(str(score))