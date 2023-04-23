package Algorithm2;

import java.util.Scanner;

// 첫째 줄에 영어 소문자와 대문자로만 이루어진 단어가 주어진다. 단어 길이는 최대 100이다.
// 첫째 줄에 입력으로 주어진 단어에서 대문자는 소문자로, 소문자는 대문자로 바꾼 단어를 출력한다.

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str = sc.next();
    char[] ans = str.toCharArray();
    for (int i = 0; i < str.length(); i++) {
      if ('a' <= ans[i] && ans[i] <= 'z') {
        ans[i] = (char) ('A' + ans[i] - 'a');
      } else {
        ans[i] = (char) ('a' + ans[i] - 'A');
      }
    }
    sc.close();

    System.out.println(ans);
  }
}