


def main():
# 链表是线性表的一种。线性表是最基本、最简单、也是最常用的一种数据结构。
# 线性表中数据元素之间的关系是一对一的关系，即除了第一个和最后一个数据元素之外，其它数据元素都是首尾相接的。
# 线性表有两种存储方式，一种是顺序存储结构，另一种是链式存储结构。我们常用的数组就是一种典型的顺序存储结构。

# 相反，链式存储结构就是两个相邻的元素在内存中可能不是相邻的，每一个元素都有一个指针域，指针域一般是存储着到下一个元素的指针。
# 这种存储方式的优点是定点插入和定点删除的时间复杂度为 O(1)，不会浪费太多内存，添加元素的时候才会申请内存，删除元素会释放内存。
# 缺点是访问的时间复杂度最坏为 O(n)。

# 顺序表的特性是随机读取，也就是访问一个元素的时间复杂度是O(1)，链式表的特性是插入和删除的时间复杂度为O(1)。

# 链表就是链式存储的线性表。根据指针域的不同，链表分为单向链表、双向链表、循环链表等等。
    class ListNode:
        def __init__(self,val):
            self.val = val
            self.next = None

# 反转链表
# 单向链表
# 链表的基本形式是：1 -> 2 -> 3 -> null，反转需要变为 3 -> 2 -> 1 -> null。这里要注意：
# 访问某个节点 curt.next 时，要检验 curt 是否为 null。
# 要把反转后的最后一个节点（即反转前的第一个节点）指向 null。
        # in python next is a reversed word
        def reverse(self,head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev


# 双向链表
# 
# 和单向链表的区别在于：双向链表的反转核心在于next和prev域的交换，还需要注意的是当前节点和上一个节点的递推。
    class DListNode():

        def __init__ (self,val):
            self.val = val
            self.prev = self.next = null

        def reverse(self,head):
            curt = None
            while head:
                curt = head
                head = curt.next
                curt.next = curt.prev
                curt.prev = head
            return curt



# 快慢指针

# 快慢指针也是一个可以用于很多问题的技巧。
# 所谓快慢指针中的快慢指的是指针向前移动的步长，每次移动的步长较大即为快，步长较小即为慢，
# 常用的快慢指针一般是在单链表中让快指针每次向前移动2，慢指针则每次向前移动1。
# 快慢两个指针都从链表头开始遍历，于是快指针到达链表末尾的时候慢指针刚好到达中间位置，于是可以得到中间元素的值。
# 快慢指针在链表相关问题中主要有两个应用：

# 快速找出未知长度单链表的中间节点 设置两个指针 *fast、*slow 都指向单链表的头节点，
# 其中*fast的移动速度是*slow的2倍，当*fast指向末尾节点的时候，slow正好就在中间了。


# 判断单链表是否有环 利用快慢指针的原理，同样设置两个指针 *fast、*slow 都指向单链表的头节点，
# 其中 *fast的移动速度是*slow的2倍。如果 *fast = NULL，说明该单链表 以 NULL结尾，不是循环链表；
# 如果 *fast = *slow，则快指针追上慢指针，说明该链表是循环链


    class NodeCircle:
        def __init__(self,val):
            self.val = val
            self.next = None

        def has_circle(self,head):
            slow = head
            fast = head

            while (slow and fast):
                fast = fast.next
                slow = slow.next
                if fast:
                    fast = fast.next
                if fast == slow:
                    break
            if fast and slow and(fast==slow):
                return True
            else:
                return False
                
if __name__ == '__main__':
    main()


