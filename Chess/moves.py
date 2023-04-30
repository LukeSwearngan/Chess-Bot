with open('num', 'r') as f:
    fil = f.read().split(']')
    fil[0] = fil[0][1:].split('[')[1][:-12]
    board = [[],[],[],[],[],[],[],[],[]]
    black = False
    level = 0
    count = 0
    for i in range(len(fil[0])):
        if fil[0][i] == '1':
            if len(fil) == i+1 and fil[0][i+1] == 0:
                pass
            elif black:
                pass
            else:
                count += 1
                board[level].append('w ')
                if count == 8:
                    level += 1
        elif fil[0][i] == '5':
            pass
        elif fil[0][i] == '3':
            pass
        elif fil[0][i] == '9':
            pass
        elif fil[0][i] == '0':
            pass
        elif fil[0][i] == '-':
            pass

print(board)