"""N 皇后问题（LeetCode 51）。

经典回溯算法应用：在 n×n 棋盘上放置 n 个皇后，使它们互不攻击。
皇后可以攻击同一行、同一列、同一对角线上的所有棋子。

解题思路：
- 逐行放置皇后，每行只放一个
- 使用三个数组标记被占用的列、主对角线、次对角线
- 当放置到第 n 行时，记录一个合法解
"""


def n_queens(n: int) -> list[list[list[str]]]:
    """N 皇后问题求解器。

    返回所有合法棋盘方案，'Q' 表示皇后，'#' 表示空位。

    参数：
        n: 棋盘大小（也是皇后数量）

    返回：
        所有合法方案的列表，每个方案是一个二维字符数组

    时间复杂度：O(n!)（最坏情况）
    空间复杂度：O(n²)（存储方案）
    """
    if n <= 0:
        return []

    # 初始化棋盘状态
    state = [["#" for _ in range(n)] for _ in range(n)]

    # 占用标记数组
    cols = [False] * n                    # 列占用情况
    diags1 = [False] * (2 * n - 1)       # 主对角线 (row - col + n - 1)
    diags2 = [False] * (2 * n - 1)       # 次对角线 (row + col)

    res: list[list[list[str]]] = []

    def backtrack(row: int) -> None:
        """回溯函数：在第 row 行放置皇后。"""
        if row == n:
            # 找到一个合法解，保存当前棋盘的深拷贝
            res.append([line[:] for line in state])
            return

        # 尝试在当前行的每一列放置皇后
        for col in range(n):
            diag1 = row - col + n - 1   # 主对角线索引
            diag2 = row + col           # 次对角线索引

            # 剪枝：检查是否冲突
            if cols[col] or diags1[diag1] or diags2[diag2]:
                continue

            # 做选择：放置皇后
            state[row][col] = "Q"
            cols[col] = diags1[diag1] = diags2[diag2] = True

            # 递归：处理下一行
            backtrack(row + 1)

            # 撤销选择：移除皇后（回溯）
            state[row][col] = "#"
            cols[col] = diags1[diag1] = diags2[diag2] = False

    backtrack(0)
    return res


if __name__ == "__main__":
    test_cases = [4, 8]

    print("N 皇后问题测试结果：")
    print("-" * 50)
    for n in test_cases:
        solutions = n_queens(n)
        print(f"\nn={n}: 共找到 {len(solutions)} 种解法")

        if solutions and len(solutions) > 0:
            print(f"示例解法 1:")
            for line in solutions[0]:
                print("".join(line))