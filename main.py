import os
import requests
import json

global meusjogos, megaSena, lotoFacil, quina, lotoMania, timeMania, duplaSena, diaDeSorte, superSete
global sorteadosMegaSena, sorteadosLotoFacil, sorteadosQuina, sorteadosLotoMania, sorteadosTimeMania, sorteadosDuplaSena, sorteadosDiaDeSorte, sorteadosSuperSete

# Meus Jogos
meusjogos = list()
megaSena = list() 
lotoFacil = list()
quina = list()
lotoMania = list()
timeMania = list()
duplaSena = list() 
diaDeSorte = list() 
superSete = list()

# Sorteios da Caixa
sorteadosMegaSena = []
sorteadosLotoFacil = list() 
sorteadosQuina = list() 
sorteadosLotoMania = list() 
sorteadosTimeMania = list() 
sorteadosDuplaSena = list() 
sorteadosDiaDeSorte = list()
sorteadosSuperSete = list()



def pegaResultadoLoteriasAPI(loteria):
    
    request = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/{loteria}/latest")
    
    resultado = json.loads(request.content)

    setNumerosSorteadosList(resultado['dezenas'], loteria)
    #sorteadosMegaSena.append()
    print(sorteadosMegaSena)
    print(sorteadosLotoFacil)
    

    print(f"-=-=-=-=-= Loteria: {resultado['nome']} -=-=-=-=-=" )
    print(f"---------------------------------------------------")
    print(f"Nº Concurso:                    {resultado['concurso']}")
    print(f"Data:                           {resultado['data']}")
    print(f"Local Sorteio:                  {resultado['local']}")
    print(f"Dezenas Sorteadas: {resultado['dezenas']}")
    print(f"---------------------------------------------------")

    
    for res in resultado['premiacoes']:

        print(f"Acertos:                    {res['acertos']}")
        print(f"Vencedores:                 {res['vencedores']}")
        print(f"Premio:                     {res['premio']}")
        print(f"---------------------------------------------------")


    print(f"Acumulado:                      {'Sim' if resultado['acumulou'] else 'Não'}")
    print(f"Acumulado Próx. concurso:       {resultado['acumuladaProxConcurso']}")
    print(f"Data Próx. concurso:            {resultado['dataProxConcurso']}")
    print(f"Nº Próx. Concurso:              {resultado['proxConcurso']}")
    print("----------------------------------------------------")


def setNumerosSorteadosList(dezenas, tipoLoteria):
    print(dezenas, tipoLoteria)
    novaLista = [int(n) for n in dezenas]
    
    match tipoLoteria:
        case "mega-sena":
            sorteadosMegaSena.clear()
            sorteadosMegaSena.append(novaLista)
        case "lotofacil":
            sorteadosLotoFacil.clear()
            sorteadosLotoFacil.append(novaLista)
        case "quina":
            sorteadosQuina.clear()
            sorteadosQuina.append(novaLista)
        case "lotomania":
            sorteadosLotoMania.clear()
            sorteadosLotoMania.append(novaLista)
        case "timemania":
            sorteadosTimeMania.clear()
            sorteadosTimeMania.append(novaLista)
        case "dupla-sena":
            sorteadosDuplaSena.clear()
            sorteadosDuplaSena.append(novaLista)
        case "dia-de-sorte":
            sorteadosDiaDeSorte.clear()
            sorteadosDiaDeSorte.append(novaLista)
        case "super-sete":
            sorteadosSuperSete.clear()
            sorteadosSuperSete.append(novaLista)


