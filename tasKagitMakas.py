import random

def play ():
    user = input("Seçiminizi belirtin\n Taş için 'T', Kağıt için'K', Makas için 'M'\n")
    print("Seçiminiz:", user)

    computer = random.choice(['t', 'k', 'm'])
    print("Bilgisayarın Seçimi: ", computer)

    if user == computer:
        return "Berabere"
    elif kazanmaSarti(user, computer):
        return 'Kazandın!'
    else:
        return 'Kaybettin!'

def kazanmaSarti (player, opponent):
    if (player == 't' and opponent == 'm') or (player == 'm' and opponent == 'k') or (player == 'k' and opponent == 't'):
        return True

while True:
    result = play()
    print(result)

    tekrar = input("Tekrar oynamak için 'R' tuşuna basın, çıkmak için herhangi bir tuşa basın: ")
    if tekrar.lower() != 'r':
        break