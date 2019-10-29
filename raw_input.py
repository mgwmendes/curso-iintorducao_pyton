def remover(nomes):
  
  print('Qual nome você gostaria de remover?')
  print(nomes)
  r_nome = raw_input()
  nomes.remove(r_nome)
  print('%s foi removido da lista' % (r_nome))
  print('Lista atual')
  print(nomes)


nomes = ['Mauricio', 'Gustavo', 'Webber', 'Mendes']
remover(nomes)
  
  
