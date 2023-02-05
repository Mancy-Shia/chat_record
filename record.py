def read_file(filename):
    lines =[]
    with open(filename,'r', encoding ='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())  
    return lines
#轉換
def convert(lines):
    s_wc = 0
    s_sc = 0
    h_wc = 0
    h_sc = 0
    person = None
    for line in lines:
        s = line.split(' ')
        if len(s)<=1:
            if name == 'Su,Chuan-Yun':
                for m in s:
                    s_wc += len(m)
            elif name == '海芳':
                for m in s:
                    h_wc += len(m)
        elif s[1] == '海芳':
            name = s[1]
            if s[2] == '貼圖':
                h_sc += 1
            else:
                for m in s[2:]:
                    h_wc += len(m)
        elif s[1] == 'Su,Chuan-Yun':
            name = s[1]
            if s[2] == '貼圖':
                s_sc += 1
            else:
                for m in s[2:]:
                    s_wc += len(m)
        else:
            if name == 'Su,Chuan-Yun':
                for m in s:
                        s_wc += len(m)
            elif name == '海芳':
                for m in s:
                        h_wc += len(m)
    print('海芳傳了:', h_wc, '個字,', h_sc, '個貼圖')
    print('Su,Chuan-Yun傳了:', s_wc, '個字,', s_sc, '個貼圖')

#寫入
def write_file(filename, lines):
    
    with open(filename,'w', encoding ='utf-8-sig') as f:
        for line in lines:
            f.write(line)

def main():
    lines = read_file('input.txt')
    convert(lines)
    
main()


