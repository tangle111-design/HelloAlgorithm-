- Question
	- 根据国际象棋的规则，皇后可以攻击与同处一行、一列或一条斜线上的棋子。给定 \(n\) 个皇后和一个 \[n*n\] 大小的棋盘，寻找使得所有皇后之间无法相互攻击的摆放方案。
- ## 逐行放置策略
	- ## 列与对角线剪枝
	- 我们可以利用一个长度为 \[n\] 的布尔型数组 `cols` 记录每一列是否有皇后。在每次决定放置前，我们通过 `cols` 将已有皇后的列进行剪枝，并在回溯中动态更新 `cols` 的状态。
	-
	- 设棋盘中某个格子的行列索引为 \[(row,col)\] ，主对角线上所有格子的 \[row-col\] 为恒定值。
	- 也就是说，如果两个格子满足 \[row_1-col_1=row_2-col_2\] ，则它们一定处在同一条主对角线上。利用该规律，我们可以借助数组 `diags1` 记录每条主对角线上是否有皇后。
	- 同理，次对角线上的所有格子的 \[row+col\] 是恒定值。我们同样也可以借助数组 `diags2` 来处理次对角线约束。
		-
- Code:
	- ```python
	  def backtrack(
	      row: int,
	      n: int,
	      state: list[list[str]],
	      res: list[list[list[str]]],
	      cols: list[bool],
	      diags1: list[bool],
	      diags2: list[bool],
	  ):
	      """回溯算法：n 皇后"""
	      # 当放置完所有行时，记录解
	      if row == n:
	          res.append([list(row) for row in state])
	          return
	      # 遍历所有列
	      for col in range(n):
	          # 计算该格子对应的主对角线和次对角线
	          diag1 = row - col + n - 1
	          diag2 = row + col
	          # 剪枝：不允许该格子所在列、主对角线、次对角线上存在皇后
	          if not cols[col] and not diags1[diag1] and not diags2[diag2]:
	              # 尝试：将皇后放置在该格子
	              state[row][col] = "Q"
	              cols[col] = diags1[diag1] = diags2[diag2] = True
	              # 放置下一行
	              backtrack(row + 1, n, state, res, cols, diags1, diags2)
	              # 回退：将该格子恢复为空位
	              state[row][col] = "#"
	              cols[col] = diags1[diag1] = diags2[diag2] = False
	  
	  def n_queens(n: int) -> list[list[list[str]]]:
	      """求解 n 皇后"""
	      # 初始化 n*n 大小的棋盘，其中 'Q' 代表皇后，'#' 代表空位
	      state = [["#" for _ in range(n)] for _ in range(n)]
	      cols = [False] * n  # 记录列是否有皇后
	      diags1 = [False] * (2 * n - 1)  # 记录主对角线上是否有皇后
	      diags2 = [False] * (2 * n - 1)  # 记录次对角线上是否有皇后
	      res = []
	      backtrack(0, n, state, res, cols, diags1, diags2)
	  
	      return res
	  ```