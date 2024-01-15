import tkinter as tk
#o que a bibliotecar tkinter tem a oferecer?
#pelo oque vi é uma biblioteca de interface grafica que oferece um padrão de desing para programas funcionais
#use Label(qual é a janela, text: texto para inserir) para incluir texto na janela
def calcular(expressao):
    try:
        resultado = eval(expressao)
        campo_texto.set(resultado)
        #em quais outros casos eu posso usar "eval" e ".set"?
    except:
        campo_texto.set("Erro")

janela = tk.Tk()
janela.title("Calculadora do balacobaco")
#funciona dando um titulo a janela
janela.geometry("300x300")
campo_texto = tk.StringVar()

entrada_texto = tk.Entry(janela, textvariable=campo_texto)
entrada_texto.grid(row=0, column=0, columnspan=4, padx=90, pady=90)
#como funciona tk.Entry?

botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

linha = 1
coluna = 0
for botao in botoes:
    tk.Button(janela, text=botao, width=10, command=lambda botao=botao: campo_texto.set(campo_texto.get() + botao) if botao != "=" else calcular(campo_texto.get())).grid(row=linha, column=coluna)
    #tk.Button oferece butões padrão?
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

def pressiona_tecla_1(event):
    campo_texto.set(campo_texto.get() + '1')

janela.bind('1', pressiona_tecla_1)
#veremos mais detalhes sobre o chamado .bind
janela.mainloop()
#e o que significa essa finalização?
#significa que mantem a jenala aberta caso contrario o comando janela.bind iria só abrir e fechar em seguida 