import re
import random

alphareg = re.compile(r'^[a-zA-Z]+$')
f = open('/usr/share/dict/words', 'r')
lines = f.readlines()
f.close()


def hangman(word):
    wrong = 0
    stages = ['',
              '=======',
              '|   o  ',
              '|  /|\ ',
              '|   |  ',
              '|  / \ ',
              '|      ']
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ！')

    while wrong < 6:
        i = 0
        print('ヒント', board)

        while i < 3:
            moji = input('アルファベットを一文字入力して下さい')
            if len(moji) == 1 and alphareg.match(moji):
                break
            print('入力が正しくありませんでした。')
            i += 1

        if i == 3:
            print('入力が正しくありませんでした。'
                  'ゲームを終了します。')
            break

        if moji in rletters:
            i = rletters.index(moji)
            board[i] = moji
            rletters[i] = '_'
        else:
            wrong += 1

        for i in range(wrong + 1):
            print(stages[i])

        if '_' not in board:
            win = True
            break

    if win:
        print('あなたの勝ち！{}です。'.format(word))
    else:
        print('あなたの負けです。{}でした。'.format(word))


hangman(word=lines[random.randint(1, len(lines) - 1)].strip())
