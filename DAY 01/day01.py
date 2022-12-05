temp = 0
final = temp
sums= [0,1]
with open('input.txt', 'r') as f:
    for s in f:
        if s != '\n':
            s = s[:-1]
            temp += int(s, base=10)
        if s == '\n':
            if (temp > final) :
                final = temp
            sums.append(temp)
            temp=0
sums.sort()
print(sums)
