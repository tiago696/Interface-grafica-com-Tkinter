'''Objetivo fazer um sistema de login'''



# Importando a blibioteca

from tkinter import *
from time import sleep


# dicionarios

lista_que_recebe_email = []
lista_que_recebe_senha = []
email = {'Email': ''}
senha = {'Senha': ''}


# Funções da janela

def new_screen():
    
    # --------------------------------------------------------------------

    # Codigo da janela 
    
    new_screen_variavel = Tk()
    new_screen_variavel.title('Login_cadastrado')
    new_screen_variavel.geometry('801x405')
    
    # --------------------------------------------------------------------

    # Caixinha de texto
    
    O_seu_cadastro_foi_feito = Label(new_screen_variavel, text='Parabens! Seu cadastro foi efetuado com sucesso.', font= ('Calibri', 15))
    O_seu_cadastro_foi_feito.place(x=180, y=40)
    
    msg_de_aviso_sobre_o_local_de_salvamento_do_cadastro = Label(new_screen_variavel, text='O seu cadastro foi salvo no arquivo cujo o nome é: "Salvar login"', font= ('Calibri', 15)) 
    msg_de_aviso_sobre_o_local_de_salvamento_do_cadastro.place(x=120, y=70)

    # --------------------------------------------------------------------

    # Importando a imagem 
    
    senhor_incrivel_meme = PhotoImage(file='Meme senhor incrivel.png')
    
    
    img = Label(new_screen_variavel, image= senhor_incrivel_meme)
    img.place(x=165,y=100)
    
    
    new_screen_variavel.mainloop()
    
    

def salvar_login():
    email_dict_append = caixinha_de_texto_email.get()
    senha_dict_append =  caixinha_de_texto_senha.get()
    
    email['Email'] = email_dict_append
    senha['Senha'] = senha_dict_append
        
    arquivo = open('Salvar_login.txt','at')
    arquivo.write(f"[ E-MAIL: {email['Email']},")
    arquivo.close()
    
    arquivo_senha = open('Salvar_login.txt','at')
    arquivo_senha.write(f" Senha: {senha['Senha']} ], ")
    sleep(0.5)
    msg = 'E-mail e senha salvos!'
    email_e_senha_salvos['text'] = msg
    

def Entrar():
   # Abaixo a duas listas acima recebem os dois dicionarios contendo o e-mail e senha
    lista_que_recebe_email.append(email)
    lista_que_recebe_senha.append(senha)
    print(lista_que_recebe_email[0],lista_que_recebe_senha[0])
    
    # No codigo abaixo fica a parte onde o programa analisa se os dois campos(e-mail e senha) estão preenchidos
    if lista_que_recebe_email[0]== {'Email': ''}:
        if lista_que_recebe_senha[0] == {'Senha': ''}:
            # Agora tem que se fazer com que a janela mostre a informação do print abaixo se quiser
            msg = 'Por favor bote seus dados nos campos acima e clique em "Salvar login" para se cadastrar.'
            Aviso_sobre_os_dados_corretamente['text'] = msg
            
            
            
            
            
           
    # Se estiverem preenchidos e foi feito o salvamento do cadastro o programa continua 
    # A janela so vai ser destruida  se houver uma informação nas duas caixinhas de e-mail e senha 
    else:
        print('Ola')
        janela.destroy()
        sleep(0.5)
        new_screen()
        
        
        
        
        
# --------------------------------------------------------------------   
     
# Programa Prinpal

# --------------------------------------------------------------------

# Codigo da janela
janela = Tk()
janela.geometry('801x405')
janela.title('Sistema de login')

# --------------------------------------------------------------------

# Importando Imagens  

imagem_de_fundo = PhotoImage(file='Interface gráfica de login.png')
Botão_entrar_fazer_login = PhotoImage(file='Botão.png')
Botão_salvar_login = PhotoImage(file='Botão de Salvar login.png')
# --------------------------------------------------------------------
# Imagem de fundo

img_de_fundo = Label(janela, image= imagem_de_fundo)
img_de_fundo.pack()

# --------------------------------------------------------------------

# Botões da janela

Botão_de_login_entrar_primeiro_botão = Button(janela, image= Botão_entrar_fazer_login, command= Entrar)
Botão_de_login_entrar_primeiro_botão.place(width=131, height=40, x=426, y=310)

Botão_de_salvar_login_segundo_botão = Button(janela, image=Botão_salvar_login, command= salvar_login)
Botão_de_salvar_login_segundo_botão.place(width=173, height=40, x=239, y=310)

# --------------------------------------------------------------------

# Caixinhas de texto

caixinha_de_texto_email = Entry(janela, bd= 2, font=('Calibri', 15), justify=CENTER)
caixinha_de_texto_email.place(width= 318, height= 38, x=239, y= 192)

caixinha_de_texto_senha = Entry(janela, bd= 2, font=('Calibri', 15), show='*', justify=CENTER)
caixinha_de_texto_senha.place(width= 318, height= 38, x=239, y= 255)

email_e_senha_salvos = Label(janela,text='',font=('Belleza',10) ,background='light blue', fg='blue')
email_e_senha_salvos.place(x=239,y=355)

Aviso_sobre_os_dados_corretamente = Label(janela, text='',font=('Belleza',10) ,background='light blue', fg='red')
Aviso_sobre_os_dados_corretamente.place(x=239, y=380)
# --------------------------------------------------------------------

janela.mainloop()
