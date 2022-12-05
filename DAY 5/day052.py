import re
import pandas as pd
f = open('input2.txt', 'r')
input=f.readlines()

stack=[["N", "R", "G", "P"],
        ["J","T","B","L","F","G","D","C"],
        ["M","S","V"],
        ["L", "S", "R", "C", "Z", "P"],
        ["P","S","L","V","C","W","D","Q"],
        ["C", "T", "N", "W", "D", "M", "S"],
        ["H", "D", "G", "W", "P"],
        ["Z", "L", "P", "H", "S", "C", "M", "V"],
        ["R", "P", "F", "L", "W", "G", "Z"]]

orders=input[10:]
for order in orders :
    split=order.split(" ")
    order_count, order_src, order_dest = map(int, (split[1], split[3], split[5]))
    for i in range(-order_count, 0):
        stack[order_dest-1].append(stack[order_src-1].pop(i))
#print(order)
result=""
print(*stack, sep="\n")
for i in range(len(stack)):
    result += str(stack[i][-1])
print(result)