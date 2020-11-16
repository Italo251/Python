print('\033[40m \033[m'*51)
print('\033[1;36;40m FUNÇÃO HORÁRIA DO MOVIMENTO UNIFORMEMENTE VARIADO \033[m')
print('\033[40m \033[m'*51)
#escolhendo o que vai ser calculado:
print(' ')
print('(Para aceleração digite: 1)')
print('(Para tempo digite: 2)')
print('(Para velocidade inicial digite: 3)')
print('(Para velocidade final digite: 4)')
print(' ')
escolha = int(input('O que você quer descobrir: '))
print(' ')
#calculando a aceleração:
if escolha == 1:
    v0 = float(input('Diga-me a velocidade inicial (metros por segundo): '))
    v = float(input('Diga-me a velocidade final (metros por segundo): '))
    t0 = float(input('Diga-me o tempo inicial (segundos): '))
    t = float(input('Diga-me o tempo final (segundos): '))
    a = (v - v0) / (t - t0)
    print('A sua aceleração será de {:.2f}m/s².'.format(a))
#calculando o tempo:
if escolha == 2:
    v0 = float(input('Diga-me a velocidade inicial (metros por segundo): '))
    v = float(input('Diga-me a velocidade final (metros por segundo): '))
    a = float(input('Diga-me a aceleração (metros por segundo quadrado): '))
    t = (v - v0) / a
    print('O tempo foi de {:.2f} segundos.'.format(t))
#calculando a velocidade inicial:
if escolha == 3:
    v = float(input('Diga-me a velocidade final (metros por segundo): '))
    a = float(input('Diga-me a aceleração (metros por segundo quadrado): '))
    t = float(input('Diga-me o tempo (segundos): '))
    v0 = v - (a * t)
    print('A sua velocidade inicial é de {:.2f}m/s.'.format(v0))
#calculando a velocidade final:
if escolha == 4:
    v0 = float(input('Diga-me a velocidade inicial (metros por segundo): '))
    a = float(input('Diga-me a aceleração (metros por segundo quadrado): '))
    t = float(input('Diga-me o tempo (segundos): '))
    v = v0 + (a * t)
    print('Sua velocidade final é de {}m/s.'.format(v))
print(' ')
print('\033[40m \033[m' * 42)
print('\033[1;40;36m AGRADECEMOS POR USAR O NOSSO PROGRAMA!!! \033[m')
print('\033[40m \033[m' * 42)



