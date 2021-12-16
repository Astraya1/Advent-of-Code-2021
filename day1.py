report = open("day1.txt", "r").readlines()
for i,number in enumerate(report):
        report[i] = number.rstrip('\n')
        report[i] = int(number)

def part1():
    count = 0

    for i,number in enumerate(report):
        if report[i]>report[i-1]:
            count+=1

    print(count)

def part2():
    count = 0

    for i, number in enumerate(report):
        if i<=(len(report)-4):
            if (report[i]+report[i+1]+report[i+2]) < (report[i+1]+report[i+2]+report[i+3]):
                count+=1
    print(count)

part1()
part2()
