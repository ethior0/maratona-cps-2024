while True:
  D = int(input());
  if D == 0: break;
  
  pontos = [0, 400, 800, 1200, 1600, 2000];
  
  for i in range(len(pontos)):
    pontos[i] = (pontos[i] - D);
    if pontos[i] < 0:
      valorString = str(pontos[i])[1:len(str(pontos[i]))];
      pontos[i] = int(valorString);
  
  pontos.sort();  
  print(pontos[0]);