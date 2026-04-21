#include <stdexcept>
#include <vector>
#include <iostream>
using namespace std;

/* 练习版：基于环形数组实现的双向队列 */
class ArrayDeque
{
private:
  vector<int> nums; // 存储元素的数组
  int front;        // 队首指针
  int queSize;      // 当前长度

public:
  /* 构造方法 */
  ArrayDeque(int capacity)
  {
    nums.resize(capacity);
    front = queSize = 0;
  }

  /* 获取双向队列的容量 */
  int capacity()
  {
    return nums.size();
  }

  /* 获取双向队列的长度 */
  int size()
  {
    return queSize;
  }

  /* 判断双向队列是否为空 */
  bool isEmpty()
  {
    return queSize == 0;
  }

  /* 计算环形数组索引 */
  int index(int i)
  {
    int cap = capacity();
    // 确保结果在 [0, cap-1]
    return ((i % cap) + cap) % cap;
  }

  /* 队首入队 */
  void pushFirst(int num)
  {
    // 先检查是否已满
    if (size() == capacity())
    {
      cout << "full" << endl;
      return;
    }

    // 不能写front--;
    front = index(front - 1);
    nums[index(front)] = num;
    queSize++;
  }

  /* 队尾入队 */
  void pushLast(int num)
  {
    if (size() == capacity())
    {
      cout << "full" << endl;
      return;
    }
    nums[index(front + size())] = num;
    queSize++;
  }

  /* 队首出队 */
  int popFirst()
  {
    // 先判断是否为空
    if (isEmpty())
    {
      cout << "empty" << endl;
      return -1;
    }
    int res = nums[index(front)];
    // 不能写front++;
    front = index(front + 1);
    queSize--;
    return res;
  }

  /* 队尾出队 */
  int popLast()
  {
    if (isEmpty())
    {
      cout << "empty" << endl;
      return -1;
    }
    int res = nums[index(front + size() - 1)];
    queSize--;
    return res;
  }

  /* 访问队首元素 */
  int peekFirst()
  {
    if (isEmpty())
    {
      
      throw std::out_of_range("deque empty");
    }
    return nums[front];
  }

  /* 访问队尾元素 */
  int peekLast()
  {
    if (isEmpty())
    {
      
      throw std::out_of_range("deque empty");
    }
    return nums[index(front + size() - 1)];
  }
  /* 返回数组用于打印 */
  vector<int> toVector()
  {
    vector<int> res(queSize);
    for (int i = 0, j = front; i < size(); i++, j++)
    {
      res[i] = nums[index(j)];
    }
    return res;
  }
};

/* 提示：
 * 1. 队首和队尾都由 front、queSize 协同维护。
 * 2. 队首插入时要先左移 front，再写入新值。
 * 3. 队尾插入时，队尾索引可以由 front + queSize 计算得到。
 * 4. 删除时要先读值，再移动指针或缩小长度。
 */