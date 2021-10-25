def solution(board, moves):
    answer = 0
    box = [0]
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                last_doll = box.pop()
                curr_doll = board[j][i-1]
                board[j][i-1] = 0
                if last_doll != curr_doll:
                    box.append(last_doll)
                    box.append(curr_doll)
                    break;
                else : 
                    answer +=1
                    break;
                
    return answer * 2

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))