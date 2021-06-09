import PySimpleGUI as sg
from random import choice

#sortiar numero secreto

lst = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
ns = choice(lst)
contador = 1

#Criar telas

def Tela_inicio():
    layout = [
        [sg.Text('Pensei em um numero entre 1 a 9.')],
        [sg.Text('Seu Chute:'), sg.Input(key='chute')],
        [sg.Button('Chutar')]
    ]
    return sg.Window('Adivinhe o Numero', layout=layout, finalize=True)

def Tela_certo():
    layout = [
        [sg.Text(f'Parabéns, Acertou com {contador} tentativas.')],
        [sg.Button('Sair')]
    ]
    return sg.Window('Acertou', layout=layout, finalize=True)

def Tela_erro():
    layout = [
        [sg.Text('Errou Tente de Novo.')],
        [sg.Text('Novo Chute:'), sg.Input(key='nChute')],
        [sg.Button('Novo Chute'), sg.Button('Sair')]
    ]
    return sg.Window('Erro', layout=layout, finalize=True)

#Mostrar Telas

janela1, janela2, janela3 = Tela_inicio(), None, None
while True:

    #condições para fechar

    window, event, values = sg.read_all_windows()
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    elif window == janela3 and event == 'Sair':
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    elif window == janela2 and event == 'Sair':
        break
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    #conferir o numero

    if window == janela1 and event == 'Chutar':
        if values['chute'] == ns:
            janela1.hide()
            janela2 = Tela_certo()
        elif values['chute'] != ns:
            if values['chute'] > ns:
                sg.popup('Chute maior que o numero secreto.')
            else:
                sg.popup('Chute menor que o numero secreto')
            janela1.hide()
            janela3 = Tela_erro()
            contador += 1

    if window == janela3 and event == 'Novo Chute':
        if values['nChute'] == ns:
            janela3.hide()
            janela2 = Tela_certo()
        if values['nChute'] != ns:
            contador += 1
            if values['nChute'] > ns:
                sg.popup('Chute maior que o numero secreto.')
            elif values['nChute'] < ns:
                sg.popup('Chute menor que o numero secreto')
