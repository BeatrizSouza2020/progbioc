# 1

arquivo = open('D:\Graduação\Comp 2\\tac1a.txt', 'r')

cabeçalho = ''
seq = ''

for linha in arquivo.readlines():
    if '>' in linha:
        cabeçalho += linha
        cabeçalho = cabeçalho.split('\n')[0][1:]
        print(cabeçalho)
    else:
        seq += linha.replace('\n', '')

print(cabeçalho, '\t', seq)
