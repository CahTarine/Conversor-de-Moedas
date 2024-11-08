# Criar a janela
# Separar em dois frames
# Adicionar a barra de pesquisa e botão
# Adicionar os elementos da tela
# Fazer a integração com API

import customtkinter
from PIL import Image


import requests
from datetime import datetime
import json

import pytz
import pycountry_convert as pc

fundo_dia = "teal"
fundo_noite ="black"
fundo = fundo_dia


janela = customtkinter.CTk()
janela.geometry("320x350")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# fg_color - cor da frame / border_color - cor das bordas da frame / border_widht - tamanho da borda
frame1 = customtkinter.CTkFrame(janela,  width=320, height=50, fg_color="white", border_color="black", border_width=2).place(x=0, y=0)

frame2 = customtkinter.CTkFrame(janela,  width=320, height=300, fg_color=fundo).place(x=0, y=50)

global imagem 

# Função que passa as informações
def informacao():

    chave = "d74bcd0e6cc581c744b58566ef191229"
    cidade = barra_pesquisa.get()
    api_link = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade, chave)
   
    # fazendo a chamada da API
    r = requests.get(api_link)


    # convertendo os dados em dicionário

    dados = r.json()
    

    # divisão das linhas
    #print("*"*70)




    # Zona, País e Horas

    pais_codigo = dados['sys']['country']
    

    # Para zona - pip install pytz
    pais_zona = pytz.country_timezones[pais_codigo]
    

    # País
    pais = pytz.country_names[pais_codigo]
    
    zona = pytz.timezone(pais_zona[0])
    

    # Data e horas
    data = datetime.now(zona)
    # formatação
    data = data.strftime("%d %m %Y  |  %H:%M:%S %p")
    




    # Tempo
    tempo = dados['main']['temp']
    pressao = dados['main']['pressure']
    humidade = dados['main']['humidity']
    vento = dados['wind']['speed']
    descricao = dados['weather'][0]['description']




    # formatação da ordem de Cidade - País / Zona - pip install pycountry-convert
    # Ex: transforma o país em cod (i), transforma (i) no cod do continente, transforma cod do continente no nome do continente.

    def pais_para_continente(i):
        pais_principal = pc.country_name_to_country_alpha2(i)
        continente_codigo = pc.country_alpha2_to_continent_code(pais_principal)
        continente_nome = pc.convert_continent_code_to_continent_name(continente_codigo)

        return continente_nome



    continente = pais_para_continente(pais)

    # Passando as informações para as Labels
    l_cidade.configure(text = cidade + " - " + pais + " / " + continente)
    l_data.configure(text = data)
    l_valor.configure(text = humidade)
    l_humidade.configure(text = "Humidade")
    l_pressao.configure(text = "Pressão : " + str(pressao))
    velocidade_vento.configure(text = "Velocidade do vento : " + str(vento))
    l_descricao.configure(text = descricao)
    sinal.configure(text = "%")

    # Imagem e fundo
    periodo = datetime.now(zona)
    periodo = periodo.strftime("%H")

    global imagem

    periodo = int(periodo)

    if periodo <= 5:
        fundo=fundo_noite
        imagem = customtkinter.CTkImage(Image.open("lua.png"), size=(120, 120))
    elif periodo <= 18:
        imagem = customtkinter.CTkImage(Image.open("brilho-do-sol.png"), size=(120, 120))
        fundo=fundo_dia
    elif periodo <=23:
        imagem = customtkinter.CTkImage(Image.open("lua.png"), size=(120, 120))
        fundo = fundo_noite
    else:
        pass

    icone = customtkinter.CTkLabel(frame2, image=imagem, text=None, bg_color=fundo)
    icone.place(x=180, y=120)
            
    janela.configure(bg_color=fundo)
    frame1.configure(fg_color=fundo)
    frame2.configure(fg_color = fundo)

 # Passando as informações para as Labels
    l_cidade.configure(bg_color=fundo)
    l_data.configure(bg_color =fundo)
    l_valor.configure(bg_color =fundo)
    l_humidade.configure(bg_color =fundo)
    l_pressao.configure(bg_color =fundo)
    velocidade_vento.configure(bg_color =fundo)
    l_descricao.configure(bg_color =fundo)
    sinal.configure(bg_color =fundo)

# Elementos frame 1

barra_pesquisa = customtkinter.CTkEntry(frame1, width=200, justify='left', font=("",14), fg_color="teal")
barra_pesquisa.place(x=10, y=10)

botao = customtkinter.CTkButton(frame1, width=60, command=informacao, text='Ver clima', font=("Arial", 12), fg_color="teal")
botao.place(x=230, y=10)

# Elementos frame 2
l_cidade = customtkinter.CTkLabel(frame2, text='', anchor="center", font=("arial bold", 16), bg_color=fundo)
l_cidade.place(x=10, y=70)

l_data = customtkinter.CTkLabel(frame2, text="", anchor="center", font=("Arial", 12),bg_color=fundo)
l_data.place(x= 10, y=130)

l_valor = customtkinter.CTkLabel(frame2, text="", anchor="center", font=("Arial", 65), bg_color=fundo)
l_valor.place(x= 10, y=160)

sinal = customtkinter.CTkLabel(frame2, text="", anchor="center", font=("", 15),bg_color=fundo)
sinal.place(x=90, y=160)

l_humidade = customtkinter.CTkLabel(frame2, text="", anchor="center", font=("Arial", 11),bg_color=fundo)
l_humidade.place(x=90, y=210)

l_pressao = customtkinter.CTkLabel(frame2, text="", anchor="center", font=("Arial",11),bg_color=fundo)
l_pressao.place(x= 10, y=260)

velocidade_vento = customtkinter.CTkLabel(frame2, text="", anchor="center", font=("Arial", 11),bg_color=fundo)
velocidade_vento.place(x=10, y=300)

l_descricao = customtkinter.CTkLabel(frame2, text="", anchor="center", font=("Arial", 13),bg_color=fundo)
l_descricao.place(x=180, y=260)


janela.mainloop()