while True:
  linha = input();
  if linha == "0 0": break;
  
  N, M = map(int, linha.split());
  matriz = [];
  
  for _ in range(N):
    matriz.append(list(map(int, input().split())));
  
  for i in range(N):
    for j in range(M):
      