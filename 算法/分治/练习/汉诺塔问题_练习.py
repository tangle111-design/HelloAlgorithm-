"""汉诺塔问题练习版：经典递归与分治算法。


问题描述：
有三根柱子 A、B、C，A 柱上有 n 个圆盘（从大到小叠放）。
目标：将所有圆盘从 A 移到 C。
规则：
1. 每次只能移动一个圆盘
2. 大盘不能放在小盘上面
3. 可以借助 B 柱作为中转

示例（n=3）：
步骤1: A→C (移动圆盘1)
步骤2: A→B (移动圆盘2)
步骤3: C→B (移动圆盘1)
步骤4: A→C (移动圆盘3)  ← 最大盘子到位！
步骤5: B→A (移动圆盘1)
步骤6: B→C (移动圆盘2)
步骤7: A→C (移动圆盘1)
完成！

总移动次数 = 2^n - 1
"""


def move(src: list[int], tar: list[int]) -> None:
    """移动一个圆盘。

    参数：
        src: 源柱子
        tar: 目标柱子
    """
    # 步骤 1：从源柱顶部取出圆盘
    # TODO: 使用 src.pop() 取出顶部元素，赋值给 pan
    pan = src.pop()

    # 步骤 2：放到目标柱顶部
    # TODO: 使用 tar.append(pan) 将圆盘放入目标柱
    tar.append(pan)


def dfs(i: int, src: list[int], buf: list[int], tar: list[int]) -> None:
    """递归求解汉诺塔问题。

    分治策略：
    将"移动 i 个圆盘"分解为三步：
    1. 先将上面 i-1 个移到缓冲柱
    2. 再将最大的那个移到目标柱
    3. 最后将 i-1 个从缓冲柱移到目标柱

    参数：
        i: 要移动的圆盘数量
        src: 源柱
        buf: 缓冲柱（辅助）
        tar: 目标柱
    """
    # 步骤 1：基本情况（终止条件）
    # TODO: 若 i == 1，直接调用 move(src, tar) 然后 return
    if i == 1:
        move(src, tar)
        return

    # 步骤 2：将上面 i-1 个圆盘从 src 移到 buf（借助 tar）
    # TODO: 调用 dfs(i-1, src, tar, buf)
    dfs(i - 1, src, tar, buf)

    # 步骤 3：将最后一个圆盘从 src 移到 tar
    # TODO: 调用 move(src, tar)
    move(src, tar)

    # 步骤 4：将 buf 上的 i-1 个圆盘移到 tar（借助 src）
    # TODO: 调用 dfs(i-1, buf, src, tar)
    dfs(i - 1, buf, src, tar)


def solve_hanota(A: list[int], B: list[int], C: list[int]) -> None:
    """汉诺塔问题主函数。"""
    n = len(A)
    dfs(n, A, B, C)


if __name__ == "__main__":
    print("=" * 60)
    print("汉诺塔问题测试")
    print("=" * 60)

    for n in [1, 2, 3]:
        A = list(range(n, 0, -1))
        B, C = [], []

        print(f"\n{n} 个圆盘:")
        print(f"  初始: A={A}, B=[], C=[]")
        solve_hanota(A, B, C)
        print(f"  结果: A={A}, B={B}, C={C}")
        print(f"  理论移动次数: {2**n - 1}")

    print("\n💡 关键要点：")
    print("- 分治思想：大问题拆分为小问题")
    print("- 递归结构：f(n) = f(n-1) + move + f(n-1)")
    print("- 时间复杂度：O(2^n)")