from vars import *
from funcoes import *

def pegaResultadoLoteriasAPI(loteria):
    
    request = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/{loteria}/latest")
    
    resultado = json.loads(request.content)

    setNumerosSorteadosList(resultado['dezenas'], loteria)
    

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
