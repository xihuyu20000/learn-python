writer = open('大文件.csv', 'w', encoding='utf-8')

for i in range(30):
    with open('350MB大文件.csv', encoding='utf-8') as f:
        lines = f.readlines()

        if i == 0:
            writer.writelines(lines)
        else:
            writer.writelines(lines[1:])
        writer.write('\r\n')
        writer.flush()
writer.close()
