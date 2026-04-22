"""N 皇后问题：回溯法。"""


def n_queens(n: int) -> list[list[list[str]]]:
    """返回所有合法棋盘方案，'Q' 表示皇后，'#' 表示空位。"""
    if n <= 0:
        return []

    state = [["#" for _ in range(n)] for _ in range(n)]
    cols = [False] * n
    diags1 = [False] * (2 * n - 1)  # 主对角线：row - col + n - 1
    diags2 = [False] * (2 * n - 1)  # 次对角线：row + col
    res: list[list[list[str]]] = []

    def backtrack(row: int) -> None:
        if row == n:
            res.append([line[:] for line in state])
            return

        for col in range(n):
            diag1 = row - col + n - 1
            diag2 = row + col
            if cols[col] or diags1[diag1] or diags2[diag2]:
                continue

            state[row][col] = "Q"
            cols[col] = diags1[diag1] = diags2[diag2] = True

            backtrack(row + 1)

            state[row][col] = "#"
            cols[col] = diags1[diag1] = diags2[diag2] = False

    backtrack(0)
    return res