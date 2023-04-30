fil = open('example.txt')

for i in fil.read().split('\n'):
    l = [['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''], ]
    count = 0
    count2 = 0
    flag = True
    for j in i:
        if flag:
            if j == 'r':
                l[count2][count] = 'bR'
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j == 'n':
                l[count2][count] = 'bN'
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j == 'b':
                l[count2][count] = 'bB'
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j == 'q':
                l[count2][count] = 'bQ'
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j == 'k':
                l[count2][count] = 'bK'
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j == 'p':
                l[count2][count] = 'b '
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j == 'R':
                l[count2][count] = 'wR'
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j == 'N':
                l[count2][count] = 'wN'
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j == 'B':
                l[count2][count] = 'wB'
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j == 'Q':
                l[count2][count] = 'wQ'
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j == 'K':
                l[count2][count] = 'wK'
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j == 'P':
                l[count2][count] = 'w '
                if count >= 7:
                    count = 0
                    count2 += 1
                else:
                    count += 1
            if j.isnumeric():
                for i in range(int(j)):
                    l[count2][count] = ''
                    if count >= 7:
                        count = 0
                        count2 += 1
                    else:
                        count += 1
            print(l)
            if j == ' ':
                flag = False
        elif j == 'f':
            flag = True
        #print(count)