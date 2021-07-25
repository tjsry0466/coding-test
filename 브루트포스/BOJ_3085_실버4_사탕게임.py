# 2개의 수를 뽑아서 자리를 바꾼 후에 연속된 수가 몇개가 있는지 조사.
# 1. 자리수 2개 바꾸기
# 2. 바뀐 배열에서 최대 연속수 찾기.

n = int(input())
board = [list(input()) for _ in range(n)]

ans = 0
def check(board):
    cnt = 0
    for i in range(n):
        cnt_row = 1
        cnt_col = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt_row += 1
            else:
                cnt = max(cnt, cnt_row)
                cnt_row = 1

            if board[j][i] == board[j+1][i]:
                cnt_col += 1
            else:
                cnt = max(cnt, cnt_col)
                cnt_col = 1
        cnt = max(cnt, cnt_row, cnt_col)
    return cnt

for i in range(n):
    for j in range(n-1):
        if board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            ans = max(ans, check(board))

            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if board[j][i] != board[j+1][i]:
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
            ans = max(ans, check(board))

            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
print(ans)

