while True:
  linha = input();
  if linha == "0 0": break;
  
  K, N = map(int, linha.split());
  
  alf = input();
  msg = input();
  
  for i in range(len(msg)):
    flag = False;
    for j in range(len(alf)):
      if alf[j] == msg[i]:
        flag = True;
    if not(flag):
      break;
  
  if flag:
    print("Sim");
  else:
    print("Não");