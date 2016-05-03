'''
Created on 2016年5月2日

@author: huangshuai
'''
# col:55 -> BC
def change1(col):
    K = []
    while(col > 0):
        yu = col % 26
        if yu == 0:
            col = col - 1
            K.append(26)
        else:
            K.append(yu)
        col = (col // 26)  
    K.reverse()
    return K

# col:BC -> 55 
def change2(col):
    sum = 0
    col = col[::-1]
    for index in range(len(col)):
        sum += (ord(col[index]) - 64) * (26 ** index)  
    return sum

def chk(s):
    if s[0] == 'R' and s[1].isdigit():
        i = 2
        while i < len(s):
            if s[i] == 'C':
                return True
            i += 1
    return False

n = int(input())
for l in range(n):
    i = input()
    
    # R23C55 -> BC23
    if chk(i):
        col = int(i[i.index('C') + 1:])  # 55
        row = int(i[1:i.index('C')])  # 23
        # ord('A') = 65   chr(65) = 'A'
        result = ''
        for k in change1(col):
            result += chr(k + 64)
        result += str(row)
        print(result)
    else:
        col = ''
        row = ''
        for j in range(len(i)):
            if ord(i[j]) > 64:
                col += i[j]
            else:
                row += i[j]
        col = str(change2(col))
        result = 'R' + row + 'C' + col
        print(result)

            
        