def listarResultado(tipo):
    loteria = []
    match tipo:
        case "mega-sena":
            loteria = sorteadosMegaSena
        case "lotofacil":
            loteria = sorteadosLotoFacil
        case "quina":
            loteria = sorteadosQuina
        case "lotomania":
            loteria = lotoMania
        case "timemania":
            loteria = sorteadosTimeMania
        case "dupla-sena":
            loteria = sorteadosDuplaSena
        case "dia-de-sorte":
            loteria = sorteadosDiaDeSorte
        case "super-sete":
            loteria = sorteadosSuperSete

    
    if len(loteria) == 0:
        print(f"ERRO! Você ainda não viu o resultado da {tipo}.\n\n\n\n\n")
        return
    
    conta = 1
    print(f"-=-=-=-=-= Resultados(s) da {tipo} -=-=-=-=-= ")
    for aposta in loteria:
        print(f"Aposta {conta}", end=" : ")
        for numero in sorted(aposta):
            print(f"- {numero}", end=" ")
        
        print()
        conta += 1
    
    conta = 1


def visualizarTodasAsApostas():
    for tipo in range(1, 9):
        visualizarApostas(tipo)


def visualizarApostas(tipo):
    loteria = []
    match tipo:
        case 1:
            tipo = "Mega Sena"
            loteria = megaSena
        case 2:
            tipo = "Loto Fácil"
            loteria = lotoFacil
        case 3:
            tipo = "Quina"
            loteria = quina
        case 4:
            tipo = "Loto Mania"
            loteria = lotoMania
        case 5:
            tipo = "Time Mania"
            loteria = timeMania
        case 6:
            tipo = "Dupla Sena"
            loteria = duplaSena
        case 7:
            tipo = "Dia de Sorte"
            loteria = diaDeSorte
        case 8:
            tipo = "Super Sete"
            loteria = superSete

    
    if len(loteria) == 0:
        print(f"ERRO! Você não fez nenhuma aposta na {tipo}.\n\n\n\n\n")
        return
    
    conta = 1
    print(f"-=-=-=-=-= Aposta(s) na {tipo} -=-=-=-=-= ")
    for aposta in loteria:
        print(f"Aposta {conta}", end=" : ")
        for numero in sorted(aposta):
            print(f"- {numero}", end=" ")
        
        print()
        conta += 1
    
    conta = 1



#def visualizaNumerosSorteados(numerosSorteados):
#
#    #if len(numerosSorteados) == 0:
#    #    print("ERRO! Você não inseriu as Dezenas Sorteadas.\n\n\n\n\n")
#    #    return
#    
#    print(f"Números Sorteados : ", end=" ==> ")
#    for numero in sorted(numerosSorteados):
#        print(f"- {numero}", end=" ")
#    
#    print("\n") 
#    print("-="*30)
   

