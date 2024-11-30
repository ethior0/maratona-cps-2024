while True:
  linha = input();
  if linha == "0 0": break;
  
  N, K = map(int, linha.split());
  prateleira = list(map(int, input().split()));
  
  cc = 0;
  
  for left in range(N+1):
    for right in range(N - left):
      if left + right > N: break;
      array = [0 for _ in range(N - left - right)];
      for i in range(left, N - right):
        array[i - left] = prateleira[i];
      if len(array) >= K: cc += 1;
  
  print(cc);