def move(src: list[int], tar: list[int]):
    """将一个圆盘从 src 顶部移动到 tar 顶部"""
    # 步骤 1：从 src 弹出顶部圆盘。
    # 步骤 2：将该圆盘压入 tar。
    """在此处完成代码"""


def dfs(i: int, src: list[int], buf: list[int], tar: list[int]):
    """求解汉诺塔子问题 f(i)：将 src 顶部 i 个圆盘移到 tar"""
    # 步骤 1：处理 i == 1 的基线情况，直接移动一个圆盘并结束。
    # 步骤 2：先把 src 顶部 i-1 个圆盘借助 tar 移到 buf。
    # 步骤 3：把 src 剩下的最大圆盘移到 tar。
    # 步骤 4：再把 buf 顶部 i-1 个圆盘借助 src 移到 tar。
    """在此处完成代码"""


def solve_hanota(A: list[int], B: list[int], C: list[int]):
    """求解汉诺塔问题：将 A 中圆盘移到 C"""
    # 步骤 1：计算圆盘总数 n。
    # 步骤 2：调用 dfs(n, A, B, C)。
    """在此处完成代码"""