def insereApostas():
    while True:
        print("-=-=-= Escolha qual Loteria você quer apostar -=-=-=-=")
        print("1. Mega Sena")
        print("2. Loto Fácil")
        print("3. Quina")
        print("4. Loto Mania")
        print("5. Time Mania")
        print("6. Dupla-Sena")
        print("7. Dia-de-Sorte")
        print("8. Super Sete")
        print("0. Retornar ao Menu Principal")

        opcao = input("Opção: 1-2-3-4-5-6-7-8-9 ou 0 pra retornar ao Menu Principal")
        os.system("clear")

        if opcao.isnumeric():
            match opcao:
                case "0":
                    print("0. Retornar ao Menu Principal.\n\n\n\n\n")
                    break

                # Escolhendo qtde de dezenas

                case "1":
                    while True:
                        print("1. Mega Sena")
                        numDezenas = input("Insira o número de Dezenas que você quer jogar na Mega Sena: 6-15.")
                        if numDezenas.isnumeric():
                            if int(numDezenas) >= 6 and int(numDezenas) <= 15:
                                jogar(1, int(numDezenas))
                                break

                            else:
                                print("ERRO! Você pode jogar de 6 até 15 dezenas na MegaSena")
                        else:
                            print("ERRO! Valor inválido.")

                case "2":
                    while True:
                        print("2. Loto Fácil")
                        numDezenas = input("Insira o número de Dezenas que você quer jogar na Loto Fácil: 15-18.")
                        if numDezenas.isnumeric():
                            if int(numDezenas) >= 15 and int(numDezenas) <= 18:
                                jogar(2, int(numDezenas))
                                break

                            else:
                                print("ERRO! Você pode jogar de 15 até 18 dezenas na Loto Fácil")
                        else:
                            print("ERRO! Valor inválido.")
                    
                    
                case "3":
                    while True:
                        print("3. Quina")
                        numDezenas = input("Insira o número de Dezenas que você quer jogar na Quina: 5-15.")
                        if numDezenas.isnumeric():
                            if int(numDezenas) >= 5 and int(numDezenas) <= 15:
                                jogar(3, int(numDezenas))
                                break

                            else:
                                print("ERRO! Você pode jogar de 5 até 15 dezenas na Quina")
                        else:
                            print("ERRO! Valor inválido.")


                case "4":
                    print("4. Loto Mania")
                    print("Na Loto Mania você pode escolher 50 dezenas.")
                    
                    numDezenasLotoMania = 50
                      
                    jogar(4, numDezenasLotoMania)
                    

                      
                case "5":
                    print("5. Time Mania")
                    print("Na Time Mania você pode escolher 20 dezenas")

                    numDezenasTimeMania = 20

                    jogar(5, numDezenasTimeMania)


                case "6":
                    while True:
                        print("6. Dupla Sena")    
                        numDezenas = input("Insira o número de Dezenas que você quer jogar na Quina: 6-15.")
                        if numDezenas.isnumeric():
                            if int(numDezenas) >= 6 and int(numDezenas) <= 15:
                                jogar(6, int(numDezenas))
                                break

                            else:
                                print("ERRO! Você pode jogar de 6 até 15 dezenas na Dupla Sena")
                        else:
                            print("ERRO! Valor inválido.")


        
                case "7":
                    while True:
                        print("7. Dia de Sorte")    
                        numDezenas = input("Insira o número de Dezenas que você quer jogar na Quina: 7-15.")
                        if numDezenas.isnumeric():
                            if int(numDezenas) >= 7 and int(numDezenas) <= 15:
                                jogar(7, int(numDezenas))
                                break

                            else:
                                print("ERRO! Você pode jogar de 7 até 15 dezenas na Dia de Sorte")
                        else:
                            print("ERRO! Valor inválido.")


                case "8":
                    while True:
                        print("8. Super Sete")    
                        numDezenas = input("Insira o número de Dezenas que você quer jogar na Super Sete: 7-21.")
                        if numDezenas.isnumeric():
                            if int(numDezenas) >= 7 and int(numDezenas) <= 21:
                                jogar(8, int(numDezenas))
                                break

                            else:
                                print("ERRO! Você pode jogar de 7 até 21 dezenas na Super Sete")
                        else:
                            print("ERRO! Valor inválido.")


                case _:
                    print("Opção Inválida")
        else:
            print("Valor inválido.")


