inputs = open("day4input.txt").readlines()

for i, value in enumerate(inputs):
    inputs[i] = value.rstrip('\n')

bingonumbers = []

for i, value in enumerate(inputs):
    if value != '':
        bingonumbers.extend(value.split(','))
    else:
        del inputs[:i+1]
        break

for i, value in enumerate(bingonumbers):
    bingonumbers[i] = int(value)

bingoboards = [[[]]*5]*(int((len(inputs)+1)/6))

boardcount = 0
linecount = 0

print(inputs)
for i, line in enumerate(inputs):
    if (i+1)%6 == 0:
        boardcount += 1
        print('ASDFASDF')
    else:
        bingoboards[bingoboards].append(line.split())         

print(bingoboards)