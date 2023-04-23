package Algorithm2;
import java.util.Scanner;

// 철수는 화학 시험을 망치고, 애꿎은 화학 선생님에게 복수를하기로 한다.
// 철수는 집에서 만든 자동 로봇팔을 선생님의 책상에 숨겨, 선생님이 수업을 시작하려 들어온 순간 숨겨놓은 로봇팔을 이용해 선생님을 혼내주려고한다. 
// 철수는 선생님이 늘 애용하는 물컵에 시간이 되면 로봇팔이 소금을 잔뜩 집어넣도록 프로그램을 짜려고한다.
// 철수는 현재시각과 선생님이 언제 컵을 사용할지 시간을 알고있지만, 수 계산에 정말 약해서 로봇팔에 입력해야할 시간 계산을 못한다. 철수가 로봇팔에 알맞은 시간을 입력할수 있도록 도와주자.

// 첫째 줄에는 현재 시각이 hh:mm:ss로 주어진다. 시간의 경우 0≤h≤23 이며, 분과 초는 각각 0≤m≤59, 0≤s≤59 이다.
// 두 번째 줄에는 소금 투하의 시간이 hh:mm:ss로 주어진다.

// 로봇팔이 소금을 투하할때까지 필요한 시간을 hh:mm:ss로 출력한다. 이 시간은 1초보다 크거나 같고, 24시간보다 작거나 같다.

public class String5 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String realTime = sc.next();
    String saltTime = sc.next();

    String[] realTimeArr = realTime.split(":");
    String[] saltTimeArr = saltTime.split(":");

    int secondDiff = (60 * 60 * Integer.parseInt(saltTimeArr[0]) + 60 * Integer.parseInt(saltTimeArr[1])
        - (60 * 60 * Integer.parseInt(realTimeArr[0]) + 60 * Integer.parseInt(realTimeArr[1])
            + Integer.parseInt(realTimeArr[2]))
        + Integer.parseInt(saltTimeArr[2]));

    secondDiff = secondDiff < 0 ? secondDiff + 24 * 60 * 60 : secondDiff;

    String hour = secondDiff / 3600 < 10 ? "0" + (secondDiff / 3600) : Integer.toString(secondDiff / 3600);
    String minute = (secondDiff % 3600) / 60 < 10 ? "0" + ((secondDiff % 3600) / 60)
        : Integer.toString((secondDiff % 3600) / 60);
    String second = (secondDiff % 3600) % 60 < 10 ? "0" + ((secondDiff % 3600) % 60)
        : Integer.toString((secondDiff % 3600) % 60);

    System.out.print(hour);
    System.out.print(":");
    System.out.print(minute);
    System.out.print(":");
    System.out.print(second);

    sc.close();
  }
}