def jogar(loteria, numDezenas):
    match loteria:
        case 1:
            print(f"1. Mega Sena - {numDezenas} dezenas de 1 a 60.")
            conta = 0
            meuJogo = []
            
            while conta < numDezenas:
                dezena = input(f"Digite a Dezena: {conta + 1} de {numDezenas}: ")
                os.system("clear")
        
                if dezena.isnumeric():
                    if int(dezena) >= 1 and int(dezena) <= 60:
                        if int(dezena) not in meuJogo:
                            meuJogo.append(int(dezena))
                            print(f"Dezena {dezena} inserida:")
                            print(f"{meuJogo}")
                            conta += 1
        
        
                            if len(meuJogo) == numDezenas:
                                megaSena.append(meuJogo)
                                meuJogo = []
                                visualizarApostas(1)
                                break
                            
                                    
                        else:
                            print(f"ERRO! Você já inseriu a dezena {dezena}.\n\n\n\n\n")
                    
                    else:
                        print("ERRO! A Mega Sena só contempla números entre 1 a 60.\n\n\n\n\n")
                else:
                    print("Dezena Inválida!\n\n\n\n\n")
            
        case 2:
            print(f"2. Lotofácil - {numDezenas} dezenas de 1 a 25.")
            conta = 0
            meuJogo = []
            
            while conta < numDezenas:
                dezena = input(f"Digite a Dezena: {conta + 1} de {numDezenas}: ")
                os.system("clear")
        
                if dezena.isnumeric():
                    if int(dezena) >= 1 and int(dezena) <= 25:
                        if int(dezena) not in meuJogo:
                            meuJogo.append(int(dezena))
                            print(f"Dezena {dezena} inserida:")
                            print(f"{meuJogo}")
                            conta += 1
        
        
                            if len(meuJogo) == numDezenas:
                                lotoFacil.append(meuJogo)
                                meuJogo = []
                                visualizarApostas(2)
                                break
                            
                                    
                        else:
                            print(f"ERRO! Você já inseriu a dezena {dezena}.\n\n\n\n\n")
                    
                    else:
                        print("ERRO! A Loto Fácil só contempla números entre 1 a 25.\n\n\n\n\n")
                else:
                    print("Dezena Inválida!\n\n\n\n\n")

        case 3:
            print(f"3. Quina - {numDezenas} dezenas de 1 a 80.")
            conta = 0
            meuJogo = []
            
            while conta < numDezenas:
                dezena = input(f"Digite a Dezena: {conta + 1} de {numDezenas}: ")
                os.system("clear")
        
                if dezena.isnumeric():
                    if int(dezena) >= 1 and int(dezena) <= 80:
                        if int(dezena) not in meuJogo:
                            meuJogo.append(int(dezena))
                            print(f"Dezena {dezena} inserida:")
                            print(f"{meuJogo}")
                            conta += 1
        
        
                            if len(meuJogo) == numDezenas:
                                quina.append(meuJogo)
                                meuJogo = []
                                visualizarApostas(3)
                                break
                            
                                    
                        else:
                            print(f"ERRO! Você já inseriu a dezena {dezena}.\n\n\n\n\n")
                    
                    else:
                        print("ERRO! A Quina só contempla números entre 1 a 80.\n\n\n\n\n")
                else:
                    print("Dezena Inválida!\n\n\n\n\n")
        case 4:
            print(f"4. Loto Mania - {numDezenas} dezenas de 0 a 99")
            conta = 0
            meuJogo = []
            
            while conta < numDezenas:
                dezena = input(f"Digite a Dezena: {conta + 1} de {numDezenas}: ")
                os.system("clear")
        
                if dezena.isnumeric():
                    if int(dezena) >= 0 and int(dezena) <= 99:
                        if int(dezena) not in meuJogo:
                            meuJogo.append(int(dezena))
                            print(f"Dezena {dezena} inserida:")
                            print(f"{meuJogo}")
                            conta += 1
        
        
                            if len(meuJogo) == numDezenas:
                                lotoMania.append(meuJogo)
                                meuJogo = []
                                visualizarApostas(4)
                                break
                            
                                    
                        else:
                            print(f"ERRO! Você já inseriu a dezena {dezena}.\n\n\n\n\n")
                    
                    else:
                        print("ERRO! A Loto Mania só contempla números entre 0 a 99.\n\n\n\n\n")
                else:
                    print("Dezena Inválida!\n\n\n\n\n")


        case 5:
            print(f"5. Time Mania - {numDezenas} dezenas de 1 a 80.")
            conta = 0
            meuJogo = []
            
            while conta < numDezenas:
                dezena = input(f"Digite a Dezena: {conta + 1} de {numDezenas}: ")
                os.system("clear")
        
                if dezena.isnumeric():
                    if int(dezena) >= 1 and int(dezena) <= 80:
                        if int(dezena) not in meuJogo:
                            meuJogo.append(int(dezena))
                            print(f"Dezena {dezena} inserida:")
                            print(f"{meuJogo}")
                            conta += 1
        
        
                            if len(meuJogo) == numDezenas:
                                timeMania.append(meuJogo)
                                meuJogo = []
                                visualizarApostas(5)
                                break
                            
                                    
                        else:
                            print(f"ERRO! Você já inseriu a dezena {dezena}.\n\n\n\n\n")
                    
                    else:
                        print("ERRO! A Time Mania só contempla números entre 1 a 80.\n\n\n\n\n")
                else:
                    print("Dezena Inválida!\n\n\n\n\n")
        case 6:
            print(f"6. Dupla Sena - {numDezenas} dezenas de 1 a 50.")
            conta = 0
            meuJogo = []
            
            while conta < numDezenas:
                dezena = input(f"Digite a Dezena: {conta + 1} de {numDezenas}: ")
                os.system("clear")
        
                if dezena.isnumeric():
                    if int(dezena) >= 1 and int(dezena) <= 50:
                        if int(dezena) not in meuJogo:
                            meuJogo.append(int(dezena))
                            print(f"Dezena {dezena} inserida:")
                            print(f"{meuJogo}")
                            conta += 1
        
        
                            if len(meuJogo) == numDezenas:
                                duplaSena.append(meuJogo)
                                meuJogo = []
                                visualizarApostas(6)
                                break
                            
                                    
                        else:
                            print(f"ERRO! Você já inseriu a dezena {dezena}.\n\n\n\n\n")
                    
                    else:
                        print("ERRO! A Dupla Sena só contempla números entre 1 a 50.\n\n\n\n\n")
                else:
                    print("Dezena Inválida!\n\n\n\n\n")


        case 7:
            print(f"7. Dia de Sorte - {numDezenas} dezenas de 1 a 31.")
            conta = 0
            meuJogo = []
            
            while conta < numDezenas:
                dezena = input(f"Digite a Dezena: {conta + 1} de {numDezenas}: ")
                os.system("clear")
        
                if dezena.isnumeric():
                    if int(dezena) >= 1 and int(dezena) <= 31:
                        if int(dezena) not in meuJogo:
                            meuJogo.append(int(dezena))
                            print(f"Dezena {dezena} inserida:")
                            print(f"{meuJogo}")
                            conta += 1
        
        
                            if len(meuJogo) == numDezenas:
                                diaDeSorte.append(meuJogo)
                                meuJogo = []
                                visualizarApostas(7)
                                break
                                    
                        else:
                            print(f"ERRO! Você já inseriu a dezena {dezena}.\n\n\n\n\n")
                    
                    else:
                        print("ERRO! A Dia de Sorte só contempla números entre 1 a 31.\n\n\n\n\n")
                else:
                    print("Dezena Inválida!\n\n\n\n\n")


        case 8:
            print(f"8. Super Sete - {numDezenas} dezenas de 0 a 9")
            conta = 0
            meuJogo = []
            
            while conta < numDezenas:
                dezena = input(f"Digite a Dezena: {conta + 1} de {numDezenas}: ")
                os.system("clear")
        
                if dezena.isnumeric():
                    if int(dezena) >= 0 and int(dezena) <= 9:
                        meuJogo.append(int(dezena))
                        print(f"Dezena {dezena} inserida:")
                        print(f"{meuJogo}")
                        conta += 1
    
    
                        if len(meuJogo) == numDezenas:
                            superSete.append(meuJogo)
                            meuJogo = []
                            visualizarApostas(8)
                            break
                    
                    else:
                        print("ERRO! A Super Sete só contempla números entre 0 a 9.\n\n\n\n\n")
                else:
                    print("Dezena Inválida!\n\n\n\n\n")


        
