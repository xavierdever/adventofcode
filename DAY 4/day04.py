list_of_pairs=[]
f = open('input3.txt', 'r')
input=f.readlines()
count=0
for i in input:
    i = i.rstrip()
    pair1, pair2 = i.split(',')

    pair1_start, pair1_end = map(int, pair1.split('-'))
    pair2_start, pair2_end = map(int, pair2.split('-'))
    if(pair1_start <= pair2_start and pair1_end >= pair2_end) or (pair2_start <= pair1_start and pair2_end >= pair1_end):
        count+=1

print(len(list_of_pairs))
print(count)
