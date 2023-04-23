package Algorithm2;
import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str1 = sc.next();
    String str2 = sc.next();
    char[] arrayStr2 = str2.toCharArray();
    int count = 0;

    for (int i = 0; i < str1.length(); i++) {
      for (int j = 0; j < str2.length(); j++) {
        if (str1.charAt(i) == arrayStr2[j]) {
          count++;
          arrayStr2[j] = ' ';
          break;
        }
      }
    }
    System.out.println(str1.length() + str2.length() - count * 2);
    sc.close();
  }
}