"""
def numerosLoteriaCaixa(dezenas):

    if len(numerosSorteados) == 0:
        for num in dezenas:
            numerosSorteados.append(int(num))
            print(f" {num}", end=" ")

    else:
        numerosSorteados = []
        numerosSorteados(dezenas)
    #visualizaNumerosSorteados()
"""
def menuConfereApostas():
    while True:
        print("Conferência de Apostas - Escolha a sua aposta no Menu abaixo.")
        print("1. Mega Sena")
        print("2. Lotofácil")
        print("3. Quina")
        print("4. Loto Mania")
        print("5. Time Mania")
        print("6. Dupla-Sena")
        print("7. Dia-de-Sorte")
        print("8. Super Sete")
        print("0. Retornar ao Menu Principal")

        opcao = input("Opção: 1-2-3-4-5-6-7-8-9 ou 0 pra Retornar ao Menu Principal. ")

        if opcao.isnumeric():
            match int(opcao):
                case 1:
                    print("Conferindo Aposta da Mega Sena")
                    confereMegaSena(sorteadosMegaSena, megaSena)
                    break



def confereMegaSena(sorteado, minhaAposta):
    # Verificando número de acertos nas apostas
    if len(sorteado) > 0 and len(minhaAposta) > 0:
        sorteado = sorteado[0]

        #visualizaNumerosSorteados(sorteado)
        
        contaAcertos = 0
        for i in range(len(minhaAposta)):
            print(f"Jogo Nº {i+1}", end=" => ")
            print(sorted(minhaAposta[i]))
            for j in range(len(minhaAposta[i])):
                if minhaAposta[i][j] in sorteado:
                    contaAcertos += 1

            print("\n")
            print(f"Jogo {i+1}: {contaAcertos} acertos", end=" ---> ")
            if contaAcertos == 11:
                print("Você ganhou o prêmio mínimo de R$ 5,00\n\n\n\n\n")
            elif contaAcertos == 12:
                print("Você ganhou o prêmio para 12 acertos: R$ 10,00\n\n\n\n\n")
            elif contaAcertos == 13:
                print("Você ganhou o prêmio para 13 acertos: R$ 25,00\n\n\n\n\n")
            elif contaAcertos == 14:
                print("Você ganhou o prêmio para 14 acertos: R$ 25,00\n\n\n\n\n")
            elif contaAcertos == 15:
                print("Parabéns! Você ganhou a premiação máxima!\n\n\n\n\n")
            else:
                print("Você não ganhou prêmio nenhum. Não foi dessa vez.\n\n\n\n\n")

            contaAcertos = 0
            print()
        
    else:
        print("ERRO! Antes de conferir apostas, é necessário inserir seus jogos e também conferir as Dezenas Sorteadas.\n\n\n\n\n")

