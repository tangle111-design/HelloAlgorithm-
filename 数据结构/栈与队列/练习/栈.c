/* 练习版：基于链表实现的栈 */
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 1024

/* 基于数组实现的栈 */
typedef struct
{
  int *data;
  int size;
} ArrayStack;

/* 构造函数 */
ArrayStack *newArrayStack()
{
  ArrayStack *newone = malloc(sizeof(ArrayStack));
  newone->data = malloc(sizeof(int) *MAX_SIZE);
  newone->size = 0;
  return newone;
}

/* 析构函数 */
void delArrayStack(ArrayStack *stack)
{
  free(stack->data);
  free(stack);
}

/* 获取栈的长度 */
int size(ArrayStack *stack)
{
  return stack->size;
}

/* 判断栈是否为空 */
bool isEmpty(ArrayStack *stack)
{
  return stack->size == 0;
}

/* 入栈 */
void push(ArrayStack *stack, int num)
{
  if (size(stack) == MAX_SIZE)
  {
    printf("full");
    return;
  }
  stack->data[size(stack)] = num;
  stack->size++;
}

/* 访问栈顶元素 */
int peek(ArrayStack *stack)
{
  if (isEmpty(stack))
  {
    printf("%s", "empty");
    return -1;
  }
  return stack->data[size(stack)-1];
}

/* 出栈 */
int pop(ArrayStack *stack){
  if(isEmpty(stack)){printf("%s","empty");return -1;}
  int res = stack->data[size(stack)-1];
  stack->size--;
  return res;
}

/* 练习提示：
 * 1. 数组栈需要记录当前元素数量。
 * 2. 入栈和出栈都只影响最后一个有效位置。
 * 3. 访问栈顶前要先检查是否为空。
 */