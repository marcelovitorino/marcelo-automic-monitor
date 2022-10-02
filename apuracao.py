import threading
import requests

URL = 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'

def printit():
  threading.Timer(5.0, printit).start()
  print "Hello, World!"
  resultado = requests.get(URL).json()
  tabela = sorted([
      (candidate['nm'], candidate['vap'], candidate['pvap'])
      for candidate in resultado['cand']
      ], key=lambda linha: linha[1], reverse=True) # Ordena por votos
 
  print('Nome\tVotos\tPorcentagem')
  for linha in tabela:
      print('\t'.join(linha))

printit()