def confereApostas(sorteado, minhaAposta):
    # Verificando número de acertos nas apostas
    if len(sorteado) > 0 and len(minhaAposta) > 0:
        #visualizaNumerosSorteados(sorteado)
        
        contaAcertos = 0
        for i in range(len(minhaAposta)):
            print(f"Jogo Nº {i+1}", end=" => ")
            print(sorted(minhaAposta[i]))
            for j in range(len(minhaAposta[i])):
                if minhaAposta[i][j] in sorteado:
                    contaAcertos += 1

            print("\n")
            print(f"Jogo {i+1}: {contaAcertos} acertos", end=" ---> ")
            if contaAcertos == 11:
                print("Você ganhou o prêmio mínimo de R$ 5,00\n\n\n\n\n")
            elif contaAcertos == 12:
                print("Você ganhou o prêmio para 12 acertos: R$ 10,00\n\n\n\n\n")
            elif contaAcertos == 13:
                print("Você ganhou o prêmio para 13 acertos: R$ 25,00\n\n\n\n\n")
            elif contaAcertos == 14:
                print("Você ganhou o prêmio para 14 acertos: R$ 25,00\n\n\n\n\n")
            elif contaAcertos == 15:
                print("Parabéns! Você ganhou a premiação máxima!\n\n\n\n\n")
            else:
                print("Você não ganhou prêmio nenhum. Não foi dessa vez.\n\n\n\n\n")

            contaAcertos = 0
            print()
        
    else:
        print("ERRO! Antes de conferir apostas, é necessário inserir seus jogos e também as Dezenas sorteadas na Lotofácil do dia.\n\n\n\n\n")



