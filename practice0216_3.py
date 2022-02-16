from datetime import datetime, timedelta

order_times = ["12:10", "12:20", "12:40", "12:40", "12:50", "13:00", "13:20"]
k = 20


def solution(order_times, k):
    answer = 0
    for i in range(len(order_times)-1):
        start = datetime.strptime(order_times[i], '%H:%M')
        end = start + timedelta(minutes=k)
        cnt = 0
        for j in range(len(order_times)):
            if datetime.strptime(order_times[j], '%H:%M') >= start and datetime.strptime(order_times[j], '%H:%M') <= end:
                cnt += 1
        answer = max(answer, cnt)
    return answer


print(solution(order_times, k))
