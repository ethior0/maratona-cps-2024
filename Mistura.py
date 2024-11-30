import math;

while True:
  linha = input();
  if linha == "0 0": break;
  
  N, K = map(int, linha.split());
    
  prateleira = list(map(int, input().split()));
  
  print();