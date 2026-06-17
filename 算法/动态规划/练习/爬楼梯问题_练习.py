"""爬楼梯问题练习版：经典的斐波那契数列应用场景。


问题描述：
有 n 阶楼梯，你每次可以选择爬 1 阶或 2 阶。
问有多少种不同的方法可以爬到楼顶？


示例分析：
n=1: 1 种方法 → [1]
n=2: 2 种方法 → [1+1, 2]
n=3: 3 种方法 → [1+1+1, 1+2, 2+1]
n=4: 5 种方法 → [1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2]

规律发现：
要到达第 n 阶，最后一步只有两种可能：
1. 从第 n-1 阶爬 1 步上来
2. 从第 n-2 阶爬 2 步上来
所以：f(n) = f(n-1) + f(n-2) （这就是斐波那契数列！）
"""


def climbing_stairs_dp(n: int) -> int:
    """爬楼梯：动态规划实现（使用一维数组）。

    核心思路：
    - 定义 dp[i] 表示到达第 i 阶楼梯的方法数
    - 状态转移方程：dp[i] = dp[i-1] + dp[i-2]
      （从 i-1 走一步 或 从 i-2 走两步）
    - 边界条件：dp[1]=1, dp[2]=2
    """
    # 步骤 1：处理边界情况
    # TODO 1: 若 n <= 0，返回 0（没有楼梯）
    # TODO 2: 若 n <= 2，返回 n（可以直接得出答案）
    if n <= 0:
        return 0
    if n <= 2:
        return n

    # 步骤 2：创建 dp 数组
    # TODO: 创建长度为 n+1 的列表，初始值全为 0
    # 提示：dp[i] 对应第 i 阶楼梯的方法数
    dp = [0] * (n + 1)

    # 步骤 3：初始化已知条件（边界值）
    # TODO: 设置 dp[1] = 1（第1阶只有1种方法：走1步）
    #       设置 dp[2] = 2（第2阶有2种方法：走两次1步 或 直接走2步）
    dp[1], dp[2] = 1, 2

    # 步骤 4：填充 dp 数组（从第3阶开始计算到第n阶）
    # TODO: 使用 for 循环遍历 i 从 3 到 n（包含 n）
    for i in range(3, n + 1):

        # 步骤 5：应用状态转移方程
        # TODO: dp[i] = dp[i-1] + dp[i-2]
        # 解释：
        #   - dp[i-1]: 到达第 i-1 阶后，再走 1 步就到第 i 阶
        #   - dp[i-2]: 到达第 i-2 阶后，再走 2 步就到第 i 阶
        #   - 两者相加就是总的方法数
        dp[i] = dp[i - 1] + dp[i - 2]

    # 步骤 6：返回最终结果
    # TODO: 返回 dp[n]，即到达第 n 阶的方法总数
    return dp[n]


def climbing_stairs_dp_comp(n: int) -> int:
    """爬楼梯：空间优化版本（只使用两个变量）。

    优化原理：
    - 观察发现 dp[i] 只依赖前两个值：dp[i-1] 和 dp[i-2]
    - 不需要保存整个数组，只需记住最近的两个值即可
    - 类似于斐波那契数列的滚动数组优化

    变量含义：
    - a: 表示 dp[i-2]（倒数第二项）
    - b: 表示 dp[i-1]（倒数第一项）

    更新过程：
    新的 a = 旧的 b (dp[i-1])
    新的 b = 旧的 a + 旧的 b (dp[i-2] + dp[i-1] = dp[i])
    """
    # 步骤 1：处理边界情况
    # TODO: 与上面相同，处理 n<=0 和 n<=2 的情况
    if n <= 0:
        return 0
    if n <= 2:
        return n

    # 步骤 2：初始化两个变量
    # TODO: 设置 a=1, b=2
    # 含义：
    #   a = dp[1] = 1 （到达第1阶的方法数）
    #   b = dp[2] = 2 （到达第2阶的方法数）
    a, b = 1, 2

    # 步骤 3：迭代计算
    # TODO: 使用 for 循环从第 3 阶计算到第 n 阶
    # 提示：range(3, n+1)，循环次数为 n-2 次
    for _ in range(3, n + 1):

        # 步骤 4：滚动更新两个变量
        # TODO: 同时更新 a 和 b：
        #   - 新的 a 应该等于旧的 b
        #   - 新的 b 应该等于 旧的 a + 旧的 b
        # Python 技巧：可以使用元组赋值 a, b = b, a+b
        a, b = b, a + b

    # 步骤 5：返回最终结果
    # TODO: 返回 b（此时 b 就是 dp[n]）
    return b


if __name__ == "__main__":
    # 测试代码（验证你的实现是否正确）
    test_cases = [
        (1, 1),   # n=1, 期望输出=1
        (2, 2),   # n=2, 期望输出=2
        (3, 3),   # n=3, 期望输出=3
        (4, 5),   # n=4, 期望输出=5
        (5, 8),   # n=5, 期望输出=8
        (10, 89), # n=10, 期望输出=89
    ]

    print("爬楼梯问题测试：")
    print("=" * 40)
    all_passed = True
    for n, expected in test_cases:
        result_dp = climbing_stairs_dp(n)
        result_comp = climbing_stairs_dp_comp(n)

        passed = result_dp == expected and result_comp == expected
        status = "✅" if passed else "❌"
        print(f"{status} n={n:2d}: DP={result_dp}, 优化={result_comp}, 期望={expected}")

        if not passed:
            all_passed = False

    print("=" * 40)
    if all_passed:
        print("🎉 所有测试通过！")
    else:
        print("⚠️  存在测试失败，请检查代码")