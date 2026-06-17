"""回溯算法基础练习版：从二叉树搜索到通用框架的递进式学习。


学习目标：
理解回溯法的核心思想，掌握"尝试→递归→回退"的基本模式。


本文件包含四个递进式的示例：

示例1 - 简单遍历：
在二叉树中查找所有值为 7 的节点
（最基础的 DFS，不涉及状态管理）

示例2 - 路径记录：
查找从根节点到所有值为 7 的节点的完整路径
（引入状态管理：维护当前路径）

示例3 - 带约束剪枝：
路径中不允许出现值 3 的节点
（引入剪枝策略：提前终止无效分支）

示例4 - 通用框架：
将回溯法抽象为通用模板
（理解回溯的本质结构）


核心概念总结：
- **状态 (State)**: 当前所处的状态或已做出的选择
- **选择 (Choice)**: 当前可以做的决策
- **约束 (Constraint)**: 限制选择是否合法的条件
- **目标 (Goal)**: 判断是否找到解的条件
- **回溯 (Backtrack)**: 撤销选择，返回上一层重新尝试
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar


@dataclass
class TreeNode:
    """二叉树节点定义。

    属性说明：
        val: 节点存储的整数值
        left: 左子节点的引用（可能为 None）
        right: 右子节点的引用（可能为 None）
    """

    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def find_nodes_with_value_7(root: TreeNode | None) -> list[TreeNode]:
    """例题一：返回所有值为 7 的节点。

    这是最基础的深度优先搜索（DFS）遍历。
    不涉及复杂的状态管理，只是简单地访问每个节点。

    算法流程：
    1. 如果当前节点为空，直接返回
    2. 如果当前节点值为 7，将其加入结果列表
    3. 递归处理左子树
    4. 递归处理右子树

    时间复杂度：O(n)，需要访问所有 n 个节点
    空间复杂度：O(h)，h 为树的高度（递归栈空间）
    """
    # 步骤 1：创建结果列表
    # TODO: 创建空列表 res，用于存储找到的目标节点
    res: list[TreeNode] = []

    # 步骤 2：定义前序遍历函数
    def pre_order(node: TreeNode | None) -> None:
        """前序遍历二叉树。

        参数：
            node: 当前正在访问的节点
        """
        # 步骤 3：空节点检查（终止条件）
        # TODO: 若 node 为 None，直接 return（到底了）
        if node is None:
            return

        # 步骤 4：检查当前节点是否符合条件
        # TODO: 若 node.val == 7，将 node 添加到 res 列表中
        if node.val == 7:
            res.append(node)

        # 步骤 5：递归遍历左子树
        # TODO: 调用 pre_order(node.left)
        pre_order(node.left)

        # 步骤 6：递归遍历右子树
        # TODO: 调用 pre_order(node.right)
        pre_order(node.right)

    # 步骤 7：启动遍历
    # TODO: 调用 pre_order(root)，从根节点开始遍历
    pre_order(root)

    # 步骤 8：返回结果
    # TODO: 返回 res
    return res


def find_paths_to_value_7(root: TreeNode | None) -> list[list[TreeNode]]:
    """例题二：返回从根节点到所有值为 7 的节点的完整路径。

    新概念 - 状态管理：
    除了记录找到的目标，还需要记录"如何到达目标"。
    使用 path 列表保存从根节点到当前节点的路径。

    回溯的关键操作：
    - **尝试**：进入子节点前，将当前节点加入 path
    - **记录**：当找到目标时，保存 path 的深拷贝
    - **回退**：处理完子节点后，将当前节点从 path 中移除

    为什么需要深拷贝？
    因为 path 是全局共享的列表，后续会修改它。
    如果不复制，最终所有保存的路径都会变成相同的！
    """
    # 步骤 1：初始化数据结构
    # TODO 1: 创建空列表 res，用于存储所有找到的路径
    # TODO 2: 创建空列表 path，用于记录当前的访问路径
    res: list[list[TreeNode]] = []
    path: list[TreeNode] = []

    # 步骤 2：定义带路径记录的前序遍历函数
    def pre_order(node: TreeNode | None) -> None:
        """带有路径记录的前序遍历。

        参数：
            node: 当前正在访问的节点
        """
        # 步骤 3：空节点检查
        # TODO: 若 node 为 None，直接 return
        if node is None:
            return

        # 步骤 4：尝试 - 将当前节点加入路径（做选择）
        # TODO: 调用 path.append(node)
        path.append(node)

        # 步骤 5：检查是否找到目标
        # TODO: 若 node.val == 7，则保存当前路径的深拷贝到 res
        # 提示：使用 list(path) 创建深拷贝
        if node.val == 7:
            res.append(list(path))

        # 步骤 6：递归遍历左子树
        # TODO: 调用 pre_order(node.left)
        pre_order(node.left)

        # 步骤 7：递归遍历右子树
        # TODO: 调用 pre_order(node.right)
        pre_order(node.right)

        # 步骤 8：回退 - 将当前节点从路径中移除（撤销选择）
        # TODO: 调用 path.pop()
        # 解释：这一步非常关键！表示我们已经完成了这个节点的所有处理，
        #       需要返回到父节点，所以要从路径中移除它
        path.pop()

    # 步骤 9：启动遍历
    # TODO: 调用 pre_order(root)
    pre_order(root)

    # 步骤 10：返回结果
    # TODO: 返回 res
    return res


def find_paths_to_value_7_without_3(root: TreeNode | None) -> list[list[TreeNode]]:
    """例题三：返回值为 7 的路径，且路径中不能包含值为 3 的节点。

    新概念 - 剪枝 (Pruning)：
    在搜索过程中，如果发现当前路径已经违反约束条件，
    就立即停止向下搜索，直接返回。

    剪枝的好处：
    - 减少不必要的递归调用
    - 大幅提高算法效率
    - 在某些情况下可以将指数级时间降至多项式时间

    本例的剪枝条件：
    如果当前节点的值为 3，则以该节点为根的整个子树都不需要搜索了，
    因为任何经过该节点的路径都会包含 3。
    """
    # 步骤 1：初始化数据结构
    # TODO 1: 创建空列表 res
    # TODO 2: 创建空列表 path
    res: list[list[TreeNode]] = []
    path: list[TreeNode] = []

    # 步骤 2：定义带剪枝的遍历函数
    def pre_order(node: TreeNode | None) -> None:
        """带有剪枝策略的前序遍历。

        参数：
            node: 当前正在访问的节点
        """
        # 步骤 3：剪枝判断（关键优化！）
        # TODO: 如果以下任一条件成立，直接 return：
        #   条件1: node is None （空节点）
        #   条件2: node.val == 3 （遇到禁止的值，剪掉整个分支）
        if node is None or node.val == 3:
            return

        # 步骤 4：尝试 - 将当前节点加入路径
        # TODO: 调用 path.append(node)
        path.append(node)

        # 步骤 5：检查是否找到目标
        # TODO: 若 node.val == 7，保存 path 的深拷贝到 res
        if node.val == 7:
            res.append(list(path))

        # 步骤 6：递归遍历左子树
        # TODO: 调用 pre_order(node.left)
        pre_order(node.left)

        # 步骤 7：递归遍历右子树
        # TODO: 调用 pre_order(node.right)
        pre_order(node.right)

        # 步骤 8：回退 - 移除当前节点
        # TODO: 调用 path.pop()
        path.pop()

    # 步骤 9：启动遍历
    # TODO: 调用 pre_order(root)
    pre_order(root)

    # 步骤 10：返回结果
    # TODO: 返回 res
    return res


if __name__ == "__main__":
    print("=" * 60)
    print("回溯算法基础测试")
    print("=" * 60)

    # 构建测试用的二叉树
    # 树的结构如下：
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   7   5
    #      /
    #     7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(5)
    root.left.right.left = TreeNode(7)

    print("\n测试用的二叉树结构：")
    print("      1")
    print("     / \\")
    print("    2   3")
    print("   / \\   \\")
    print("  4   7   5")
    print("     /")
    print("    7")

    # 测试示例1
    print("\n【示例1】查找值为 7 的节点")
    nodes = find_nodes_with_value_7(root)
    print(f"找到 {len(nodes)} 个值为 7 的节点")

    # 测试示例2
    print("\n【示例2】查找到值为 7 的路径")
    paths = find_paths_to_value_7(root)
    print(f"找到 {len(paths)} 条路径:")
    for i, path in enumerate(paths):
        path_values = [node.val for node in path]
        print(f"  路径{i+1}: {' → '.join(map(str, path_values))}")

    # 测试示例3（带剪枝）
    print("\n【示例3】查找不含 3 的路径（带剪枝）")
    filtered_paths = find_paths_to_value_7_without_3(root)
    print(f"找到 {len(filtered_paths)} 条有效路径:")
    for i, path in enumerate(filtered_paths):
        path_values = [node.val for node in path]
        print(f"  路径{i+1}: {' → '.join(map(str, path_values))}")

    print("\n" + "=" * 60)
    print("✅ 回溯算法基础示例完成！")
    print("\n关键要点回顾：")
    print("1. 尝试 → 递归 → 回退 是回溯的核心模式")
    print("2. 使用 path 列表记录当前状态")
    print("3. 通过剪枝提前终止无效分支，提高效率")
    print("4. 保存结果时要使用深拷贝（list(path)）")