from time import sleep
from random import randint
f1 = randint(1, 5)
fl1 = randint(1, 5)
fl2 = randint(1, 5)
idb = randint(0, 1)
vida = 5
tdf = randint(1,8)
tdf1 = randint (1,8)
personagens = 'Personagem de fogo', 'Personagem de Agua', 'Personagem de terra'
caminhos = 'direita', 'esquerda', 'frente'
itens =  'bau armadilha', 'vida extra'
s = 'sim'
print('Bem vindo ao meu jogo')
n = input('Qual o seu nome? ')
print('seja muito bem vindo {}!' .format(n))
sleep(1)
e1 = input('Esta pronto para começar a melhor aventura da sua vida??: ')
if e1 == s:
    print('Opa chama no xesque, Vamos começar então!!!')
    print('você possui 5 vidas')
    sleep(1)
    print('''Escolha um atributo para seu personagem
    [ 0 ] para personagem de fogo
    [ 1 ] para personagem de agua
    [ 2 ] para personagem de terra''')
    pe = int(input('Qual sera seu personagem? '))
    print('OK, você escolheu o {}!!' .format(personagens[pe]))
    sleep(2)
    print('Que comece os jogos')
    print('Voce esta em uma floresta deserta, existem apenas 3 caminhos')
    print('''escolha uma opção de caminho
    [ 0 ] direita
    [ 1 ] esquerda
    [ 2 ] frente''')
    c = int(input('qual caminho você ira seguir '))
    print('OK, voce esta indo para {}...' .format(caminhos[c]))
    sleep(2)
    if c == 0:
        print('você encontrou um bau super raro!!!')
        ab = str(input('Deseja abrir esse bau? '))
        if ab == s:
            print('OK, abrindo bau...')
            sleep(3)
            print('você encontrou um {}' .format(itens[idb]))
            if itens[idb] == 'bau armadilha':
                print('voce foi pego pelo bau armadilha!, perca uma vida')
                vida = vida - 1
                print('voce esta com {} vidas' .format(vida))
            elif itens[idb] == 'vida extra':
                print('você adquiriu uma vida extra, uhuuu!')
                vida = vida + 1
                print('você esta com {} vidas' .format(vida))
        else:
            print('ok, continuando...')
        pr = str(input('Deseja prosseguir na sua aventura? '))
        if pr == 'sim':
            print('OK, prosseguindo...')
            sleep(2)
            print('voce se deparou com uma montanha gigante!! ')
            print('no topo da montanha possui um vida extra!!')
            sleep(1)
            print('porem pode ser perigoso escalar devido ao vento muito forte!')
            em = str(input('Deseja escalar a montanha? '))
            if em == 'sim':
                print('Ok, escalando...')
                sleep(2)
                print('\033[31mPLOFT\033[m')
                print('voce infelimente caiu devido ao vento...')
                sleep(2)
                print('perca uma vida')
                vida = vida - 1
                print('voce esta com {} vida(s)' .format(vida))
                sleep(2)
                print('vamos dar a volta na montanha...')
            else:
                print('ok vamos dar a volta na montanha entao...')
            sleep(2)
            print('voce encontrou um gurreiro alado...')
            sleep(2)
            print('nao da pra fugir dos guerreiros alados...')
            sleep(2)
            print('sua unica opcao é lutar...')
            sleep(2)
            print('\033[31mEscolha um numero de 1 a 5\033[m')
            print('esses numeros sao sorteados aleatoriamente')
            print('voce tera 2 palpites, se acertar ganhará a luta!')
            el5 = int(input('Primeiro palpite: '))
            el6 = int(input('Segundo palpite: '))
            if el5 or el6 == fl2:
                print('Voce ganhou a lutaa')
                print('Parabens, continuando aventura...')
            else:
                print('Voce perdeu a luta')
                print('Perca uma vida')
                vida = vida - 1
                print(vida)



    elif c == 1:
        print('Voce encontrou um guerreiro de agua')
        e2 = str(input('Deseja tentar fugir? ou quer lutar? '))
        if e2 == 'fugir':
            print('Voce esta tentando fugir...')
            sleep(2)
            if tdf % 2 == 1:
                print('Voce conseguiu fugir!!! parabens!!')
            elif tdf % 2 == 0:
                print('o guerreiro de agua usou jato tsunami enquanto voce estava fungindo')
                print('Perca uma vida')
                vida = vida - 1
                print('voce esta com {} vidas' .format(vida))
        else:
            print('\033[31mEscolha um numero de 1 a 5\033[m')
            print('esses numeros sao sorteados aleatoriamente')
            print('voce tera 2 palpites, se acertar ganhará a luta!')
            el1 = int(input('Primeiro palpite: '))
            el2 = int(input('Segundo palpite: '))
            if el1 or el2 == f1:
                print('Voce ganhou a lutaa')
                print('Parabens, continuando aventura...')
            else:
                print('Voce perdeu a luta')
                print('Perca uma vida')
                vida = vida - 1
                print(vida)
    elif c == 2:
        print('voce encontrou um guerreiro de fogo!!')
        e3 = str(input('Deseja tentar fugir? ou quer enfrentar o bunda mole? '))
        if e3 == 'fugir':
            print('Voce esta tentando fugir...')
            sleep(2)
            if tdf1 % 2 == 1:
                print('Voce conseguiu fugir!!! parabens!!')
            elif tdf1 % 2 == 0:
                print('o guerreiro de agua usou jato tsunami enquanto voce estava fungindo')
                print('Perca uma vida')
                vida = vida - 1
                print('voce esta com {} vidas'.format(vida))
        else:
            print('\033[31mEscolha um numero de 1 a 5\033[m')
            print('esses numeros sao sorteados aleatoriamente')
            print('voce tera 2 palpites, se acertar ganhará a luta!')
            el3 = int(input('Primeiro palpite: '))
            el4 = int(input('Segundo palpite: '))
            if el3 or el4 == fl1:
                print('Voce ganhou a lutaa')
                print('Parabens, continuando aventura...')
            else:
                print('Voce perdeu a luta')
                print('Perca uma vida')
                vida = vida - 1
                print(vida)
else:
    print('ok, voce nao esta pronto ainda')
