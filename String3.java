package Algorithm2;
import java.util.Scanner;

// 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
// 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
// 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

public class String3 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str = sc.next();
    char[] arrStringToChar = str.toCharArray();
    int[] arrAlphabet = new int[26];
    int maxCount = 0;
    int cnt = 0;
    int index = 0;
    for (int i = 0; i < str.length(); i++)
      if ('a' <= arrStringToChar[i] && arrStringToChar[i] <= 'z') {
        arrAlphabet[arrStringToChar[i] - 'a']++;
      } else {
        arrAlphabet[arrStringToChar[i] - 'A']++;
      }

    for (int i = 0; i < 26; i++) {
      if (maxCount < arrAlphabet[i])
        maxCount = arrAlphabet[i];
    }

    for (int i = 0; i < 26; i++) {
      if (maxCount == arrAlphabet[i]) {
        cnt++;
        index = i;
      }
      if (cnt > 1) {
        System.out.println('?');
        break;
      }
    }

    if (cnt == 1)
      System.out.println((char) (index + 'A'));

    sc.close();
  }
}
