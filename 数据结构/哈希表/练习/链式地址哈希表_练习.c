#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 键值对 */
typedef struct
{
    int key;
    char val[64];
} Pair;

/* 链表节点 */
typedef struct Node
{
    Pair *pair;
    struct Node *next;
} Node;

/* 链式地址哈希表 */
typedef struct
{
    int size;
    int capacity;
    double loadThres;
    int extendRatio;
    Node **buckets;
} HashMapChaining;

HashMapChaining *newHashMapChaining();
void delHashMapChaining(HashMapChaining *hashMap);
int hashFunc(HashMapChaining *hashMap, int key);
double loadFactor(HashMapChaining *hashMap);
char *get(HashMapChaining *hashMap, int key);
void put(HashMapChaining *hashMap, int key, const char *val);
void extend(HashMapChaining *hashMap);
void removeItem(HashMapChaining *hashMap, int key);
void printMap(HashMapChaining *hashMap);

HashMapChaining *newHashMapChaining()
{
    /* 步骤提示：
     * 1) 分配 HashMapChaining 内存
     * 2) 初始化 size/capacity/loadThres/extendRatio
     * 3) 分配 buckets 并全部置空
     */
    HashMapChaining *newhmap = malloc(sizeof(HashMapChaining));
    newhmap->size = 0;
    newhmap->capacity = 4;
    newhmap->loadThres = 2.0 / 3.0;
    newhmap->extendRatio = 2;
    newhmap->buckets = malloc(newhmap->capacity * sizeof(Node *));
    for (int i = 0; i < newhmap->capacity; i++)
    {
        newhmap->buckets[i] = NULL;
    }
    return newhmap;
}

void delHashMapChaining(HashMapChaining *hashMap)
{
    /* 步骤提示：
     * 1) 遍历每个桶和链表节点
     * 2) 依次释放 pair 与 node
     * 3) 释放 buckets 与 hashMap 本体
     */
    for (int i = 0; i < hashMap->capacity; i++)
    {
        while (hashMap->buckets[i] != NULL)
        {
            Node *temp = hashMap->buckets[i];
            hashMap->buckets[i] = hashMap->buckets[i]->next;
            free(temp->pair);
            free(temp);
        }
    }
    free(hashMap->buckets);
    free(hashMap);
}

int hashFunc(HashMapChaining *hashMap, int key)
{
    /* 步骤提示：
     * 1) 使用 key 对 capacity 取模
     */
    return key % hashMap->capacity;
}

double loadFactor(HashMapChaining *hashMap)
{
    /* 步骤提示：
     * 1) 将 size 与 capacity 转成 double 再相除
     */
    return (double)hashMap->size / (double)hashMap->capacity;
}

char *get(HashMapChaining *hashMap, int key)
{
    /* 步骤提示：
     * 1) 通过 hashFunc 定位桶
     * 2) 遍历链表查找 key
     * 3) 命中返回 val，未命中返回空串或 NULL
     */
    Node *buck = hashMap->buckets[hashFunc(hashMap, key)];
    while (buck)
    {
        if (buck->pair->key == key)
        {
            return buck->pair->val;
        }
        buck = buck->next;
    }
    return NULL;
}

void put(HashMapChaining *hashMap, int key, const char *val)
{
    /* 步骤提示：
     * 1) 检查负载因子，必要时先扩容
     * 2) 在桶内查找是否已有 key
     * 3) 有则更新，无则头插/尾插新节点
     * 4) 新增节点时维护 size
     */
    if (loadFactor(hashMap) >= hashMap->loadThres)
    {
        extend(hashMap);
    }
    int index = hashFunc(hashMap, key);
    Node *cur = hashMap->buckets[index];

    while (cur)
    {
        if (cur->pair->key == key)
        {
            strcpy(cur->pair->val, val);
            return;
        }
        cur = cur->next;
    }
    // 创建新节点
    Pair *newp = malloc(sizeof(Pair));
    newp->key = key;
    strncpy(newp->val, val, 63);
    newp->val[63] = '\0';

    
    Node *newnode = malloc(sizeof(Node));
    newnode->pair = newp;
    newnode->next = hashMap->buckets[index];
    hashMap->buckets[index] = newnode;

    hashMap->size++;
    return;
}

void extend(HashMapChaining *hashMap)
{
    /* 步骤提示：
     * 1) 暂存旧 buckets 与旧容量
     * 2) 扩容后重建新 buckets
     * 3) size 归零
     * 4) 遍历旧节点并重新 put 到新表
     * 5) 释放旧链表节点与旧 buckets
     */
    // 暂存原哈希表
    //     int oldCapacity = hashMap->capacity;
    //     Node **oldBuckets = hashMap->buckets;
    //     // 初始化扩容后的新哈希表
    //     hashMap->capacity *= hashMap->extendRatio;
    //     hashMap->buckets = (Node **)malloc(hashMap->capacity * sizeof(Node *));
    //     for (int i = 0; i < hashMap->capacity; i++) {
    //         hashMap->buckets[i] = NULL;
    //     }
    //     hashMap->size = 0;
    //     // 将键值对从原哈希表搬运至新哈希表
    //     for (int i = 0; i < oldCapacity; i++) {
    //         Node *cur = oldBuckets[i];
    //         while (cur) {
    //             put(hashMap, cur->pair->key, cur->pair->val);
    //             Node *temp = cur;
    //             cur = cur->next;
    //             // 释放内存
    //             free(temp->pair);
    //             free(temp);
    //         }
    //     }

    //     free(oldBuckets);
    // }

    // 直接移动旧节点的方法, 不需要释放旧节点
    Node **old_buckets = hashMap->buckets;
    int old_cap = hashMap->capacity;

    hashMap->capacity *= hashMap->extendRatio;
    // calloc 自动初始化为 NULL，无需手动循环置空
    hashMap->buckets = calloc(hashMap->capacity, sizeof(Node *));

    hashMap->size = 0;

    for (int i = 0; i < old_cap; i++)
    {
        Node *curr = old_buckets[i];
        while (curr)
        {
            Node *nx = curr->next;

            int new_index = hashFunc(hashMap, curr->pair->key);
            curr->next = hashMap->buckets[new_index];
            hashMap->buckets[new_index] = curr;

            curr = nx;
            hashMap->size++;
        }
    }

    free(old_buckets); // 节点已经移动, 不需释放
}

void removeItem(HashMapChaining *hashMap, int key)
{
    /* 步骤提示：
     * 1) 定位桶并维护 pre/cur 双指针
     * 2) 找到 key 后修改链并摘除节点
     * 3) 释放内存并维护 size
     */
    int index = hashFunc(hashMap, key);
    Node *pre = NULL;
    Node *cur = hashMap->buckets[index];
    
    while (cur)
    {
        if (cur->pair->key == key)
        {
            if(pre){
                // 非头节点
                pre->next = cur->next;
            }
            else{
                // 头节点
                hashMap->buckets[index] = cur->next;
            }
            
            free(cur->pair);
            free(cur);
            hashMap->size--;
            return;
        }
        pre = cur;
        cur = cur->next;
        
    }
}

void printMap(HashMapChaining *hashMap)
{
    /* 步骤提示：
     * 1) 逐桶遍历
     * 2) 输出桶内所有 key -> val
     */
    for (int i = 0; i < hashMap->capacity; i++)
    {
        Node *go = hashMap->buckets[i];
        while (go)
        {
            printf("%d -> %s\n", go->pair->key, go->pair->val);
            go = go->next;
        }
    }
}