def resultadosLoteria():
    while True:
        print("-=-=-= Resultados - Loterias Caixa -=-=-=-=-=")
        print("1. Mega Sena")
        print("2. Loto Fácil")
        print("3. Quina")
        print("4. Loto Mania")
        print("5. Time Mania")
        print("6. Dupla-Sena")
        print("7. Dia-de-Sorte")
        print("8. Super Sete")
        print("0. Retornar ao Menu Principal")

        opcao = input("Opção: 1-2-3-4-5-6-7-8-9 ou 0 pra retornar ao Menu Principal")
        os.system("clear")

        if opcao.isnumeric():
            match opcao:
                case "0":
                    print("0. Retornar ao Menu Principal.\n\n\n\n\n")
                    break
                case "1":
                    print("1. Mega Sena")
                    pegaResultadoLoteriasAPI("mega-sena")
                case "2":
                    print("2. Loto Fácil")
                    pegaResultadoLoteriasAPI("lotofacil")
                case "3":
                    print("3. Quina")
                    pegaResultadoLoteriasAPI("quina")
                case "4":
                    print("4. Loto Mania")
                    pegaResultadoLoteriasAPI("lotomania")
                case "5":
                    print("5. Time Mania")
                    pegaResultadoLoteriasAPI("timemania")
                case "6":
                    print("6. Dupla Sena")
                    pegaResultadoLoteriasAPI("dupla-sena")
                case "7":
                    print("7. Dia-de-Sorte")
                    pegaResultadoLoteriasAPI("dia-de-sorte")
                case "8":
                    print("8. Super Sete")
                    pegaResultadoLoteriasAPI("super-sete")
                case _:
                    print("Opção Inválida")



def menu():
    while True:
        print("======== Bem vindos ao Sistema de Conferência da Lotofácil - Caixa Econômica Federal =========")
        print("Escolha uma das opções abaixo: ")
        print("1. Inserir aposta")
        print("2. Visualizar apostas")
        print("3. Resultados da Loteria")
        print("4. Conferir Apostas")
        print("5. Resultado Lotofácil")

        opcao = input("Opção: 1.2.3.4 ou 5 Sair: ")
        os.system("clear")
        if opcao.isnumeric():

            match opcao:
                case "1":
                    print("Opção 1: Inserir Aposta.\n\n")
                    insereApostas() 
                case "2":
                    print("Opção 2: Visualizar Apostas.\n\n")
                    print("Qual Aposta deseja visualizar?")
                    print("1. Mega Sena")
                    print("2. Loto Fácil")
                    print("3. Quina")
                    print("4. Loto Mania")
                    print("5. Time Mania")
                    print("6. Dupla Sena")
                    print("7. Dia de Sorte")
                    print("8. Super Sete")
                    print("9. Ver Todas")
                    print("0. Retornar ao Menu Principal")
                    qualJogo = input("Digite a opção: ")

                    if qualJogo.isnumeric():
                        if int(qualJogo) >= 1 and int(qualJogo) <= 8:
                            visualizarApostas(int(qualJogo))
                        
                        elif int(qualJogo) == 9:
                            visualizarTodasAsApostas()

                        else:
                            print("Opção inválida.")
                    else:
                        print("Valor inválido.")
                    
                case "3":
                    print("Opção 3: Resultados da Loteria.\n\n")
                    resultadosLoteria()
                     
                case "4":
                    print("Opção 4: Conferir Apostas.\n\n")
                    menuConfereApostas()
                case "5":
                    print("Você saiu do programa.\n\n\n\n\n")
                    break
                case _:
                    print("Opção inválida.\n\n\n\n\n")

        else:
            print("Valor inválido.\n\n\n\n\n")


if __name__ == "__main__":
    menu()