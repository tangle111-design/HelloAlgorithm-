"""汉诺塔问题（Tower of Hanoi）- 经典分治算法。

问题描述：
有三根柱子 A、B、C，A 柱上有 n 个大小不一的圆盘（大的在下小的在上）。
目标是将所有圆盘从 A 移到 C，规则：
1. 每次只能移动一个圆盘
2. 大盘不能放在小盘上面
3. 可以借助 B 柱作为中转

分治策略：
将"移动 n 个盘子"分解为三个子问题：
1. 将上面 n-1 个盘子从 A 移到 B（借助 C）
2. 将最底下的盘子从 A 移到 C
3. 将 n-1 个盘子从 B 移到 C（借助 A）

时间复杂度：O(2^n) - 每次增加一个盘子，步数翻倍
空间复杂度：O(n) - 递归深度
"""


def move(src: list[int], tar: list[int]) -> None:
    """移动一个圆盘从源柱到目标柱。

    参数：
        src: 源柱子（圆盘列表）
        tar: 目标柱子（圆盘列表）
    """
    pan = src.pop()   # 从源柱顶部取出一个圆盘
    tar.append(pan)   # 放到目标柱顶部


def dfs(i: int, src: list[int], buf: list[int], tar: list[int]) -> None:
    """递归求解汉诺塔问题。

    分治思路：
    将 i 个圆盘从 src 移动到 tar（使用 buf 作为缓冲）

    参数：
        i: 要移动的圆盘数量
        src: 源柱子
        buf: 缓冲柱子（辅助）
        tar: 目标柱子

    递归结构：
    f(i, src, buf, tar) =
        f(i-1, src, tar, buf) + move(src,tar) + f(i-1, buf, src, tar)
    """
    if i == 1:
        # 基本情况：只剩一个圆盘，直接移动
        move(src, tar)
        return

    # 子问题1：将上面 i-1 个圆盘从 src 移到 buf（借助 tar）
    dfs(i - 1, src, tar, buf)

    # 子问题2：将最后一个圆盘从 src 移到 tar
    move(src, tar)

    # 子问题3：将 buf 上的 i-1 个圆盘移到 tar（借助 src）
    dfs(i - 1, buf, src, tar)


def solve_hanota(A: list[int], B: list[int], C: list[int]) -> None:
    """求解汉诺塔问题的主函数。

    参数：
        A: 起始柱（初始有所有圆盘，大数在下小数在上）
        B: 辅助柱（初始为空）
        C: 目标柱（初始为空）
    """
    n = len(A)
    dfs(n, A, B, C)


if __name__ == "__main__":
    print("汉诺塔问题测试")
    print("=" * 50)

    for n in [1, 2, 3]:
        A = list(range(n, 0, -1))  # 初始化：n, n-1, ..., 1
        B, C = [], []

        print(f"\nn={n}: 初始状态 A={A}, B=[], C=[]")
        solve_hanota(A, B, C)
        print(f"最终状态: A={A}, B={B}, C={C}")
        print(f"移动次数: {2**n - 1} (理论值)")