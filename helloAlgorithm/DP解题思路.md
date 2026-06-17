# 判断是不是动态规划
- **先观察问题是否适合使用回溯（穷举）解决**
- **适合用回溯解决的问题通常满足“决策树模型”** 这种问题可以使用树形结构来描述，其中每一个节点代表一个决策，每一条路径代表一个决策序列。 (解是通过一系列决策产生的)
-
- 加分项:
	- 问题包含最大（小）或最多（少）等最优化描述。
	- 问题的状态能够使用一个列表、多维矩阵或树来表示，并且一个状态与其周围的状态存在递推关系。
- 减分项:
	- 问题的目标是找出所有可能的解决方案，而不是找出最优解。
	- 问题描述中有明显的排列组合的特征，需要返回具体的多个方案。
-
- # 问题求解步骤
- 描述决策，定义状态，建立 dp 表，推导状态转移方程，确定边界条件
-
- ## Q:最小路径和问题
	- 给定一个 \( n \times m \) 的二维网格 grid，网格中的每个单元格包含一个非负整数，表示该单元格的代价。机器人以左上角单元格为起始点，每次只能向下或者向右移动一步，直至到达右下角单元格。请返回从左上角到右下角的最小路径和。
		-
- ## 步骤
	- **Step1:思考每轮的决策，定义状态，从而得到 dp 表**
	  collapsed:: true
			- 动态规划和回溯过程可以描述为一个决策序列，而状态由所有决策变量构成。它应当包含描述解题进度的所有变量，其包含了足够的信息，能够用来推导出下一个状态。
	- 每个状态都对应一个子问题，我们会定义一个 $dp$表来存储所有子问题的解，状态的每个独立变量都是 $dp$ 表的一个维度。从本质上看，$dp$ 表是状态和子问题的解之间的映射。
	-
	- **Step2:  找出最优子结构，进而推导出状态转移方程**
		- \[dp[i, j] = \min(dp[i - 1, j], dp[i, j - 1]) + grid[i, j]\]
			- 根据定义好的$$dp$$表，思考原问题和子问题的关系，找出通过子问题的最优解来构造原问题的最优解的方法，即最优子结构。
	- 一旦我们找到了最优子结构，就可以使用它来构建出状态转移方程。
	-
	- **Step3:  确定边界条件和状态转移顺序**
		- 首行$$i=0$$和首列$$j=0$$是边界条件
		- 外循环遍历各行，内循环遍历各列
			- 边界条件在动态规划中用于初始化$$dp$$表，在搜索中用于剪枝。
	- 状态转移顺序的核心是要保证在计算当前问题的解时，所有它依赖的更小子问题的解都已经被正确地计算出来。
-
- ## 方法
	- ### 暴力搜索
				- code:
			- ```python
			  def min_path_sum_dfs(grid: list[list[int]], i: int, j: int) -> int:
			      """最小路径和：暴力搜索"""
			      # 若为左上角单元格，则终止搜索
			      if i == 0 and j == 0:
			          return grid[0][0]
			      # 若行列索引越界，则返回 +∞ 代价
			      if i < 0 or j < 0:
			          return inf
			      # 计算从左上角到 (i-1, j) 和 (i, j-1) 的最小路径代价
			      up = min_path_sum_dfs(grid, i - 1, j)
			      left = min_path_sum_dfs(grid, i, j - 1)
			      # 返回从左上角到 (i, j) 的最小路径代价
			      return min(left, up) + grid[i][j]
			  ```
	-
	- ### 记忆化搜索
		- 引入一个和网格 `grid` 相同尺寸的记忆列表 `mem` ，用于记录各个子问题的解，并将重叠子问题进行剪枝
					- code:
			- ```python
			  def min_path_sum_dfs_mem(
			      grid: list[list[int]], mem: list[list[int]], i: int, j: int
			  ) -> int:
			      """最小路径和：记忆化搜索"""
			      # 若为左上角单元格，则终止搜索
			      if i == 0 and j == 0:
			          return grid[0][0]
			      # 若行列索引越界，则返回 +∞ 代价
			      if i < 0 or j < 0:
			          return inf
			      # 若已有记录，则直接返回
			      if mem[i][j] != -1:
			          return mem[i][j]
			      # 左边和上边单元格的最小路径代价
			      up = min_path_sum_dfs_mem(grid, mem, i - 1, j)
			      left = min_path_sum_dfs_mem(grid, mem, i, j - 1)
			      # 记录并返回左上角到 (i, j) 的最小路径代价
			      mem[i][j] = min(left, up) + grid[i][j]
			      return mem[i][j]
			  ```
	-
	- ### 动态规划
		- \[dp[i, j] = \min(dp[i - 1, j], dp[i, j - 1]) + grid[i, j]\]
		- code: $O(mn)$
		  collapsed:: true
			- ```python
			  def min_path_sum_dp(grid: list[list[int]]) -> int:
			      """最小路径和：动态规划"""
			      n, m = len(grid), len(grid[0])
			      # 初始化 dp 表
			      dp = [[0] * m for _ in range(n)]
			      dp[0][0] = grid[0][0]
			      # 状态转移：首行
			      for j in range(1, m):
			          dp[0][j] = dp[0][j - 1] + grid[0][j]
			      # 状态转移：首列
			      for i in range(1, n):
			          dp[i][0] = dp[i - 1][0] + grid[i][0]
			      # 状态转移：其余行和列
			      for i in range(1, n):
			          for j in range(1, m):
			              dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
			      return dp[n - 1][m - 1]
			  ```
		-
		- 空间优化
		- 由于每个格子只与其左边和上边的格子有关，因此我们可以只用一个单行数组来实现$$dp$$表。
		- code:
			- ```python
			  def min_path_sum_dp_comp(grid: list[list[int]]) -> int:
			      """最小路径和：空间优化后的动态规划"""
			      n, m = len(grid), len(grid[0])
			      # 初始化 dp 表
			      dp = [0] * m
			      # 状态转移：首行
			      dp[0] = grid[0][0]
			      for j in range(1, m):
			          dp[j] = dp[j - 1] + grid[0][j]
			      # 状态转移：其余行
			      for i in range(1, n):
			          # 状态转移：首列
			          dp[0] = dp[0] + grid[i][0]
			          # 状态转移：其余列
			          for j in range(1, m):
			              dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
			      return dp[m - 1]
			  ```
-
-
-