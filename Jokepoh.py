import emoji
import random
print('{}'.format('#' * 30))
print('{:^30}'.format('JOGO: JOKENPO!'))
print('{}'.format('#' * 30))
tesoura = emoji.emojize(':v:',use_aliases=True)
pedra = emoji.emojize(':punch:',use_aliases=True)
papel = emoji.emojize(':hand:',use_aliases=True)
usuario = int(input('''VAMOS COMEÇAR
[1] PARA {} PEDRA
[2] PARA {} PAPEL
[3] PARA {} TESOURA
'''.format(pedra,papel,tesoura)))
lista = [pedra,papel,tesoura]
computador = random.choice(lista)
if usuario == 1:
    usuario = pedra
    print('VOCÊ:{}'.format(usuario))
    print('COMPUTADOR:{}'.format(computador))
    if computador == tesoura:
       print('WOWWW, VOCÊ VENCEU!!')
    elif computador == papel:
        print('HEHE, EU VENCI!!')
    else:
        print('HAHA, ACHO QUE ISSO FOI UM EMPATE?!')
elif usuario == 2:
    usuario = papel
    print('VOCÊ:{}'.format(usuario))
    print('COMPUTADOR:{}'.format(computador))
    if computador == pedra:
        print('YOU WIM HAHA, VOCÊ VENCEU HEHE...')
    elif computador == tesoura:
        print('HEHE, EU GANHEI ACHO QUE NÃO É SEU DIA DE SORTE...')
    else:
        print('HMMMM, UM EMPATE!!')
elif usuario == 3:
    usuario = tesoura
    print('COMPUTADOR:{}'.format(computador))
    print('VOCÊ:{}'.format(usuario))
    if computador == papel:
        print('OOOUUU, VOCÊ GANHOU!!')
    elif computador == pedra:
        print('YEHA, EU GANHEI!!')
    else:
        print('HAHA, EMPATE!!')
else:
    print('OPÇÃO DIGITADA IVALIDA!!TENTE NOVAMENTE!!')