from regex import P
from vars import *
from listaTimes import *


def setNumerosSorteadosList(dezenas, tipoLoteria):
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
    if tipo == "Time Mania":
        
        for aposta in loteria:
            print(f"Aposta {conta} - Time do Coração: {aposta[-1]}", end=" : ")
            for numero in aposta[0:-1]:#sorted(aposta):
                print(f"- {numero}", end=" ")
        
            print()
            conta += 1
    
        conta = 1

    else:
        for aposta in loteria:
            print(f"Aposta {conta}", end=" : ")
            for numero in sorted(aposta):
                print(f"- {numero}", end=" ")

            print()
            conta += 1

        conta = 1



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
                                megaSena.append(sorted(meuJogo))
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
                                lotoFacil.append(sorted(meuJogo))
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
                                quina.append(sorted(meuJogo))
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
                                lotoMania.append(sorted(meuJogo))
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
                                conta = 1
                                for time in times:
                                    print(f"Time {conta} : {time}")
                                    conta += 1

                                timeDoCoracao = input("Digite seu time do coração: ")
                                if not timeDoCoracao.isnumeric():
                                    if len(timeDoCoracao) > 0:
                                        meuJogo.append(timeDoCoracao)
                                        timeMania.append(sorted(meuJogo))
                                        meuJogo = []
                                        visualizarApostas(5)
                                        break
                                    else:
                                        print("É preciso digitar o time do coração.")
                                else:
                                    print("Erro! Favor digite o nome do time.")
     
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
                                duplaSena.append(sorted(meuJogo))
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
                                diaDeSorte.append(sorted(meuJogo))
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
                            superSete.append(sorted(meuJogo))
                            meuJogo = []
                            visualizarApostas(8)
                            break
                    
                    else:
                        print("ERRO! A Super Sete só contempla números entre 0 a 9.\n\n\n\n\n")
                else:
                    print("Dezena Inválida!\n\n\n\n\n")


"""
        Funções para conferência de apostas:

        - Cada função confere uma aposta específica, comparando a aposta do usuário com o resultado vindo da API.
"""

def confereMegaSena(sorteado, minhaAposta):
    print("-=-=-=-=-= Conferindo Apostas da Mega Sena -=-=-=-=-=")
    # Verificando número de acertos nas apostas
    if len(sorteado) > 0 and len(minhaAposta) > 0:
        sorteado = sorteado[0]
        minhaAposta = sorted(minhaAposta)
        #visualizaNumerosSorteados(sorteado)
        
        contaAcertos = 0
        for i in range(len(minhaAposta)):
            print(f"Jogo Nº {i+1}", end=" => ")
            for j in range(len(minhaAposta[i])):
                if minhaAposta[i][j] in sorteado:
                    contaAcertos += 1
                    print(f" ({minhaAposta[i][j]}) ", end=" ")
                else:
                    print(f" {minhaAposta[i][j]} ", end=" ")

            print("\n")
            print(f"Jogo {i+1}: {contaAcertos} acertos", end=" ---> ")
            if contaAcertos == 4:
                print("Você ganhou o prêmio para Quadra.\n\n\n\n\n")
            elif contaAcertos == 5:
                print("Você ganhou o prêmio para Quina.\n\n\n\n\n")
            elif contaAcertos == 6:
                print("Você ganhou o prêmio para a Sena.\n\n\n\n\n")
            else:
                print("Você não ganhou prêmio nenhum. Não foi dessa vez.\n\n\n\n\n")

            contaAcertos = 0
            print("-="*50)
        
    


def confereLotoFacil(sorteado, minhaAposta):
    print("-=-=-=-=-= Conferindo Apostas da Loto Fácil -=-=-=-=-=")
    # Verificando número de acertos nas apostas
    if len(sorteado) > 0 and len(minhaAposta) > 0:
        sorteado = sorteado[0]

        #visualizaNumerosSorteados(sorteado)
        
        contaAcertos = 0
        for i in range(len(minhaAposta)):
            print(f"Jogo Nº {i+1}", end=" => ")
            for j in range(len(minhaAposta[i])):
                if minhaAposta[i][j] in sorteado:
                    contaAcertos += 1
                    print(f" ({minhaAposta[i][j]}) ", end=" ")
                else:
                    print(f" {minhaAposta[i][j]} ", end=" ")


            print(f"Jogo {i+1}: {contaAcertos} acertos", end=" ---> ")
            if contaAcertos == 11:
                print("Você ganhou o prêmio para 11 acertos.\n\n\n\n\n")
            elif contaAcertos == 12:
                print("Você ganhou o prêmio para 12 acertos.\n\n\n\n\n")
            elif contaAcertos == 13:
                print("Você ganhou o prêmio para 13 acertos.\n\n\n\n\n")
            elif contaAcertos == 14:
                print("Você ganhou o prêmio para 14 acertos.\n\n\n\n\n")
            elif contaAcertos == 15:
                print("Parabéns! Você ganhou a premiação para 15 acertos.!\n\n\n\n\n")
            else:
                print("Você não ganhou prêmio nenhum. Não foi dessa vez.\n\n\n\n\n")

            contaAcertos = 0
            print("-="*50)
        
    


