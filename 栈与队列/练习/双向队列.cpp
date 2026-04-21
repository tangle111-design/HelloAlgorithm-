#include <vector>

using namespace std;

/* 练习版：基于环形数组实现的双向队列 */
class ArrayDeque {
  private:
    vector<int> nums; // 存储元素的数组
    int front;        // 队首指针
    int queSize;      // 当前长度

  public:
    /* 构造方法 */
    ArrayDeque(int capacity);

    /* 获取双向队列的容量 */
    int capacity();

    /* 获取双向队列的长度 */
    int size();

    /* 判断双向队列是否为空 */
    bool isEmpty();

    /* 计算环形数组索引 */
    int index(int i);

    /* 队首入队 */
    void pushFirst(int num);

    /* 队尾入队 */
    void pushLast(int num);

    /* 队首出队 */
    int popFirst();

    /* 队尾出队 */
    int popLast();

    /* 访问队首元素 */
    int peekFirst();

    /* 访问队尾元素 */
    int peekLast();

    /* 返回数组用于打印 */
    vector<int> toVector();
};

/* 提示：
 * 1. 队首和队尾都由 front、queSize 协同维护。
 * 2. 队首插入时要先左移 front，再写入新值。
 * 3. 队尾插入时，队尾索引可以由 front + queSize 计算得到。
 * 4. 删除时要先读值，再移动指针或缩小长度。
 */