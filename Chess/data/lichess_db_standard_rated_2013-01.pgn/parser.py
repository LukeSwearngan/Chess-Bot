f = open("lichess_db_standard_rated_2013-01.pgn")
f = f.read().split('\n')
mod = 16
flag = False
final = ""
for i in range(len(f)):
        #print(f[i])
        if (not (f[i] == '')):
            if f[i][0] == '1':
                final += f[i] + "\n"
file = open("Output.pgn", "w")
file.write(final)