def confereQuina(sorteado, minhaAposta):
    print("-=-=-=-=-= Conferindo Apostas da Quina -=-=-=-=-=")
    # Verificando número de acertos nas apostas
    if len(sorteado) > 0 and len(minhaAposta) > 0:
        sorteado = sorteado[0]

        #visualizaNumerosSorteados(sorteado)
        
        contaAcertos = 0
        for i in range(len(minhaAposta)):
            print(f"Jogo Nº {i+1}", end=" => ")
            for j in range(len(minhaAposta[i])):
                if minhaAposta[i][j] in sorteado:
                    contaAcertos += 1
                    print(f" ({minhaAposta[i][j]}) ", end=" ")
                else:
                    print(f" {minhaAposta[i][j]} ", end=" ")

            print("\n")
            print(f"Jogo {i+1}: {contaAcertos} acertos", end=" ---> ")
            if contaAcertos == 2:
                print("Você ganhou o prêmio para o Duque.\n\n\n\n\n")
            elif contaAcertos == 3:
                print("Você ganhou o prêmio para o Terno.\n\n\n\n\n")
            elif contaAcertos == 4:
                print("Você ganhou o prêmio para a Quadra.\n\n\n\n\n")
            elif contaAcertos == 5:
                print("Parabéns! Você ganhou o prêmio para a Quina!\n\n\n\n\n")
            
            else:
                print("Você não ganhou prêmio nenhum. Não foi dessa vez.\n\n\n\n\n")

            contaAcertos = 0
            print("-="*50)
        



def confereLotoMania(sorteado, minhaAposta):
    print("-=-=-=-=-= Conferindo Apostas da Loto Mania -=-=-=-=-=")
    # Verificando número de acertos nas apostas
    if len(sorteado) > 0 and len(minhaAposta) > 0:
        sorteado = sorteado[0]

        #visualizaNumerosSorteados(sorteado)
        
        contaAcertos = 0
        for i in range(len(minhaAposta)):
            print(f"Jogo Nº {i+1}", end=" => ")
            for j in range(len(minhaAposta[i])):
                if minhaAposta[i][j] in sorteado:
                    contaAcertos += 1
                    print(f" ({minhaAposta[i][j]}) ", end=" ")
                else:
                    print(f" {minhaAposta[i][j]} ", end=" ")

            print("\n")
            print(f"Jogo {i+1}: {contaAcertos} acertos", end=" ---> ")
            if contaAcertos == 0:
                print("Parabéns! Você ganhou o prêmio para 0 Acertos!\n\n\n\n\n")
            elif contaAcertos == 15:
                print("Você ganhou o prêmio para 15 acertos.\n\n\n\n\n")
            elif contaAcertos == 16:
                print("Você ganhou o prêmio para 16 acertos.\n\n\n\n\n")
            elif contaAcertos == 17:
                print("Você ganhou o prêmio para 17 acertos.\n\n\n\n\n")
            elif contaAcertos == 18:
                print("Você ganhou o prêmio para 18 acertos.\n\n\n\n\n")
            elif contaAcertos == 19:
                print("Você ganhou o prêmio para 19 acertos.!\n\n\n\n\n")
            elif contaAcertos == 20:
                print("Parabéns! Você ganhou o prêmio para 20 acertos!\n\n\n\n\n")
            else:
                print("Você não ganhou prêmio nenhum. Não foi dessa vez.\n\n\n\n\n")

            contaAcertos = 0
            print("-="*50)



def confereTimeMania(sorteado, minhaAposta):
    print("-=-=-=-=-= Conferindo Apostas da Loto Mania -=-=-=-=-=")
    # Verificando número de acertos nas apostas

    
    
    if len(sorteado) > 0 and len(minhaAposta) > 0:
        sorteado = sorteado[0]
        
        contaAcertos = 0
        for i in range(len(minhaAposta)):
            print(f"Jogo Nº {i+1}", end=" => ")
            for j in range(len(minhaAposta[i][0:-1])):
                if minhaAposta[i][j] in sorteado:
                    contaAcertos += 1
                    print(f" ({minhaAposta[i][j]}) ", end=" ")
                else:
                    print(f" {minhaAposta[i][j]} ", end=" ")
                
            print("\n")
            print(f"Jogo {i+1}: {contaAcertos} acertos", end=" ---> ")
            if minhaAposta[i][-1] == sorteado[-1]:
                print("Parabéns, você acertou o time do coração.")
            elif contaAcertos == 3:
                print("Parabéns! Você ganhou o prêmio para 3 Acertos!\n\n\n\n\n")
            elif contaAcertos == 4:
                print("Você ganhou o prêmio para 4 acertos.\n\n\n\n\n")
            elif contaAcertos == 5:
                print("Você ganhou o prêmio para 5 acertos.\n\n\n\n\n")
            elif contaAcertos == 6:
                print("Você ganhou o prêmio para 6 acertos.\n\n\n\n\n")
            elif contaAcertos == 7:
                print("Você ganhou o prêmio para 7 acertos.\n\n\n\n\n")
            else:
                print("Você não ganhou prêmio nenhum. Não foi dessa vez.\n\n\n\n\n")

            contaAcertos = 0
            print("-="*50)


def confereDuplaSena():
    pass