#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 键值对 */
typedef struct {
    int key;
    char val[64];
} Pair;

/* 链表节点 */
typedef struct Node {
    Pair *pair;
    struct Node *next;
} Node;

/* 链式地址哈希表 */
typedef struct {
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

HashMapChaining *newHashMapChaining() {
    /* 步骤提示：
     * 1) 分配 HashMapChaining 内存
     * 2) 初始化 size/capacity/loadThres/extendRatio
     * 3) 分配 buckets 并全部置空
     */
    abort();
}

void delHashMapChaining(HashMapChaining *hashMap) {
    /* 步骤提示：
     * 1) 遍历每个桶和链表节点
     * 2) 依次释放 pair 与 node
     * 3) 释放 buckets 与 hashMap 本体
     */
    abort();
}

int hashFunc(HashMapChaining *hashMap, int key) {
    /* 步骤提示：
     * 1) 使用 key 对 capacity 取模
     */
    abort();
}

double loadFactor(HashMapChaining *hashMap) {
    /* 步骤提示：
     * 1) 将 size 与 capacity 转成 double 再相除
     */
    abort();
}

char *get(HashMapChaining *hashMap, int key) {
    /* 步骤提示：
     * 1) 通过 hashFunc 定位桶
     * 2) 遍历链表查找 key
     * 3) 命中返回 val，未命中返回空串或 NULL
     */
    abort();
}

void put(HashMapChaining *hashMap, int key, const char *val) {
    /* 步骤提示：
     * 1) 检查负载因子，必要时先扩容
     * 2) 在桶内查找是否已有 key
     * 3) 有则更新，无则头插/尾插新节点
     * 4) 新增节点时维护 size
     */
    abort();
}

void extend(HashMapChaining *hashMap) {
    /* 步骤提示：
     * 1) 暂存旧 buckets 与旧容量
     * 2) 扩容后重建新 buckets
     * 3) size 归零
     * 4) 遍历旧节点并重新 put 到新表
     * 5) 释放旧链表节点与旧 buckets
     */
    abort();
}

void removeItem(HashMapChaining *hashMap, int key) {
    /* 步骤提示：
     * 1) 定位桶并维护 pre/cur 双指针
     * 2) 找到 key 后修改链并摘除节点
     * 3) 释放内存并维护 size
     */
    abort();
}

void printMap(HashMapChaining *hashMap) {
    /* 步骤提示：
     * 1) 逐桶遍历
     * 2) 输出桶内所有 key -> val
     */
    abort();
}
