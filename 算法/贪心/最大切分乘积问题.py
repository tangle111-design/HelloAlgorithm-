"""最大切分乘积问题（LeetCode 343 - 整数拆分）。

问题描述：
给定一个正整数 n，将其拆分为至少两个正整数的和，
使这些整数的乘积最大化，返回最大的乘积。

数学原理：
- 最优解应尽可能多地拆分成 3（因为 3 的乘积效率最高）
- 当余数为 1 时，将 3+1 转换为 2+2（因为 2×2 > 3×1）
- 当余数为 2 时，保留即可

贪心策略：
1. n ≤ 3: 特殊处理（必须拆分出 1）
2. n > 3: 尽可能多拆成 3

时间复杂度：O(1)
空间复杂度：O(1)
"""

import math


def max_product_cutting(n: int) -> int:
    """计算整数拆分的最大乘积。

    参数：
        n: 要拆分的正整数（n ≥ 2）

    返回：
        拆分后能得到的最大乘积

    算法逻辑：
    - n=2: 拆为 1+1, 乘积=1
    - n=3: 拆为 1+2, 乘积=2
    - n=4: 拆为 2+2, 乘积=4 (不拆成 3+1)
    - n=5: 拆为 3+2, 乘积=6
    - n=6: 拆为 3+3, 乘积=9
    - ...
    """
    # 特殊情况：n ≤ 3 时必须切分出一个 1
    if n <= 3:
        return 1 * (n - 1)

    # 计算可以拆分出多少个 3 和余数
    a, b = divmod(n, 3)  # a 是 3 的个数，b 是余数

    if b == 0:
        # 余数为 0：全部拆成 3
        return int(math.pow(3, a))

    elif b == 1:
        # 余数为 1：将一个 3+1 转化为 2+2（因为 2×2 > 3×1）
        return int(math.pow(3, a - 1)) * 2 * 2

    else:  # b == 2
        # 余数为 2：保留这个 2
        return int(math.pow(3, a)) * 2


if __name__ == "__main__":
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 4),
        (5, 6),
        (10, 36),
    ]

    print("最大切分乘积问题测试结果：")
    print("-" * 50)
    for n, expected in test_cases:
        result = max_product_cutting(n)
        status = "✅" if result == expected else "❌"
        print(f"{status} n={n}: 最大乘积={result}, 期望={expected}")