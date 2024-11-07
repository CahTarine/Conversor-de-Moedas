# Criar janela
# Título - Conversor de moedas
# Campo para selecinar moeda de origem (lista) com label
# Campo para selecionar moeda de destino (lista) com label
# Botão para converter
# Lista para pesquisar nome das moedas

import customtkinter
from pegar_moedas import nomes_moedas, combinacoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

# Criar e configurar janela 

# Cores da janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
# Criação
janela = customtkinter.CTk()
janela.geometry("400x400")

dic_combinacoes_disponiveis = combinacoes_disponiveis()

# Criar botões, textos e outros elementos
titulo = customtkinter.CTkLabel(janela, text="CONVERSOR DE MOEDAS", font=("Arial", 20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("", 17))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("", 17))

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_combinacoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_combinacoes_disponiveis.keys()), command=carregar_moedas_destino)

campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"])

# Keys: em python, pega todas as chaves do dicionario.


def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")




botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

# Lista de pesquisa
lista_moedas = customtkinter.CTkScrollableFrame(janela)

#moeda1 = customtkinter.CTkLabel(lista_moedas, text="USD: Dólar americano")
#moeda2 = customtkinter.CTkLabel(lista_moedas, text="BRL: Real brasileiro")
#moeda3 = customtkinter.CTkLabel(lista_moedas, text="EUR: Euro europeu")
#moeda1.pack()
#moeda2.pack()
#moeda3.pack()

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")


moedas_disponiveis = nomes_moedas()
{"BRL" : "Real Brasileiro", "USD" : "Dólar Americano"}
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda} : {nome_moeda}")
    texto_moeda.pack()

# Colocar todos os elementos na janela

# Espaçamento entre um elemento e outro
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)

texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)

botao_converter.pack(padx=10, pady=10)

texto_cotacao_moeda.pack(padx=10, pady=10)

lista_moedas.pack(padx=10, pady=10)

# Rodar a janela
janela.mainloop()
