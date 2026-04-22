"""N 皇后问题（练习版）：回溯法。"""


def n_queens(n: int) -> list[list[list[str]]]:
    """返回所有合法棋盘方案，'Q' 表示皇后，'#' 表示空位。"""
    if n <= 0:
        return []

    state = [["#" for _ in range(n)] for _ in range(n)]
    cols = [False] * n
    diags1 = [False] * (2 * n - 1)  # 主对角线索引：row - col + n - 1
    diags2 = [False] * (2 * n - 1)  # 次对角线索引：row + col
    res: list[list[list[str]]] = []

    def backtrack(row: int) -> None:
        # 步骤 1：若 row == n，说明每一行都已放置皇后，复制当前棋盘到 res。
        if row == n:
            return

        # 步骤 2：尝试在当前行的每一列放皇后。
        for col in range(n):
            diag1 = row - col + n - 1
            diag2 = row + col

            # 步骤 3：若列/主对角线/次对角线任一被占用，跳过。
            if cols[col] or diags1[diag1] or diags2[diag2]:
                continue

            # 步骤 4（尝试）：在 (row, col) 放置皇后，并标记占用。
            state[row][col] = "Q"
            cols[col] = diags1[diag1] = diags2[diag2] = True

            # 步骤 5：递归处理下一行。
            backtrack(row + 1)

            # 步骤 6（回退）：移除皇后并恢复占用标记。
            state[row][col] = "#"
            cols[col] = diags1[diag1] = diags2[diag2] = False

    backtrack(0)
    return res
