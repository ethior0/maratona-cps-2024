while True:
  linha = input();
  if linha == "0 0": break;
  N, Q = map(int, linha.split());
  
  lista = input().split();

  for _ in range(Q):
    soma = 0;
    L, R = map(int, input().split());
    L -= 1;
    
    for i in range(L, R-1):
      valorAtual = lista[i];
      for j in range(i+1, R):
        valor1 = valorAtual + lista[j];
        valor2 = lista[j] + valorAtual;
        soma += int(valor1) + int(valor2);
    print(soma);