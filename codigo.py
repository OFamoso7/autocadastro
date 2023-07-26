import pyautogui
import time
import pandas as pd
pyautogui.PAUSE = 0.3

# passo a passo do projeto.
# passo 1: entrar no sistema da empresa.
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# -ABRIR O NAVEGADOR.
pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.click(x=879, y=392)
time.sleep(1)

# -ENTRAR NO LINK.
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)

# passo 2: logar no sistema.

# Selecionar campo do email
pyautogui.click(x=661, y=358)

# escrever o email
pyautogui.write("luidyp.monteiro@gmail.com")
# dar um tab
pyautogui.press("tab")
# escrever a senha
pyautogui.write("suasenha")
pyautogui.press("enter")
time.sleep(3)


# passo 3:  importar a base de produtos para cadastrar.

#usando PANDAS 

tabela = pd.read_csv("produtos.csv")
print(tabela)
# passo 4: cadastrar um produto.
for linha in tabela.index:

    #clicar no campo 
    pyautogui.click(x=612, y=246)
    # pegar da tabela o valor do campo que queremos preencher 
    codigo = tabela.loc[linha, "codigo"]

    # preencher o campo
    pyautogui.write(str(codigo))

    #passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # if para verificar se a coluno OBS está vazia
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")

    # enviar tabela 

    pyautogui.press("enter")

    #dar um scroll de tudo pra cima

    pyautogui.scroll(5000) #se fosse pra baixo seria (-5000)

# passo 5: repetir o processo de cadastrar o produto até o fim.
#usar TABELA.INDEX para dar todas as linhas da tabela, se fosse coluna seria TABELA.COLUMNS

