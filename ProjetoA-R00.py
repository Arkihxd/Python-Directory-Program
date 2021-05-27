import os
import shutil
import logging as log

terminou = False
caminho = ""

while (not terminou):

    print("Organizador Automatico de Arquivos")
    print("")
    print("1. Renomear arquivos conforme ano e quantidade escolhida.")
    print("2. Criar novas subpastas divididas por ano.")
    print("3. Mover arquivos entre pasta pricipal e subpastas")

    caso = int(input(""))

    log.basicConfig(filename="Diario_Execução_Proj-A.log", level=log.INFO, format="%(asctime)s %(levelname)s %(funcName)s => %(message)s")
   
    if (caso == 1):
        arquivos = os.listdir()
        ano_inicial = int(input("Digite o ano inicial: "))
        quantidade_arquivos = int(input("Digita a quantidade de arquivos que seja renomear: "))
        i = 1
        for arquivo in (arquivos):
            if (arquivo != 'Diario_Execução_Proj-A.log' ):
                destino = caminho + str(ano_inicial) + "_0" + str(i)
                fonte = caminho + arquivo
                os.rename(fonte, destino) 
            else:
               break;
                
            if (i / quantidade_arquivos) == 1:
                ano_inicial += 1
                i = 1
            else:
                i += 1 
            
            log.info("Renomeou os arquivos em: " + fonte)
        
        resposta = input("Deseja continuar? (s) ou (n) ")
        if resposta == "n" or resposta == "N":
            terminou = True
             
    if (caso == 2):
        ano_inicial = int(input("Digite o ano inicial:"))
        quantidade_pastas = int(input("Digite a quantidade de pastas que voce deseja:"))
        for i in range(quantidade_pastas):
            caminho_novas_pastas = caminho + str(ano_inicial + i)
            os.mkdir(caminho_novas_pastas)
            log.info("Criou pasta em: " + caminho_novas_pastas)
            
        resposta = input("Deseja continuar? (s) ou (n) ")
        if resposta == "n" or resposta == "N":
            terminou = True
        
    if (caso == 3):
        nome_pasta = input("Digite o ano da pasta destino: ")
        arquivos = os.listdir()
        for nome_arquivo in (arquivos):
            if nome_arquivo[0:4] == nome_pasta:
                origem = caminho + nome_arquivo
                destino = caminho + nome_pasta
                shutil.move (origem, destino)
                log.info("Moveu arquivos para: " + destino)     
                
        resposta = input("Deseja continuar? (s) ou (n) ")
        if resposta == "n" or resposta == "N":
            terminou = True
