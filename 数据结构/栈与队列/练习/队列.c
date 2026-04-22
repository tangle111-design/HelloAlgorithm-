#include <stdio.h>
#include <stdlib.h>
/* 练习版：基于链表实现的队列 */
#include <stdbool.h>

typedef struct ListNode
{
    int val;
    struct ListNode *next;
} ListNode;

typedef struct
{
    ListNode *front, *rear;
    int queSize;
} LinkedListQueue;

/* 构造函数 */
LinkedListQueue *newLinkedListQueue()
{
    LinkedListQueue *newone = malloc(sizeof(LinkedListQueue));
    newone->queSize = 0;
    newone->front = NULL;
    newone->rear = NULL;
    return newone;
}

/* 析构函数 */
void delLinkedListQueue(LinkedListQueue *queue)
{
    while (queue->front != NULL)
    {
        ListNode *temp = queue->front;
        queue->front = queue->front->next;
        free(temp);
    }
    free(queue);
}

/* 获取队列的长度 */
int size(LinkedListQueue *queue)
{
    return queue->queSize;
}

/* 判断队列是否为空 */
bool empty(LinkedListQueue *queue)
{
    return queue->queSize == 0;
}

/* 入队 */
void push(LinkedListQueue *queue, int num)
{
    ListNode *newnode = malloc(sizeof(ListNode));
    newnode->val = num;
    newnode->next = NULL;
    if (!empty(queue))
    {
        queue->rear->next = newnode;
        queue->rear = queue->rear->next;
    }
    else
    {
        // 空队列时，新节点应同时成为队首和队尾，即 front 和 rear 都要指向它。
        queue->rear = newnode;
        queue->front = newnode;
    }
    queue->queSize++;
}

/* 访问队首元素 */
int peek(LinkedListQueue *queue)
{
    if (empty(queue))
    {
        printf("empty");
        return -1;
    }
    return queue->front->val;
}

/* 出队 */
int pop(LinkedListQueue *queue)
{
    if (empty(queue))
    {
        printf("empty");
        return -1;
    }
    int res = queue->front->val;
    ListNode *temp = queue->front;
    queue->front = queue->front->next;
    free(temp);
    queue->queSize--;
    if (queue->queSize == 0)
    {
        queue->rear = NULL;
    }
    return res;
}

/* 打印队列 */
void printLinkedListQueue(LinkedListQueue *queue)
{
    ListNode *node = queue->front;
    while (node != NULL)
    {
        printf("%d ", node->val);
        node = node->next;
    }
}

/* 练习提示：
 * 1. 先区分空队列和非空队列。
 * 2. 头尾指针必须同步更新，不能只改一个。
 * 3. 出队后如果队列变空，要检查 rear 是否也需要重置。
 * 4. 打印前先把链表遍历到数组，再统一输出。
 */