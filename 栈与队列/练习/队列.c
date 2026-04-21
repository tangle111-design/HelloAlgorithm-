/* 练习版：基于链表实现的队列 */
#include <stdbool.h>

typedef struct ListNode ListNode;

typedef struct {
    ListNode *front, *rear;
    int queSize;
} LinkedListQueue;

/* 构造函数 */
LinkedListQueue *newLinkedListQueue();

/* 析构函数 */
void delLinkedListQueue(LinkedListQueue *queue);

/* 获取队列的长度 */
int size(LinkedListQueue *queue);

/* 判断队列是否为空 */
bool empty(LinkedListQueue *queue);

/* 入队 */
void push(LinkedListQueue *queue, int num);

/* 访问队首元素 */
int peek(LinkedListQueue *queue);

/* 出队 */
int pop(LinkedListQueue *queue);

/* 打印队列 */
void printLinkedListQueue(LinkedListQueue *queue);

/* 练习提示：
 * 1. 先区分空队列和非空队列。
 * 2. 头尾指针必须同步更新，不能只改一个。
 * 3. 出队后如果队列变空，要检查 rear 是否也需要重置。
 * 4. 打印前先把链表遍历到数组，再统一输出。
 */