def read_file(filename):
    lines =[]
    with open(filename,'r', encoding ='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())  
    return lines
#轉換
def convert(lines):
    new = []
    for line in lines:
        if 'Allen' in line:
            person = 'Allen'
        elif 'Tom' in line:
            person = 'Tom'
        else:
            new.append(person + ': ' + line + '\n')
    return new

#寫入
def write_file(filename, lines):
    
    with open(filename,'w', encoding ='utf-8-sig') as f:
        for line in lines:
            f.write(line)

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)
main()


