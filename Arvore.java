import java.util.*;
public class Arvore {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int x = in.nextInt();
    int[] crescimento = {1, 2, 4, 5, 7, 13};
    int altura = 0;

    while (x != 0) {
      if (x <= crescimento.length) {
        altura = crescimento[x - 1];
      } else {
        altura = crescimento[5] + (x - 6) * (crescimento[5] - crescimento[4]);
      }
      System.out.println(altura);
      x = in.nextInt();
    }

    in.close();
  }
}