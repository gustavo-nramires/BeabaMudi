

arq = 'amostra.txt'

with open(arq, 'r+', encoding='utf-8') as fp:
    saida = ''
    cnt = 1
    linha = fp.readline()
    cnt += 1
    nova_linha = fp.readline()
    while nova_linha:
        entrada = ''
        linha = nova_linha
        nova_linha = fp.readline()
        if nova_linha:
            if nova_linha == '\n':
                for c in linha:
                    if c != '\n':
                        entrada = entrada + c
                    else:
                        if linha != '\n':
                            entrada = entrada + '\\\\' + '!' + c
                        else:
                            entrada = entrada + c
            else:
                for c in linha:
                    if c != '\n':
                        entrada = entrada + c
                    else:
                        if linha != '\n':
                            entrada = entrada + '\\\\' + c
                        else:
                            entrada = entrada + c
            saida = saida + entrada
            cnt += 1

poema_formatado = saida

with open('parte1-latex.txt', 'r+', encoding='utf-8') as p1:
    parte1 = p1.read()
with open('parte2-latex.txt', 'r+', encoding='utf-8') as p2:
    parte2 = p2.read()
with open('parte3-latex.txt', 'r+', encoding='utf-8') as p3:
    parte3 = p3.read()

autor = 'Teste'

saida = parte1 + autor + parte2 + '\n' + poema_formatado + parte3
