entries=[]
result=0
with open('input2.txt') as ruckstacks :
    count=0
    entry=[]
    for ruckstack  in ruckstacks:
        half1= ruckstack[:len(ruckstack)//2]
        half2= ruckstack[len(ruckstack)//2:]
        s1 = set(half1)
        s2 = set(half2)
        duplicate = s1 & s2
        common_char=duplicate.pop()
        if common_char.isupper():
            value=ord(common_char)-64+26
        else:
            value=ord(common_char)-96
        result+=value
        entries.append((s1, s2, common_char, value))
print(result)
for entry in entries:
    print(entry)
print(result)