#include <vector>
#include <stdexcept>   
using namespace std;
/* 列表类 */

class MyList {
  private:
    int *arr;             // 数组（存储列表元素）
    int arrCapacity = 10; // 列表容量
    int arrSize = 0;      // 列表长度（当前元素数量）
    int extendRatio = 2;   // 每次列表扩容的倍数

  public:
    /* 构造方法 */
    MyList() {
        arr = new int[arrCapacity];
    }

    /* 析构方法 */
    ~MyList() {
        delete[] arr;
    }

    /* 获取列表长度（当前元素数量）*/
    int size() {
        // 要求：返回当前有效元素数量。
        return 0;
    }

    /* 获取列表容量 */
    int capacity() {
        // 要求：返回底层数组容量。
        return 0;
    }

    /* 访问元素 */
    int get(int index) {
        // 要求：
        // 1) 检查索引是否越界，越界时抛出 out_of_range。
        // 2) 返回 index 位置的元素。
        return 0;
    }

    /* 更新元素 */
    void set(int index, int num) {
        // 要求：
        // 1) 检查索引是否越界，越界时抛出 out_of_range。
        // 2) 将 index 位置更新为 num。
    }

    /* 在尾部添加元素 */
    void add(int num) {
        // 要求：
        // 1) 若容量不足，先扩容。
        // 2) 在尾部插入 num。
        // 3) 更新元素数量。
    }

    /* 在中间插入元素 */
    void insert(int index, int num) {
        // 要求：
        // 1) 检查 index 合法性（按当前实现规则）。
        // 2) 必要时先扩容。
        // 3) 将 index 及其后元素整体后移一位。
        // 4) 在 index 处写入 num 并更新元素数量。
    }

    /* 删除元素 */
    int remove(int index) {
        // 要求：
        // 1) 检查索引是否越界。
        // 2) 记录并返回被删除元素。
        // 3) 将 index 后元素整体前移。
        // 4) 更新元素数量。
        return 0;
    }

    /* 列表扩容 */
    void extendCapacity() {
        // 要求：
        // 1) 按 extendRatio 扩容。
        // 2) 复制原有有效元素到新数组。
        // 3) 释放旧数组并更新容量。
    }

    /* 将列表转换为 Vector 用于打印 */
    vector<int> toVector() {
        // 要求：仅转换有效长度范围内的元素到 vector 并返回。
        return {};
    }
};

/* =========================
 * 参考答案（放在最下面）
 * ========================= */
class MyListAnswer {
  private:
    int *arr;
    int arrCapacity = 10;
    int arrSize = 0;
    int extendRatio = 2;

  public:
    MyListAnswer() {
        arr = new int[arrCapacity];
    }

    ~MyListAnswer() {
        delete[] arr;
    }

    int size() {
        return arrSize;
    }

    int capacity() {
        return arrCapacity;
    }

    int get(int index) {
        if (index < 0 || index >= size())
            throw out_of_range("索引越界");
        return arr[index];
    }

    void set(int index, int num) {
        if (index < 0 || index >= size())
            throw out_of_range("索引越界");
        arr[index] = num;
    }

    void add(int num) {
        if (size() == capacity())
            extendCapacity();
        arr[size()] = num;
        arrSize++;
    }

    void insert(int index, int num) {
        if (index < 0 || index >= size())
            throw out_of_range("索引越界");
        if (size() == capacity())
            extendCapacity();
        for (int j = size() - 1; j >= index; j--) {
            arr[j + 1] = arr[j];
        }
        arr[index] = num;
        arrSize++;
    }

    int remove(int index) {
        if (index < 0 || index >= size())
            throw out_of_range("索引越界");
        int num = arr[index];
        for (int j = index; j < size() - 1; j++) {
            arr[j] = arr[j + 1];
        }
        arrSize--;
        return num;
    }

    void extendCapacity() {
        int newCapacity = capacity() * extendRatio;
        int *tmp = arr;
        arr = new int[newCapacity];
        for (int i = 0; i < size(); i++) {
            arr[i] = tmp[i];
        }
        delete[] tmp;
        arrCapacity = newCapacity;
    }

    vector<int> toVector() {
        vector<int> vec(size());
        for (int i = 0; i < size(); i++) {
            vec[i] = arr[i];
        }
        return vec;
    }
};