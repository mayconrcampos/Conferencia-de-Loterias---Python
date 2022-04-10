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