from vars import *
from funcoes import *
from api import *







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
                    print("Na Time Mania você pode escolher 10 dezenas")

                    numDezenasTimeMania = 10

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
        os.system("clear")

        if opcao.isnumeric():
            match int(opcao):
                case 1:
                    if len(megaSena) > 0:
                        print("Conferindo sua(s) Aposta(s) da Mega Sena")
                        pegaResultadoLoteriasAPI("mega-sena")
                        confereMegaSena(sorteadosMegaSena, megaSena)
                        break
                    else:
                        print("Você precisa primeiro inserir suas apostas antes de conferir.")
                        break

                case 2:
                    if len(lotoFacil) > 0:
                        print("Conferindo sua(s) Aposta(s) da Loto Fácil")
                        pegaResultadoLoteriasAPI("lotofacil")
                        confereLotoFacil(sorteadosLotoFacil, lotoFacil)
                        break
                    else:
                        print("Você precisa primeiro inserir suas apostas antes de conferir.")
                        break

                case 3:
                    if len(quina) > 0:
                        print("Conferindo sua(s) Aposta(s) da Quina")
                        pegaResultadoLoteriasAPI("quina")
                        confereQuina(sorteadosQuina, quina)
                        break
                    else:
                        print("Você precisa primeiro inserir suas apostas antes de conferir.")

                case 4:
                    if len(lotoMania) > 0:
                        print("Conferindo sua(s) Aposta(s) da Loto Mania")
                        pegaResultadoLoteriasAPI("lotomania")
                        confereLotoMania(sorteadosLotoMania, lotoMania)
                        break
                    else:
                        print("Você precisa primeiro inserir suas apostas antes de conferir.")
                        break

                case 5:
                    if len(timeMania) > 0:
                        print("Conferindo sua(s) Aposta(s) da Time Mania")
                        pegaResultadoLoteriasAPI("timemania")
                        confereTimeMania(sorteadosTimeMania, timeMania)
                        break
                    else:
                        print("Você precisa primeiro inserir suas apostas antes de conferir.")
                        break


                case 6:
                    if len(duplaSena) > 0:
                        print("Conferindo sua(s) Aposta(s) da Dupla Sena")
                        pegaResultadoLoteriasAPI("dupla-sena")
                        confereDuplaSena(sorteadosDuplaSena, duplaSena)
                        break
                    else:
                        print("Você precisa primeiro inserir suas apostas antes de conferir.")
                        break

                case 7:
                    print("Conferindo sua(s) Aposta(s) da Dia de Sorte")
                    pegaResultadoLoteriasAPI("dia-de-sorte")

                case 8:
                    print("Conferindo sua(s) Aposta(s) da Super Sete")
                    pegaResultadoLoteriasAPI("super-sete")








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
        print("5. Sair")

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