while True:
  linha = input();
  if linha == "0 0 0": break;
  
  L, C, D = linha.split();
  # linhas, colunas, dias
  
  # Mais especificamente, se ela estiver 
  # levando W bombons, ela irá
  # demorar p×W dias para atravessar uma cidade 
  # com dificuldade p
  
  mapa = [];
  for _ in range(L):
    mapa.append(list(map(int, input().split())));
    # dificuldade da cidade na pos

  L1, C1 = map(int, input().split()); # Cidade A
  L2, C2 = map(int, input().split()); # Cidade B
  