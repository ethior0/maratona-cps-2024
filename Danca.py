while True:
  linha = input();
  if linha == "0 0 0": break;
  
  N, M, P = map(int, linha.split());
  array = [];
  cc = 1;
  
  for _ in range(N):
    linha = [];
    for j in range(M):
      linha.append(cc);
      cc += 1;
    array.append(linha);
  
  for _ in range(P):
    valores = input().split();
    O = valores[0];
    L = int(valores[1]) - 1;
    C = int(valores[2]) - 1;
    
    tam = 0;
    
    if O == "C": tam = N;
    elif O == "L": tam = M;
    
    for k in range(tam):
      if O == "C":
        array[k][L], array[k][C] = array[k][C], array[k][L];
      elif O == "L":
        array[L][k], array[C][k] = array[C][k], array[L][k];
  
  for l in range(N):
    arrayLinha = str(array[l]).replace(",", "").replace("[", "").replace("]", "");
    print(arrayLinha);