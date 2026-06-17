"""N 皇后问题练习版：经典回溯算法应用。


问题描述：
在 n×n 的国际象棋棋盘上放置 n 个皇后，使得它们彼此之间不能相互攻击。
皇后可以攻击同一行、同一列、以及两条对角线上的任意棋子。

示例（4皇后问题）：
解法1:          解法2:
. Q . .         . . Q .
. . . Q         Q . . .
Q . . .         . . . Q
. . Q .         . Q . .

（其中 Q 表示皇后，. 表示空位）


回溯法核心思想：
1. **逐行尝试**：每行只放一个皇后，避免同行冲突
2. **剪枝策略**：在放置前检查是否与已放置的皇后冲突
3. **状态记录**：使用数组标记被占用的列和对角线
4. **递归+回溯**：深度优先搜索 + 撤销选择
"""


def n_queens(n: int) -> list[list[list[str]]]:
    """N 皇后问题求解器。

    返回所有合法的棋盘方案。

    参数说明：
        n: 棋盘大小，也是需要放置的皇后数量

    返回值：
        三维列表，每个元素是一个完整的棋盘方案（二维字符矩阵）
        'Q' 表示皇后位置，'#' 或 '.' 表示空位

    算法流程：
    - 从第0行开始，逐行放置皇后
    - 对于每一行，遍历所有列，找到安全的位置
    - 放置后进入下一行递归
    - 如果某行无法放置任何皇后，则回溯到上一行
    - 当所有行都放置完毕时，找到一个合法解
    """
    # 步骤 1：处理边界情况
    # TODO: 若 n <= 0，返回空列表（没有有效的棋盘）
    if n <= 0:
        return []

    # 步骤 2：初始化棋盘状态
    # TODO: 创建 n×n 的二维列表，初始值全部为 "#"
    # 提示：使用列表推导式 [["#" for _ in range(n)] for _ in range(n)]
    state = [["#" for _ in range(n)] for _ in range(n)]

    # 步骤 3：创建占用标记数组（用于快速判断是否可以放置）
    # TODO 1: 创建长度为 n 的列表 cols，初始值全为 False
    #       含义：cols[col] = True 表示第 col 列已有皇后
    cols = [False] * n

    # TODO 2: 创建长度为 (2*n-1) 的列表 diags1，初始值全为 False
    #       含义：主对角线占用情况（row - col 为常数）
    #       索引计算公式：diag1_index = row - col + n - 1
    diags1 = [False] * (2 * n - 1)

    # TODO 3: 创建长度为 (2*n-1) 的列表 diags2，初始值全为 False
    #       含义：次对角线占用情况（row + col 为常数）
    #       索引计算公式：diag2_index = row + col
    diags2 = [False] * (2 * n - 1)

    # 步骤 4：创建结果存储列表
    # TODO: 创建空列表 res，用于存储所有合法的棋盘方案
    res: list[list[list[str]]] = []

    # 步骤 5：定义回溯函数
    def backtrack(row: int) -> None:
        """在第 row 行尝试放置皇后。"""
        # 步骤 6：检查是否完成（终止条件）
        # TODO: 若 row == n，表示已经成功放置了 n 个皇后
        #       需要保存当前棋盘的深拷贝到结果列表中
        if row == n:
            res.append([line[:] for line in state])
            return

        # 步骤 7：遍历当前行的每一列
        # TODO: 使用 for 循环遍历 col 从 0 到 n-1
        for col in range(n):

            # 步骤 8：计算对角线索引
            # TODO 1: 计算主对角线索引 diag1 = row - col + n - 1
            # TODO 2: 计算次对角线索引 diag2 = row + col
            diag1 = row - col + n - 1
            diag2 = row + col

            # 步骤 9：剪枝判断（关键步骤！）
            # TODO: 如果以下任一条件为 True，则跳过当前列（continue）：
            #   - cols[col]: 当前列已被占用
            #   - diags1[diag1]: 主对角线已被占用
            #   - diags2[diag2]: 次对角线已被占用
            if cols[col] or diags1[diag1] or diags2[diag2]:
                continue

            # 步骤 10：做选择（放置皇后）
            # TODO 1: 在棋盘上标记当前位置为 "Q"
            #       state[row][col] = "Q"
            state[row][col] = "Q"

            # TODO 2: 更新三个占用标记数组为 True
            #       cols[col], diags1[diag1], diags2[diag2] = True, True, True
            cols[col] = diags1[diag1] = diags2[diag2] = True

            # 步骤 11：递归调用（处理下一行）
            # TODO: 调用 backtrack(row + 1)
            backtrack(row + 1)

            # 步骤 12：撤销选择（回溯！非常重要！）
            # TODO 1: 将棋盘当前位置恢复为 "#"
            #       state[row][col] = "#"
            state[row][col] = "#"

            # TODO 2: 将三个占用标记恢复为 False
            #       cols[col], diags1[diag1], diags2[diag2] = False, False, False
            cols[col] = diags1[diag1] = diags2[diag2] = False

    # 步骤 13：启动回溯搜索
    # TODO: 调用 backtrack(0)，从第 0 行开始放置皇后
    backtrack(0)

    # 步骤 14：返回结果
    # TODO: 返回 res（包含所有合法方案的列表）
    return res


if __name__ == "__main__":
    # 测试代码
    print("=" * 60)
    print("N 皇后问题测试")
    print("=" * 60)

    test_cases = [
        (4, 2),   # 4皇后有2种解
        (8, 92),  # 8皇后有92种解
    ]

    all_passed = True
    for n, expected_count in test_cases:
        solutions = n_queens(n)
        actual_count = len(solutions)

        passed = actual_count == expected_count
        status = "✅" if passed else "❌"

        print(f"\n{status} n={n}: 找到 {actual_count} 种解 (期望 {expected_count})")

        if not passed:
            all_passed = False

        # 显示第一个解法的可视化
        if solutions and len(solutions) > 0:
            print("示例解法:")
            for i, line in enumerate(solutions[0]):
                print(f"  第{i}行: {' '.join(line)}")

    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 所有测试通过！")
    else:
        print("⚠️  存在测试失败，请检查代码")