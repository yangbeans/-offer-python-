# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:37:55 2019

@author: 11955
"""

"""
目录：
第一大部分：数据结构  链表、树、栈、队列、哈希表查找
第二大部分：循环、递归、查找、排序
第三大部分：动态规划
第四大部分：排列组合
第五大部分：其他

"""

import numpy as np


#第一大部分：数据结构  链表、树、栈、队列、哈希表查找
print("==【第一大部分：数据结构】==")
class PrintTree:
    def __init__(self):
        self.l_tin = []
        
    def tin_ergodic(self, root):
        if root != None:
            self.tin_ergodic(root.left)
            self.l_tin.append(root.val)
            self.tin_ergodic(root.right)
        return self.l_tin


#链表
#面试题6：从尾到头打印链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, pHead):
        # write code here
        #1 反转链表
        if not pHead:
            return []
        elif not pHead.next:
            last = pHead
        else:
            last = None
            while pHead:
                tmp = pHead.next
                pHead.next = last
                last = pHead
                pHead = tmp
        #2 求出结果
        arr = []
        while last:
            arr.append(last.val)
            last = last.next
        return arr


#面试题6：从头到尾打印链表
def printNode(pHead):
    if pHead == None:
        return None
    else:
        return printNode(pHead.next)

#*面试题18：删除链表的节点
"""
思路：
    <1>
    用三个指针p,c,n分别表示头节点、中间节点、末尾节点。
    <2>
    如果p一开始不与c相同，则保存当前p节点为ans，然后对比c是否与n相同，如果相同把n往后移一位，继续判断直到c与n不相同
    连接p和n节点，并删除p和n之间的节点(不包括p和n)
    然后节点p往后移一位，继续生成p,c,n。继续前面的操作。
    
    如果p一开始就和c相同，则在p前加一个新头节点，并保存该节点为ans，然后继续对比c是否与n相同，如果相同把n往后移一位，继续判断直到c与n不相同
    连接p和n节点，并删除p和n之间的节点(不包括p和n)
    然后节点p往后移一位，继续生成p,c,n
   
    <3>返回ans
    
"""
class Solution:
    def deleteDuplication(self, pHead):
        #1
        p = pHead
        c = pHead.next
        n = pHead.next.next
        
        #2 
        while p:
            if pHead and pHead.next and pHead.next.next:
                #如果p一开始就不等于c
                if p.val != c.val:
                    ans = p
                    #如果c一开始就等于n
                    if c.val == n.val:
                        while (c.val == n.val) and n.next != None:
                            n = n.next
                            c = c.next
                            
                        if c.val == n.val:
                            p.next = None
                        else:
                            p.next = n
                            c.next =None
                            
                    #如果c一开始就不等于n，就移动指针p
                    if p.next:      
                        pHead = p.next
                    p = pHead
                    c = pHead.next
                    n = pHead.next.next
                    
            if pHead and pHead.next and pHead.next.next == None:
                print(1)
    
    def deleteDuplication2(self, pHead):
        # write code here
        #1 先删除重复i后边的那个节点，直到i后边没有重复地节点。并且把节点i记录下来
        dupNodes = []
        p1 = pHead
        while pHead.next:
            print(pHead.val)
            #删除i之后重复的节点，并把这个节点保存下来
            if pHead.val == pHead.next.val:
                while pHead.val == pHead.next.val:
                    ###***删除链表的某一节点
                    tmp = pHead.next.next
                    pHead.next.next = None
                    pHead.next = tmp.next
                
                dupNodes.append(pHead.val)
                print("======")
                print(pHead.val)
                print("======")
                
            print(pHead.val)
            pHead = pHead.next
            print(pHead.val)
            print("--------------------------")
        return dupNodes
print("----------【18】删除链表的节点--------")
pHead = ListNode(1)
jl = pHead
pHead.next = ListNode(2)
pHead.next.next = ListNode(3)
pHead.next.next.next = ListNode(3)
pHead.next.next.next.next = ListNode(4)
pHead.next.next.next.next.next = ListNode(4)
pHead.next.next.next.next.next.next = ListNode(5)
pHead.next.next.next.next.next.next.next = ListNode(6)

s = Solution()

print(s.deleteDuplication2(jl))


#面试题22：链表中倒数第k个节点
"""
要点：
<1>普通链表listNode(单向链表)指针是从前往后指的，listNode的值是指针此时指的节点的值,listNode表示此时针指指在的这个节点。
如listNode:1->3->4->6->7, print(listNode) -->1  listNode = listNode.next, print(listNode.val) -->3
<2>链表不能直接输出第n个节点的值  用指针思想      链表内部比较抽象......
本题思路：创建一个list接收(append)链表从头到尾的节点值，然后输出list对应的位置的值
<3>python的优点，用一个数组装节点，然后再进行下一步处理
<4>链表理解的核心!!!：
    (1)pHead表示什么
    pHead(或listNode)即是一个节点也表示该链表的状态，比较抽象...... 链表是个抽象的东西。。。
    当print(pHead)时就是打印此时指针所在位置节点即以后的所有链表所有节点  例如思考pHead = pHead.next 此时的pHead
    l = []
    l.append(pHead)表示把此时指针指向的那个节点放入了数组l中
    (2)指针思想
<5>newHead = listNode(90)表示创建一个新链表(节点)，这个链表有一个节点，节点值为90
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def FindKthToTail(self, listNode, k):
        #1 求出链表的长度
        length = 0
        p1 = listNode  #链表是不可变数据结构， 相当于开创了一块新的内存空间1，让变量p1指向这块空间1
        p2 = listNode #相当于开创了一块新的内存空间2，让变量p2指向这块空间2
        while p1:
            length += 1
            listNode = listNode.next
        
        #2 算出倒数第k个节点的位置，遍历到该位置。
        idx = length - k
        count = 0
        while count < idx:
            p2 = p2.next
            count += 1
        return p2.val

class Solution_sec:
    def FindKthToTail(self, listNode, k):
        if k <= 0:
            return None
        
        #1 求出链表的长度length
        length = 0
        l_p = listNode
        while l_p:
            length += 1
            l_p = l_p.next
        if k > length:
            return None
        
        #2 倒数第k个链表的位置=>正数第length-k的位置
        idx = length - k
        
        #3 遍历到length-k的位置
        for i in range(idx):
            listNode = listNode.next
        return listNode.val

print("------【22】链表中倒数第k个节点-----")
pHead = ListNode(1)
jl = pHead
pHead.next = ListNode(2)
pHead.next.next = ListNode(3)
pHead.next.next.next = ListNode(4)
pHead.next.next.next.next = ListNode(5)

s2 = Solution_sec()
print(s2.FindKthToTail(jl, 2))
        

print("------打印链表中的某一节点-------")
#创建链表
pHead = ListNode(1)
jl = pHead
pHead.next = ListNode(2)
pHead.next.next = ListNode(3)
pHead.next.next.next = ListNode(4)
pHead.next.next.next.next = ListNode(5)
pHead.next.next.next.next.next = ListNode(6)
print(jl)


#打印链表中的某一节点  指针思想

print(jl.val)
print(jl.next.val)


#打印整个链表
print("------打印整个链表-------")
l = []
while jl:
    l.append(jl)
    jl = jl.next
print(l)
print(l[1])

    
#面试题23：链表中环的入口节点    数组、指针
"""
思路：
    1 求出环的长度loop_length：
        引入两个指针，同时在头节点起步，一快一慢，两个指针必定会在环内相遇。这样就可以求出环的长度了
    2 求出环的入口：
        两个指针，一个节点先走loop_length步，接着另一个指针也走，当两个指针相遇第一次的时候就是环的入口。

小结：
pHead移动后值是会改变的，如果要用某一个节点要提前用另一个变量保存起来
节点值不一定唯一，但节点一定是唯一： if pHead1 == pHead2: ......

"""
class Solution_RingEntr:
    def EntryNodeOfLoop(self, pHead):
        #1 求出链表的环的节点数m
        p1 = pHead
        p2 = pHead
        f1 = pHead
        f2 = pHead
        loop_num = 0
        while p1 == p2:
            count_pHead = p1
            val_pHead = p1
            p1 = p1.next
            p2 = p2.next.next
            
        count_pHead = p1
        val_pHead = p1
        while count_pHead:
            loop_num += 1
            count_pHead = count_pHead.next
            if count_pHead == val_pHead:
                break
            
        #2 用两个指针，其中一个指针先走m步，然后两个指针一起以同样的速度前移。当两指针第一次相逢的位置就是环的入口
        for i in range(loop_num):
            f1 = f1.next
        while True:
            if f1 == f2:
                return f1
            f1 = f1.next
            f2 = f2.next
        return None

class Solution_sec:
    def EntryNodeOfLoop(self, pHead):
        #1求出环的长度loop_length
        p1 = pHead
        p2 = pHead
        
        p1 = p1.next
        p2 = p2.next.next
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next.next
        
        p_save = p1
        p1 = p1.next
        loop_length = 1
        while p1 != p_save:
            loop_length += 1
            p1 = p1.next
        
        #2 求出环的入口
        p3 = pHead
        p4 = pHead
        
        for i in range(loop_length):
            p4 = p4.next
        while p3 == p4:
            p3 = p3.next
            p4 = p4.next
        return p3
    
    
#面试题24：反转链表
class Solution:
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        
        last = None
        while pHead:
            #1 因为之后的指针移动pHead会变动，先保存原始链表pHead的下一个节点，以便后边移动指针更新pHead时用
            tmp = pHead.next
            
            #2 把当前的pHead与反转链表的最新节点(头节点)相连，并更新反转链表的头节点
            pHead.next = last
            last = pHead
            
            #3 移动pHead的指针
            pHead = tmp
        
        return last


###***面试题25：合并两个排序的链表
"""
def Merge(pHead1, pHead2):   #pHead即是个节点，也表示该链表的状态(即指针指到哪了) print(pHead)时就是打印此时指针所在位置节点即以后的所有链表所有节点
    #创建一个空链表用来生成排序后的链表
    mergeHead = listNode(90) #创建一个新链表，这个链表有一个节点，节点值为90
    p = mergeHead ###***记下第一个节点，就相当于记下了整个链表了当mergeHead不断移动连接新节点时，print(p)就相当于打印了加入所有节点后的整个新链表了
    #先把listNode1或listNode2遍历完，只要有其中一个链表遍历完了，另一个链表剩下的节点都大于已遍历的节点的值
    
    while pHead1 and pHead2:
        if pHead1.val > pHead2.val:
            mergeHead.next = pHead2 #sequenceNode接入下一个新节点，该节点为链表2指针此时指向的节点
            pHead2 = pHead2.next
        else:
            mergeHead.next = pHead1
            pHead1 = pHead1.next
        
    if pHead1:
        mergeHead.next = pHead1
    if pHead2:
        mergeHead.next = pHead2
    return p.next
"""
pHead1 = ListNode(1)
jl = pHead1
pHead1.next = ListNode(3)
pHead1.next.next = ListNode(5)
pHead1.next.next.next = ListNode(7)
pHead1.next.next.next.next = ListNode(9)
pHead1.next.next.next.next.next = ListNode(11)

pHead2 = ListNode(2)
j2 = pHead2
pHead2.next = ListNode(4)
pHead2.next.next = ListNode(6)
pHead2.next.next.next = ListNode(8)
pHead2.next.next.next.next = ListNode(10)
pHead2.next.next.next.next.next = ListNode(12)


def Merge(pHead1, pHead2):
    mergeHead = ListNode(0)
    p = mergeHead
    while pHead1 and pHead2:
        if pHead1.val >= pHead2.val:
                mergeHead.next = pHead2
                pHead2 = pHead2.next
        else:
            mergeHead.next = pHead1
            pHead1 = pHead1.next
        mergeHead = mergeHead.next
    if pHead1:
        mergeHead.next = pHead1  #表示把链表1剩下的一坨全都给了合并链表
        
    if pHead2:
        mergeHead.next = pHead2
        
    return p.next

print("-----合并两个排序的链表-----")
print(Merge(pHead1, pHead2))


#面试题35：复杂链表的复制
"""
思路：
    1 复制主链表
    2 复制random
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None
        
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        #1 复制每个节点，并用next链接
        p0 = pHead
        pCopy = ListNode(0)
        p1 = pCopy
        while pHead:
            pCopy.next = pHead
            pHead = pHead.next
            pCopy = pCopy.next
        
        #2 复制random
        cpNode = p1.next
        cp_ans = cpNode
        
        while cpNode:
            raNode = p0.random
            cpNode.random = raNode
            p0 = p0.next
            cpNode = cpNode.next
        
        return cp_ans

class SolutionSec:
    # 返回 RandomListNode
    def Clone(self, pHead):
        #1 复制主链表
        p = ListNode(0)
        res1 = p
        pHead1 = pHead
        while pHead1:
            p.next = pHead1
            pHead1 = pHead1.next
            p = p.next
        
        #2 复制random
        res1 = res1.next
        res = res1
        pHead2 = pHead
        while pHead2:
            res1.random = pHead2.random
            pHead2 = pHead2.next
            res1 = res1.next
        return res
            
        
    
print("-----【35】复杂链表的复制---------")
"""
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node1.random = node3
node4.random = node2
"""
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(3)
node7 = ListNode(5)
node8 = ListNode("#")
node9 = ListNode(2)
node10 = ListNode("#")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

node1.random = node3
node4.random = node2

pNode = node1

s = Solution()
cp = s.Clone(pNode)
cp_ans = cp

def print_next_nodes(pHead):
    j1_next = []
    while pHead:
        j1_next.append(pHead.val)
        pHead = pHead.next
    return j1_next
    
def print_random_nodes(pHead):
    j1_random = []
    while pHead:
        if pHead.random:
            j1_random.append(pHead.random.val)
        pHead = pHead.next
    return j1_random

pNode = node1
print("cp_next", print_next_nodes(pNode))
pNode = node1
print("j1_random", print_random_nodes(pNode))
cp_ans = cp
print("cp_random", print_random_nodes(cp_ans))

print("-----------------------")
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(3)
node7 = ListNode(5)
node8 = ListNode("#")
node9 = ListNode(2)
node10 = ListNode("#")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

node1.random = node3
node4.random = node2

pNode = node1

s2 = SolutionSec()
res = s2.Clone(pNode)
pNode = node1
print("cp_next", print_next_nodes(pNode))
pNode = node1
print("j1_random", print_random_nodes(pNode))
cp_ans = res
print("cp_random", print_random_nodes(cp_ans))

#面试题36：二叉搜索树与双向链表
"""
思路：
    1 中序遍历求出排序的各个子节点
    2 把1中所求的节点连起来。每一个节点的left指向前一个节点，right指向后一个节点
    注：考虑边界问题
"""
class Solution:
    def __init__(self):
        self.nodes = [] 
        
    def Convert(self, pRootOfTree):
        # write code here
        #1 中序遍历求出排序的各个子节点
        self.nodes = self.tin(pRootOfTree)
        
        if len(self.nodes) == 0:
            return 
        if len(self.nodes) == 1:
            self.nodes[0].left = None
            self.nodes[0].right = None
            return self.nodes[0]
        
        #2 把1中所求的节点连起来。每一个节点的left指向前一个节点，right指向后一个节点
        nodes_len = len(self.nodes)
        for i in range(nodes_len):
            if i == 0:
                self.nodes[i].left = None
                self.nodes[i].right = self.nodes[i+1]
            elif i == nodes_len-1:
                self.nodes[i].left = self.nodes[i-1]
                self.nodes[i].right = None
            else:
                self.nodes[i].left = self.nodes[i-1]
                self.nodes[i].right = self.nodes[i+1]
        
        return self.nodes[0], self.nodes[-1]
        
    def tin(self, pRoot):
        if pRoot:
            self.tin(pRoot.left)
            self.nodes.append(pRoot)
            self.tin(pRoot.right)
        return self.nodes

class SolutionSec:
    def __init__(self):
        self.nodes = [] 
        
    def Convert(self, pRootOfTree):
        #1 通过中序遍历，将所有节点保存在一个数组中
        self.nodes = self.tin(pRootOfTree)
        
        #2 从头遍历这个数组，从第二个节点到倒数第二个节点的每个节点左节点指向它数组中的前一个节点，右节点指它向数组中的后一个节点
            # 第一个节点的左节点指向None,右节点指向后一个节点；最后一个节点头左节点指向它的前一个节点，右节点指向None
        len_nodes = len(self.nodes)
        if len_nodes == 0:
            return None
        if len_nodes == 1:
            return self.nodes[0]
        res = self.nodes[0]
        for i in range(len_nodes):
            if i == 0:
                self.nodes[i].left = None
                self.nodes[i].right = self.nodes[i+1]
            elif i == len_nodes-1:
                self.nodes[i].left = self.nodes[i-1]
                self.nodes[i].right = None
            else:
                self.nodes[i].left = self.nodes[i-1]
                self.nodes[i].right = self.nodes[i+1]
        return res
    
    def tin(self, pRootOfTree):
        if pRootOfTree:
            self.tin(pRootOfTree.left)
            self.nodes.append(pRootOfTree)
            self.tin(pRootOfTree.right)
        return self.nodes

print("-----二叉搜索树与双向链表------")
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

treeNode = TreeNode(10)
t1 = treeNode
treeNode.left = TreeNode(6)
treeNode.right = TreeNode(14)
treeNode.left.left = TreeNode(4)
treeNode.left.right = TreeNode(8)
treeNode.right.left = TreeNode(12)
treeNode.right.right = TreeNode(16)

s = Solution()
#print(s.Convert(t1))
p1, p2 = s.Convert(t1)
print("从前往后")
while p1:
    print(p1.val)
    p1 = p1.right
print("从后往前")
while p2:
    print(p2.val)
    p2 = p2.left



#树
#面试题7：重建二叉树
"""
要点：
1 构建树：给个启动节点 rootNode = TreeNode(x)  rootNode.left 表示rootNode这个节点下的左节点 rootNode.right 表示rootNode这个节点下的右节点
2 递归 构建递归函数返回当输入前序和中序遍历，该情况下树的根节点
3 指针思想，与链表相似。指针指在根节点，表示了一棵树
"""
"""
树结构的要点：
构建树、查找、打印树、已知某两个遍历重构树
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def reConstructBinaryTree(pre, tin): #reConstructBinaryTree函数的目的是输入前序和中序遍历，返回该情况下树的跟节点
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])
    else:
        flag = TreeNode(pre[0])  #启动... 
        flag.left = reConstructBinaryTree(pre[1:tin.index(pre[0])+1], tin[:tin.index(pre[0])])
        flag.right = reConstructBinaryTree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])
    return flag


class SolutionSec:
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            flag = TreeNode(pre[0])
            flag.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1], tin[:tin.index(pre[0])])
            flag.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])
        return flag
        

print("----------树结构------------------")
print("----------创建一棵树---------------")
treeNode = TreeNode(1)
t1 = treeNode
treeNode.left = TreeNode(2)
treeNode.right = TreeNode(3)
treeNode.left.left = TreeNode(4)
treeNode.left.right = TreeNode(5)
treeNode.right.left = TreeNode(6)
treeNode.right.right = TreeNode(7)
print("-----------遍历一棵树------------")
print(t1.left.val)

reConstructBinaryTree([3,9,20,15,7], [9,3,15,20,7])




#面试题8：二叉树的下一个节点
"""
思路： 给出具体例子，分类讨论找规律
    如果该节点有右节点
    如果该节点没有右节点
        一直回溯直达找到父节点的左节点是该节点的时候，这个时候的节点的父节点就是答案
"""
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:       
    def GetNext(self, pNode):
        if pNode is None: #情况0 如果节点不存在，返回None
            return None
        if pNode.right:#情况1 如果该节点的右节点存在，往右查找下一个节点，如果这个节点还有左节点，一直查找直到找到这边的最左节点
            res = pNode.right
            while res.left:
                tmp = res.left
                res = tmp
            return res
        
        #情况2 如果该节点没有右节点...  
        p = pNode
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:#如果是父节点的左节点，直接返回父节点
                return tmp
            pNode = tmp#如果不是父节点的左节点(即父节点的右节点)，令pNode为父节点，再进入循环判断，
                      #直到pNode等于父节点的左节点时返回父节点;或者直到while程序退出，返回None,这种情况的pNode是左右的叶节点

#树中序遍历的下一个节点
class SolutionSec:       
    def GetNext(self, pNode):
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        else:
            while pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                pNode = pNode.next
            return None
   
#树前序遍历的下一个节点  
"""
思路：
    如果该节点有左节点，左节点底下最左的那个点就是答案
    如果该节点有右节点(且没有左节点),该节点的右节点底下最左的节点就是答案
    如果该节点是叶节点：
        如果该节点是父节点的右节点，父节点就是答案
        如果该节点是父节点的左节点：
            如果父节点有右节点，父节点的右节点底下最左的节点就是答案
            如果父节点没有右节点，父节点就是答案
"""
class SolutionSecPre:       
    def GetNext(self, pNode):
        p = pNode
        #如果该节点有左节点
        if p.left:
            while p.left:
                p = p.left
            return p
        elif p.right:
            p2 = p.right
            while p2.left:
                p2 = p2.left
            return p2
        else:
            if p.next.right == p:
                return p.next
            if p.next.left == p:
                if p.next.right:
                    p2 = p.next.right
                    while p2.left:
                        p2 = p2.left
                    return p2
                else:
                    return p.next
    

print("-------【8】二叉树的下一个节点----")


#面试题26：树的子结构   递归
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        ans = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                ans = self.is_subtree(pRoot1, pRoot2)
            if ans != True:
                ans = self.HasSubtree(pRoot1.left, pRoot2)
            if ans != True:
                ans = self.HasSubtree(pRoot1.right, pRoot2)
            return ans
    
    def is_subtree(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        
        return self.is_subtree(pRoot1.left, pRoot2.left) and self.is_subtree(pRoot1.right, pRoot2.right)
    
    
print("-------【26】树的子结构---------")
treeNode = TreeNode(1)
t1 = treeNode
treeNode.left = TreeNode(2)
treeNode.right = TreeNode(3)
treeNode.left.left = TreeNode(4)
treeNode.left.right = TreeNode(5)
treeNode.right.left = TreeNode(6)
treeNode.right.right = TreeNode(7)

treeNode = TreeNode(3)
t2 = treeNode
treeNode.left = TreeNode(6)
treeNode.right = TreeNode(7)

s = Solution()
print(s.HasSubtree(t1, t2))


#用递归思想求一棵树节点的值的和
class Solution:
    def __init__(self):
        self.res = 0
    def treenodes_sum(self, pRoot):
        if pRoot:
            self.res += pRoot.val
            self.treenodes_sum(pRoot.left) #不断递归，当不满足条件时，会跳到下面那个函数执行
            self.treenodes_sum(pRoot.right)#不断递归，当不满足条件且为右时，跳出到父节点处执行
        return self.res #定义一个全局变量量记录和，当上面所有程序和递归函数执行完之后，才轮到return执行。
print("----用递归思想求一棵树节点的值的和---")
s = Solution()
print(s.treenodes_sum(t1))

#用递归的思想求根节点的值，只有叶节点的值已知。其中根节点之和等于左右两节点值之和，根节点的左节点等于自身左右两节点之和，
#根节点的右节点也是。


        
#面试题27：二叉树的镜像
"""
思路：
    递归问题，根据思路，一步一步画出“图”，然后根据"图"写代码
"""
def mirroir(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    mirroir(root.left)
    mirroir(root.right)
    
class SolutionSec:
    def mirroir(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.mirroir(root.left)
            self.mirroir(root.right)
        return root

print("-------【27】二叉树的镜像----")
treeNode = TreeNode(1)
t1 = treeNode
treeNode.left = TreeNode(2)
treeNode.right = TreeNode(3)
treeNode.left.left = TreeNode(4)
treeNode.left.right = TreeNode(5)
treeNode.right.left = TreeNode(6)
treeNode.right.right = TreeNode(7)

s2 = SolutionSec()
pt = PrintTree()
root = s2.mirroir(t1)
print(pt.tin_ergodic(root))


  
###***面试题28：对称的二叉树
"""
is_same(2, 2)
    is_same(4, 4) and is_same(5,5)
        (is_same(None, None) and is_same(None, None)) and (is_same(None, None) and is_same(None, None)) ==> (True and True) and (True and True)
==>True

思路： 这道递归题和【26】树的子结构类似，根据题目要求先用一个判别函数判断是否为真
    1 用一个函数is_dc判断两棵树是否对称
    2 把待判别的那棵树的pRoot.left, pRoot.right输入到判别函数is_dc中
    判别两棵树是否对称的思路：
        如果p1和p2都存在：
            如果p1.val!=p2.val:
                直接返回False
            否则：
                继续is_dc(p1.leFt, p2.right) and is_dc(p1.right, p2.left)
        否则：
            返回True
"""
class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
            return True
        
        def is_same(p1, p2):
            if not p1 and not p2:
                return True
            if p1 and p2 and p1.val == p2.val:
                return is_same(p1.left, p2.right) and is_same(p1.right, p2.left)
            return False
        return is_same(pRoot.left, pRoot.right)

class SolutionSec:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
            return False
        if pRoot.left is None or pRoot.left is None:
            return False
        return self.is_dc(pRoot.left, pRoot.right)
    
    #函数功能：判断两棵树是否对称
    def is_dc(self, p1, p2):
        if p1 and p2:
            if p1.val != p2.val:
                return False
            return self.is_dc(p1.left, p2.right) and self.is_dc(p1.right, p2.left)
        return True
    
print("------【28】对称的二叉树-----")
treeNode = TreeNode(1)
t1 = treeNode
treeNode.left = TreeNode(2)
treeNode.right = TreeNode(2)
treeNode.left.left = TreeNode(4)
treeNode.left.right = TreeNode(5)
treeNode.right.left = TreeNode(5)
treeNode.right.right = TreeNode(4)

s2 = SolutionSec()
print(s2.isSymmetrical(t1))


        

#面试题32：从上往下打印二叉树 
def PrintFromTopToBottom(root):
    if root is None:
        return []
    
    q = [root]   #队列，其实可以直接用一个list表示，进队列：append;出队列：.pop(0)
    l = []
    while len(q):
        t = q.pop(0)
        l.append(t.val)
        if t.left:
            q.append(t.left)
        if t.right:
            q.append(t.right)
    return l

#从上到下按层打印二叉树
"""
思路：
    用两个队列q1，q2来分别接单双层的节点。q1 = [pRoot], q2 = []
    用print_single，先按现进先出接q1里的节点的值，同时把该节点的left,right节点放入q2中。
    当q1队列为空时，把print_single保存在print_array。以同样的方法对q2操作，把print_double保存在print_array
    如此反复，直到q1,q2都为空。返回print_array
"""
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        #边界情况
        if pRoot == None:
            return []
        
        q1 = [pRoot]
        q2 = []
        print_array = []
        while q1 or q2:
            print_single = []
            while q1:
                node = q1.pop(0)
                print_single.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            if print_single:
                print_array.append(print_single)
                
                
            print_double = []
            while q2:
                node = q2.pop(0)
                print_double.append(node.val)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            if print_double:
                print_array.append(print_double)
        
        return print_array

print("----【32】从上到下按层打印二叉树----")
treeNode = TreeNode(8)
t1 = treeNode
treeNode.left = TreeNode(6)
treeNode.right = TreeNode(10)
treeNode.left.left = TreeNode(5)
treeNode.left.right = TreeNode(7)
treeNode.right.left = TreeNode(9)
treeNode.right.right = TreeNode(11)

s = Solution()
print(s.Print(t1))


#之字形打印二叉树
def print_Z_tree(root):
    print_list = []
    stack1 = [root]
    stack2 = []
    while stack1 or stack2:
        while stack1:
            r = stack1.pop()
            print_list.append(r.val)
            if r.left:
                stack2.append(r.left)
            if r.right:
                stack2.append(r.right)
        while stack2:
            r = stack2.pop()
            print_list.append(r.val)
            if r.right:
                stack1.append(r.right)
            if r.left:
                stack1.append(r.left)
    return print_list


#面试题33：二叉搜索树的后序遍历序列
"""
思路：
    二叉搜索树知道后序就已经知道前序。本问题实质是在求给定一个中序遍历、一个后续遍历，判断这两个遍历能不能重组一棵二叉树
    判断这两个遍历能不能重组一棵二叉树的思路：
        如果中序数组和后序数组的排序后不一样，直接返回False
        否则，一直递归继续，重新分割中序、后序，直到中序(或后序)数组的长度为1且中序数组和后序数组的排序后一样，则返回True
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        tin = sorted(sequence)
        return self.is_tree(tin, sequence)
    
    #函数功能：给定两组数组tin,las，可能是中序和后序，判断这两个数组能否组成一棵树
    def is_tree(self, tin, las):
        if len(las) == 0:
            return True
        arr1 = sorted(tin)
        arr2 = sorted(las)
        if arr1 != arr2:
            return False
        return self.is_tree(tin[:tin.index(las[-1])], las[:tin.index(las[-1])]) and self.is_tree(tin[tin.index(las[-1])+1:], las[tin.index(las[-1]):-1])
 
class SolutionSec:
    def VerifySquenceOfBST(self, sequence):       
        tin = sorted(sequence)
        return self.is_tree(tin, sequence)
    
    #函数功能：给出中序和后续数组，判断这两个数组的节点能不能组成一棵树
    def is_tree(self, tin, las):
        if len(las) == 0: #边界情况
            return False
        
        if sorted(tin) != sorted(las):
            return False
        if len(las) > 1:
            return self.is_tree(tin[:tin.index(las[-1])], las[:tin.index(las[-1])]) and self.is_tree(tin[tin.index(las[-1])+1:], las[tin.index(las[-1]):-1])
        return True
    
print("------【33】二叉搜索树的后序遍历序列------")
s = Solution()
print(s.VerifySquenceOfBST([5,7,6,9,11,10,8]))

s2 = SolutionSec()
print(s2.VerifySquenceOfBST([5,7,6,9,11,10,8]))



#面试题34：二叉树中和为某一值的路径
"""
递归代码编写总结：
<1>将思路在稿纸呈现，参考前序遍历的代码思路笔记。
<2>根据递归代码逐层的逻辑，把步骤<1>中的思路表达为代码。

例：t1树[10,5,12,4,7]  22
f(10)
10入stack0
f(10.left)=f(5)
            5入stack0
            f(5.left)=f(4)
                        4入stack0
                        f(4.left)=f(None) 跳出该层的当前语句，进入下一个语句
                        f(4.right)=f(None) 跳出该层的当前语句，进入下一个语句需求
                        【语句块A】:
                        如果遇到叶节点(即4.left==None and 4.right==None，则4就是叶节点)，判断stack0中的值之和是否为
                        指定的值(这里是22)：
                            如果是，将该stack0的路径记录下来，并且stack0弹出一个节点；
                            如果不是，stack0弹出一个节点
                        执行完【语句块A】后，这是该层函数的最后一条语句，跳出该层
                        
            f(5.right)=f(7)
                        7入stack0
                        f(7.left)=f(None) 跳出该层的当前语句，进入下一个语句
                        f(7.right)=f(None) 跳出该层的当前语句，进入下一个语句需求
                        【语句块A】
                        执行完【语句块A】后，这是该层函数的最后一条语句，跳出该层
                        
f(10.right)=f(12)
            12入stack0
            f(12.left)=f(None)
            f(12.right)=f(None)
            【语句块A】
            执行完【语句块A】后，这是该层函数的最后一条语句，跳出该层。为最后一层，函数执行完毕！
            
"""

class Solution:
    def __init__(self):
        self.stack0 = []
        self.ans = []
    
    def FindPath(self, root, expectNumber):
        #print(self.stack0)
        #边界情况
        if root == None:
            return []
        
        self.stack0.append(root.val)
        if root.left:
            self.FindPath(root.left, expectNumber)
        if root.right:
            self.FindPath(root.right, expectNumber)
            
        if sum(self.stack0) == expectNumber and root.left == None and root.right == None:#当满足该节点是叶节点且和满足要求是才可记录为路径
            self.ans.append(self.my_copy(self.stack0)) ###***stack0是引用，会不断变化，用my_copy()函数让其值保留
            
        if len(self.stack0) != 0:
            self.stack0.pop()
        return self.ans
    
    ###***stack0是引用，会不断变化，用copy()函数让其值保留
    def my_copy(self, stack):
        copy_stack = []
        len_stack = len(stack)
        for i in range(len_stack):
            copy_stack.append(stack[i])
            
        return copy_stack
    
print("------【34】二叉树中和为某一值的路径-------")
treeNode = TreeNode(8)
t1 = treeNode
treeNode.left = TreeNode(6)
treeNode.right = TreeNode(10)
treeNode.left.left = TreeNode(5)
treeNode.left.right = TreeNode(7)
treeNode.right.left = TreeNode(9)
treeNode.right.right = TreeNode(11)

s = Solution()
print(s.FindPath(t1, 15))


#*面试题37：序列化二叉树
"""
思路：
    序列化、反序列化都是递归的过程，直接按递归的编程思路做就可以。纸上写出递归过程，按递归过程编写程序
"""
class Solution:
    def __init__(self):
        self.flag = -1
        
    #序列化
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
    
    def Serialize2(self, root):
        if root is None:
            self.nodesval += "#,"
        if root:
            self.nodesval += str(root.val)+","
            self.Serialize(root.left)
            self.Serialize(root.right)
        
        return self.nodesval
        
        
    #反序列化
    def Deserialize(self, str_nodesval):
        l = str_nodesval.split(",")
        self.flag += 1
        
        if self.flag >= len(l):#如果flag大于或等于这些节点值(包括空节点“#”)得个数,返回None,即跳出该函数
            return None
        
        pHead = None
        if l[self.flag] != "#":
            pHead = TreeNode(int(l[self.flag])) ###***最后直接返回pHead就是头节点
            pHead.left = self.Deserialize(str_nodesval)
            pHead.right = self.Deserialize(str_nodesval)
        
        return pHead
        
            
print("------【37】序列化二叉树-------")   
s = Solution()
print("nodesval     :", s.Serialize(t1))

t_now = s.Deserialize(s.Serialize(t1))
print("nodesval_test:", s.Serialize(t_now))




#栈和队列    
#面试题9：用两个栈实现队列
#stack1用来接收进，stack2用来出
class Queue:
    def __init__(self, stack1, stack2):
        self.stack1 = [] 
        self.stack2 = []
    def appendTail(self, node):
        stack1.append(node)
    def deleteHead(self):#如果stack2不为空，直接pop(),如果stack2为空，把stack1中的数aooend到stack2然后stack2再pop()
        if self.stack2==[]:
            while self.stack1:
                self.stack2.append(self.stack1)
            stack2.pop()
        return stack2.pop()
         
"""
用两个队列实现栈的功能
思路：
    在弹出后进入操作完之后总要让一个队列为空，这个队列是缓冲区，把另一个队列中的元素收入只剩下要弹出的一个。
"""
    
#面试题30：包含min函数的栈     辅助栈  全局变量
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        # write code here
        if (not self.min_stack) or (node <= self.min_stack[-1]):
            self.min_stack.append(node)
        self.stack.append(node)
        
    def pop(self):
        # write code here
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min_(self):
        # write code here
        if not self.min_stack:
            return "error!!"
        return self.min_stack[-1]
    
print("----------min函数的栈---------")
stack = Solution()
stack.push(3)
stack.push(8)
print(stack)
print(stack.min_())

#面试题31：栈的压入、弹出序列   for {while...}
def IsPopOrder(pushV, popV):
    stack = []
    for i in popV:
        stack.append(i)
        while (len(stack) != 0) & (stack[-1]==popV[0]):
            stack.pop()
            popV.pop(0)
    if len(stack)!=0:
        return False
    return True



#第二大部分：循环、递归、查找、排序
print("=【第二大部分：循环、递归、查找、排序】=")
#哈希表查找  -->字典
#面试题50：第一个只出现一次的字符
#*一、字符串中第一个只出现一次的字符,及位置 从第0为算起
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) == 0:
            return -1
        ###***字典的用法
        d = {}
        for i in s:
            if i in d:
                d[i] += 1###***如果i是字典d的key，则往相应key的加1
            else:
                d[i] = 1#如果i不是字典里的key,把i放入字典中,令对应的val为1，字典中的每个key都是唯一的，字符按出现的先后顺序
        
        #找出只出现一次的字符
        flag = 0 ###***立个flag
        for k, v in d.items():###***items()函数，返回字典迭代的key，val对
            if v == 1:
                flag = 1
                break
                
        if flag == 1:
            idx = 0
            for i in s:
                if i == k:
                    return idx
                idx += 1
                
        if flag == 0:
            return -1
        
        
    
print("-------【50】第一个只出现一次的字符--------")
s = Solution()
print(s.FirstNotRepeatingChar("NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp"))



#2.4 算法和数据操作
#2.4.1 循环和递归
#递归
"""
递归三要素：
<1>判断是否可以递归
<2>拆解 (return ......)
<3>递归出口 (if ....)
"""
def diguiTest1(n):
    if n <= 0:
        return 0
    
    #递归出口
    if n == 1:
        return 1
    return n + diguiTest1(n-1)

#面试题10：斐波那契数列
#题目一：求斐波那契数列的第n项(p74)
class Solution:
    def Fibonacci(n):
        if n <= 0:
            return -1
        if n == 1:
            return 0
        if n == 2:
            return 1
        return Fibonacci(n-2) + Fibonacci(n-1)
    
    def Fibonacci2(n):
        if n <= 0:
            return -1
        if n == 1:
            return 0
        if n ==2:
            return 1
        right = 0
        left = 1
        final = 0
        for i in range(n-2):
            final = right + left
            right = left
            left = final
        return final

#题目二：青蛙跳台阶问题(p77)
class Solution:
    def skipStep(n):
        if n <= 0:
            return -1
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return skipStep(n-1) + skipStep(n-2)


#2.4.2 查找和排序
#排序
#实现冒泡排序 
"""
从第i轮剩余的数组中找出最小(或最大)的数(第i个数不断在更新，遇到比它更小的就更新)，
时间复杂度：O(n^2)
"""
def bubble_sort(seq):
    # 冒泡排序
    count = len(seq)
    for i in range(0, count):
        for j in range(i + 1, count):
            if seq[i] > seq[j]:
                seq[i], seq[j] = lists[j], lists[i]
    return lists


#选择排序
"""
时间复杂度：O(n^2)
从第i轮剩余的数组中找出该轮最小(或最大)的一个数的index,然后把这个index对应的数与整体数组的第i个位置的数交换
与冒泡排序思路很像，但操作次数比冒泡排序好，整体性能比冒泡排序好
"""
def selection_sort(arr):
    length_arr = len(arr)
    for i in range(length_arr-1):
        min_idx = i
        for j in range(i+1, length_arr):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr


#插入排序
"""
插入排序最坏情况的时间复杂度为O(n^2),最好情况的时间复杂度为O(n)。适合用在部分或大部分已排好序的情况。

插入排序的工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
步骤：(以由小到大排序为例)
从第一个元素开始，该元素可以认为已经被排序
    取出下一个元素，在已经排序的元素序列中从后向前扫描
    如果被扫描的元素（已排序）大于新元素，将该元素后移一位
    重复步骤3，直到找到已排序的元素小于或者等于新元素的位置，内层for停止
    将新元素插入到该位置后
重复步骤2~5
例：
    [3,5,2,8,4,7] --> i=1 [3,5,2,8,4,7] --> i=2 ([3,2,5,8,4,7]--[2,3,5,8,4,7]) [2,3,5,8,4,7] 
    --> i=3 [2,3,5,8,4,7] --> i=4 ([2,3,5,4,8,7]--[2,3,4,5,8,7]) --> i=5 [2,3,4,5,7,8]
"""
def insert_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        for j in range(i-1, -1, -1):
            if x < arr[j]:
                arr[j+1] = arr[j] 
                arr[j] = x
            else:
                break ###***因为前面的是已排序
    return arr

print("------【插入排序】-------")
print(insert_sort([3,5,2,8,4,7]))



#归并排序   递归
"""
原理见https://www.cnblogs.com/shiqi17/p/9696301.html
时间复杂度：O(nlogn)

归并排序递归代码的思路解析：以[2,6,3,8,1]为例
mid=5//2=2
left=ms([2,6])
        mid=2//2=1
        left=ms([2]) ==> [2]  #该层的left = merge_sort(lists[:middle])执行完毕，跳出该语句，
                                #进入到该层的下一个语句right = merge_sort(lists[middle:])
        right=ms([6]) ==> [6] #该层的第二个(最后一个)语句执行完毕，跳出该层
left=merge([2,6])==>[2,6]

right=ms([3,8,1])
        mid=3//2=1
        left=ms([3]) ==> [3]
        right=ms([8,1])
                mid=2//2=1
                left=ms([8]) ==> [8]
                right=ms([1]) ==> [1]
        right=merge([8], [1])==>[1,8]
right=merge([3], [1,8])==>[1,3,8]

final = merge([2,6], [1,3,8]) ==> [1,2,3,6,8]
"""
class Solution:
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)
    
    #对有序的数组a1, a2 merge,仍然得到有序的数组
    def merge(self, arr1, arr2):
        mer_res = []
        p1 = 0
        p2 = 0
        
        len1 = len(arr1)
        len2 = len(arr2)
        while True:
            if p1 >= len1 or p2 >= len2:
                break
            if arr1[p1] <= arr2[p2]:
                mer_res.append(arr1[p1])
                p1 += 1
            else:
                mer_res.append(arr2[p2])
                p2 += 1
        
        if p1 >= len1:
            for i in range(p2, len2):
                mer_res.append(arr2[i])
        if p2 >= len2:
            for j in range(p1, len1):
                mer_res.append(arr1[j])
        return mer_res
            
        
print("--------【归并排序】----------") 
s =Solution()
print(s.merge([1,3,9], [1,3,8]))
print(s.merge_sort([2,6,3,8,1]))
        


#实现快速排序   递归
"""
时间复杂度：O(nlogn)
"""
def quickSort(data):
    if len(data) == 0:
        return []
    base = data[0]
    return quickSort([x for x in data[1:] if x < base]) + [base] + quickSort([x for x in data[1:] if x >= base])


class Solution_QuickSort:
    def quickSort(self, arr, start, end):
        if start < end:
            pivot_index = self.partition(arr, start, end)
            self.quickSort(arr, start, pivot_index)
            self.quickSort(arr, pivot_index+1, end)
            
        return arr
    
    def partition(self, arr, start, end):
        pivot_index = start
        pivot = arr[pivot_index]
        for i in range(start+1, end):#让除了pivot外的所有数与pivot对比
            if arr[i] < pivot:
                pivot_index += 1#如果有数小于pivot，分割点pivot_index+1
                if i != pivot_index:#如果该数既小于pivot又不等于分割点的index，则交换该数到分割点的位置
                    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
        arr[start], arr[pivot_index] = arr[pivot_index], arr[start]#循环结束后，把pivot外的所有数都分成两大块，交换让pivot回到本该的位置pivot_index

        return pivot_index

class Solution:
    def sort(self, arr, start, end):
        if start < end:
            pivot_index = self.partition(arr, start, end)
            self.sort(arr, 0, pivot_index)
            self.sort(arr, pivot_index+1, end)
            return arr
    
    
    #函数功能:在一次分割中，在待排序的数组中通过start,end找到操作的部分数组，将其排成左、中、右三大部分，并返回中间部分的idx(即分割点)
    """
    这个过程要保证：
    1 始终做比较的那个数不能变
    2 每找到一个小于等于pivot(固定值)后分割点要更新到最新分割点(比如找到了3个小于等于pivot时，包括自身一个pivot_index=4)
    3 找到的满足小于等于pivot的数要保护起来，不能丢(保证<=pivot_index范围内的数不能被改变);并且最后更新完，数组中的元素不能改变
    4 分割点的数组要等于pivot，所以在还没有遍历完要保护pivot最初那个位置的值不被调换(其实3就已经满足要求了)
    """
    def partition(self, arr, start, end):
        pivot_index = start #pivot用来记录分割点的位置
        pivot = arr[pivot_index] #用来记录这一次分组时始终被比较的那个数值
        
        for i in range(start+1, end):
            if arr[i] <= pivot:
                if i == pivot_index+1:#如果
                    pivot_index += 1
                else:
                    arr[i], arr[pivot_index+1] = arr[pivot_index+1], arr[i]
                    pivot_index += 1
        arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
        return pivot_index
                
                    
    
print("------------【快速排序】----------")
solution_QuickSort = Solution_QuickSort()
print(solution_QuickSort.quickSort([3,2,1,4,0,8,9],0,7))

s = Solution()
print(s.sort([5,4,5,7,3,6,9,4], 0, 8))
    

###***用时间复杂度为O(n)实现查找一个数组的第k大的数
"""
partition的思路(以从大到小排序为例)：
整体思路：随机选一个数(一般选数组的第一个数)，把大于等于该数的放左边，小于该数的放右边
细节：先把第0位留着，不断找比它大的数依次放在第1位，第2位...并记录比较完之后该数最后所在的位置(pivot_index)。
    最后把arr[0]和arr[pivot_index]调换，得到一次partition后的数组。
    例：对[4,8,5,2,3,6,7]partition
    [4,8,5,2,3,6,7] i=1,pivot_index=0 --> [4,8,5,2,3,6,7] i=2,pivot_index=1-->
    [4,8,5,2,3,6,7] i=3,pivot_index=1-->...-->[4,8,5,2,3,6,7] i=4,pivot_index=1-->
    [4,8,5,6,3,2,7] i=5,pivot_index=2-->[4,8,5,6,7,2,3] i=6,pivot_index=3-->
    [7,8,5,6,4,2,3]
"""
class Solution_Findkth:
    def partition(self, arr, start, end):
        #if start < end:
        pivot_index = start
        pivot = arr[pivot_index]
        for i in range(start+1, end):
            if arr[i] > pivot:
                pivot_index += 1
                if i != pivot_index:
                    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
        arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
        return pivot_index, arr
        #elif start == end:
        #    return start
        #else:
        #    return 
    

    def find_kth(self, arr, start, end, k):
        if k <= 0 or k > len(arr):
            return None
        
        while start < end:
            pivot_index, arr = self.partition(arr, start, end)
            if pivot_index == k-1:
                return arr[pivot_index]
            if pivot_index > k-1:
                end = pivot_index
            else:
                start = pivot_index + 1###***
        

print("--用时间复杂度为O(n)实现查找一个数组的第k大的数--")
sfkth = Solution_Findkth()
print(sfkth.partition([8, 7, 5, 6, 4, 2, 3], 2, 4))
print(sfkth.find_kth([4,8,5,5,5,2,3,6,7], 0, len([4,8,5,5,5,2,3,6,7]), 5))


#面试题11：旋转数组的最小数字(p82)    找题目规律 二分查找法
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        L = 0
        R = len(rotateArray) - 1
        data = rotateArray[-1]
        while L < R:
            mid = L + (R-L)//2
            if rotateArray[mid] > data:
                L = mid + 1
            else:
                R = mid
        
        if rotateArray[mid] > rotateArray[mid+1]: ###***二分法猜的时候判断临界点的双保险
            mid = mid + 1
        
        return rotateArray[mid]
            
        
        
    def minNumberInRotateArray2(self, rotateArray):
        
        firstIndex = 0
        finalIndex = len(rotateArray)
        while (finalIndex - firstIndex) != 1:
            midIndex = firstIndex + (finalIndex - firstIndex)//2
            if rotateArray[0] > rotateArray[midIndex]:
                firstIndex = firstIndex
                finalIndex = midIndex
            if rotateArray[0] <= rotateArray[midIndex]: #"="特殊情况
                firstIndex = midIndex
                finalIndex = finalIndex
                
        return rotateArray[finalIndex]
    
    
print("----------【11】旋转数组的最小数字-----")
s = Solution()
print(s.minNumberInRotateArray([6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]))




#第三大部分：动态规划
print("======【第三大部分：动态规划】=====")

"""
动态规划总结：
步骤：
<1>判断是否能用动态规划 动态规划应用常见场景：(1)求最优解，如小偷偷金店、(2)计数问题，如跳台阶
<2>观察规律   递归.....
<3>由大往小分析，把大问题化成子问题，在把子问题化成子子问题，找出状态转移方程
<4>由小往大分析
<5>确定边界
<6>解决问题
    创建一个数组装一个个子问题的结果
    最后装的结果就是最后解决问题的结果


"""
#面试题14：剪绳子   
def f(n):
    i_max_num = np.zeros(n)
    i_max_num[0] = 1
    i_max_num[1] = 1
    i_max_num[2] = 2
    
    for i in range(3, n):
        products = []
        for j in range(i):
            products.append(i_max_num[j]*i_max_num[i-j])
        i_max_num[i] = max(products)
    return i_max_num[n-1]

#例：有一个矩阵map，它每个格子有一个权值。从左上角的格子开始每次只能向右或者向下走，最后到达右下角的位置，
#路径上所有的数字累加起来就是路径和，返回所有的路径中最小的路径和。
#思路：为了求出到达当前格子的最短路径，我们就要先去考察那些能到达当前这个格子的格子。状态转移方程：S[i][j]=A[i][j] + min(S[i-1][j], if i>0 ; S[i][j-1], if j>0)
    

#面试题42：连续子数组的最大和     动态规划
class Solution:
    def FindGreatestSumOfSubArray1(self, array):
        #1找出可能的最大子数组的值
        may_max = [array[0]]
        arr_len = len(array)
        for i in range(1, arr_len):
            if may_max[i-1] >= 0:
                may_max.append(may_max[i-1] + array[i])
            else:
                may_max.append(array[i])
        
        #2 从may_max找出最大值，就是所求
        max_val = self.get_max(may_max)
        return max_val
    
    def FindGreatestSumOfSubArray2(array):
        _max = 0
        b = 0
        for i in range(len(array)):
            if b < 0:
                b = array[i]
            else:
                b += array[i]
            if _max < b:
                _max = b
        return _max
    
    def get_max(self, may_max):
        
        start = 0
        end = len(may_max)
        while start < end:
            pivot_index, may_max = self.partition(may_max, start, end)
            if pivot_index == 0:
                return may_max[pivot_index]
            if pivot_index > 0:
                end = pivot_index
            else:
                start = pivot_index + 1
    
    def partition(self, arr, start, end):
        pivot_index = start
        pivot = arr[pivot_index]
        for i in range(start+1, end):
            if arr[i] > pivot:
                pivot_index += 1
                if i != pivot_index:
                    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
        arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
        return pivot_index, arr

print("-------连续子数组的最大和------")
s = Solution()
print(s.FindGreatestSumOfSubArray1([-2,1,-3,4,-1,2,1,-5,4]))


#面试题47：礼物的最大价值
"""
题型：二维矩阵的最优 
        题型一： f(i, j) = max(f(i, j-1), f(i-1, j))
        题型二： f(i, j) = f(i, j-1) + f(i-1, j)  如从左
"""
def get_gift_maxVal(array):
    if array:
        mn_max_val = np.zeros((array.shape[0], array.shape[1]))
        for i in range(array.shape[0]):
            mn_max_val[i][0] += array[i][0]
        for j in range(array.shape[1]):
            mn_max_val[0][j] += array[0][j]
            
        for m in range(1, array.shape[0]):
            for n in range(1, array.shape[1]):
                mn_max_val[m][n] = max(mn_max_val[m-1][n], mn_max_val[m][n-1]) + array[m][n]
        return mn_max_val[-1][-1]
    
    return 0


#面试题48：最长不含重复字符的子字符串
class Solution:
    def max_length(self, s):
        if len(s) == 0:
            return 0
        
        ans = []
        ans.append(1)
        used = [s[0]]
        
        len_s = len(s)
        for i in range(1, len_s):
            if s[i] not in used:
                ans.append(ans[i-1] + 1)
            
            if s[i] in used:
                d = self.get_d(used, s[i])
                if d <= ans[i-1]:
                    ans.append(d)
                else:
                    ans.append(ans[i-1] + 1)
        return ans[-1]
                
    
    def get_d(self, ss, si): #求出第i个位置的元素和它相等的那个的最近距离
        count = 1
        for i in range(len(ss)-1, -1, -1):
            if ss[i] != si:
                count += 1
            else:
                break
        return count

print("----------最长不含重复字符的子字符串------")
s = Solution()
print(s.max_length("arabcacfr"))


#动态规划练习题    更多动态规划题：https://wenku.baidu.com/view/1cd740559a6648d7c1c708a1284ac850ad020469.html
#排队买票问题
"""
判断第i个时候的可能情况，找出递推公式
题型：第i个有k种情况，从这k种情况中找出最优的作为f(i)

解题思路：
设f(i)表示排到第i个人排队买票所用的最短时间，
当排到第i个人的时候，该人有两种选择，一、自己买票，二、让第i-1个人帮他买票，比较这两种方法的用时间最少的那种为f(i)
所以排到第i个人的最短时间f(i) = min(f(i-1) + T(i), f(i-2) + R(i-1))
"""
class Solution:
    def min_time(self, n, T, R):
        min_time = [T[0], R[0]]
        for i in range(2, n):
            ti = min(min_time[i-1]+T[i], min_time[i-2]+R[i-1])
            min_time.append(ti)
        return min_time[-1]
print("---------动态规划练习题-------")
print("-----排队买票问题------")


s = Solution()
print(s.min_time(5, [1,1.2,1.5,2,2.3], [2,2.6,2.1,3]))


###***最长不下降子序列的长度
"""
题型：最长子序列问题
解法：记录以arr[i]结尾的最优解may_maxormin(这样涵盖了问题的所有情况)，然后再在may_maxormin求最优解就是题目要求的解
解题思路:
    用now_maxlen保存以arr[i]结尾的最长子串长度。运用动态规划，要找到以arr[i]结尾的最长子序列长度，
    就要找到在arr[i]之前且比arr[i]小或等的不降子序列，即找比自身小的且在arr[i]前面的数的最长子序列长度，
    然后+1就是arr[i]的最长子序列长度。例如[2,11,4,12,6,1],要找到以6结尾的最长子序列长度，先找出2和4的最长子序列长度，
    然后从中再找出最长的那个长度+1就是以6结尾的最长子序列长度。求以2、4结尾的最长子序列长度以同样的方法，不断递推。
"""

class Solution:
    def subseq_maxlen(self, arr):
        now_maxlen = [1]
        len_arr = len(arr)
        for i in range(1, len_arr):
            now_maxlen.append(1)
            for j in range(0, i):
                if (arr[i] >= arr[j]) & (now_maxlen[j]>=now_maxlen[i]):
                    now_maxlen[i] = now_maxlen[j] + 1
        
        return max(now_maxlen)
    """
    def subseq_longthext(self, arr):
        #1 记录以i位置结尾的最大子序列的长度
        may_max = [1]
        sorted_used = [arr[0]]
        
        arr_len = len(arr)
        for i in range(1, arr_len):
            
            print("sorted_used:", sorted_used)
            print("may_max:    ", may_max)
            print("-----------------------------")
            #找到arr[i]对应在sorted_used的最近的数的index
            idx = self.erfen_geti(sorted_used, arr[i])
            
            #如果sorted_used里有数大于或等于arr[i]
            if arr[i] > sorted_used[0]:
                #把arr[i] insert到sorted_used对应的index+1
                sorted_used.insert(idx+1, arr[i])
                
                #may_min在index+1的位置插入 may_min[index]+1
                may_max.insert(idx+1, may_max[idx]+1)
            else:
                sorted_used.insert(0, arr[i])
                may_max.insert(0, 1)
        
        #2 求出may_max的最大值，即题目的结果
        
        return sorted_used
            
    
    def erfen_geti(self, sorted_used, x):#用二分法实现某一数找到有序数组中与自己最接近的且小于或等于自身的数的index.
                                        #如果没有比自己小的，index = 0
        if len(sorted_used) == 1:
                return 0
        
        if x >= sorted_used[-1]:
            return len(sorted_used)-1
        
        L = 0
        R = len(sorted_used) - 1
        
        while L < R:
            idx = L + (R-L)//2
            if x >= sorted_used[idx]:
                L = idx + 1
            else:
                R = idx
                
        ###***有序数组中与自己最接近的且小于或等于自身的数的index
        if x >= sorted_used[idx]:
            return idx
        else:
            return idx-1
    """
    
print("--------最长不下降子序列的长度-------")
s = Solution()
#print(s.subseq_longthext([13,7,9,16,38,24,37,18,44,19,21,22,63,15]))
print(s.subseq_maxlen([2,11,4,12,6,1]))



#最长子序列拓展：拦截导弹
class IntercMissile:
    def interc_maxnum(self, arr):
        may_max = [1]
        arr_len = len(arr)
        for i in range(1, arr_len):
            may_max.append(1)
            for j in range(0, i):
                if (arr[i]<=arr[j]) & (may_max[j] >= may_max[i]):
                    may_max[i] = may_max[j] + 1
                    
        return max(may_max)
    
    
print("-----------拦截导弹----------")
s = IntercMissile()
print(s.interc_maxnum([389,207,155,300,299,170,158,65]))



#最长子序列拓展：合唱队队形
class Solution:
    def chorus_max_num(self, arr):
        max_len_left = [1]
        max_len_right = [1]
        
        len_arr = len(arr)
        for i in range(1, len_arr):
            max_len_left.append(1)
            for j in range(0, i):
                if (arr[i]>arr[j]) & (max_len_left[j] >= max_len_left[i]):
                    max_len_left[i] = max_len_left[j] + 1
        
        arr_ni = arr[::-1]
        for k in range(1, len_arr):
            max_len_right.append(1)
            for l in range(0, k):
                if (arr_ni[k]>arr_ni[l]) & (max_len_right[l] >= max_len_right[k]):
                    max_len_right[k] = max_len_right[l] + 1
                    
        max_len_right = max_len_right[::-1]
        
        may_ans = []
        for m in range(len_arr):
            may_ans.append(len_arr - (max_len_left[m] + max_len_right[m] - 1))
        
        return min(may_ans)
        
    
print("---最长子序列拓展：合唱队队形---")
s = Solution()
print(s.chorus_max_num([186,186,150,200,160,130,197,220]))



#*第四大部分：排列组合
print("========【第四大部分：排列组合】======")
#面试题38：字符串的排列  递归
"""
思路：
f(["a","b","c"], 0)#让["a","b","c"]的第"0"位之前不动，第"0"位分别与包括自身后边的字母一一交换，
                    #得到a b c; b a c; c b a
a b c
        f(["a","b","c"], 1) #让["a","b","c"]的第"1"位之前不动，第"1"位分别与包括自身后边的字母一一交换，
                            #得到a b c; a c b
        a b c
                f(["a","b","c"], 2) ==> ["a","b","c"] #递归出口，即不满足函数条件，跳出该条语句进入下一条语句
        
        a c b
                f(["a","c","b"], 2) ==> ["a","c","b"] #跳出该层，进入上一层逻辑
                
b a c
        f(["b","a","c"], 1)
        b a c
                f(["b","a","c"], 2) ==> ["b","a","c"]
                
        b c a
                f(["b","c","a"], 2) ==> ["b","c","a"]

c b a
        f(["c","b","a"], 1)
        c b a
                f(["c","b","a"], 2) ==> ["c","b","a"]
        
        c a b
                f(["c","a","b"], 2) ==> ["c","a","b"] #该层执行结束，为最后一层，跳出，程序执行完毕！

所以最终的结果为：[["a","b","c"], ["a","c","b"], ["b","a","c"], ["b","c","a"], ["c","b","a"], ["c","a","b"]]

注意*：要考虑字母重复的情况
                        
"""

class Solution:
    def __init__(self):
        self.result = []
        
    def Permutation(self, ss, n):#n表示第"n"位之前不动，第"n"位分别与包括自身后边的字母一一交换
        # write code here
        len_ss = len(ss)
        if n == len_ss-1: #递归出口
            self.result.append(ss)
            
        for i in range(n, len_ss):
            self.swap(ss, n, i)
            self.Permutation(ss, n+1)
            
        return self.result
            
    def swap(self, ss, i, j):
        ss[i], ss[j] = ss[j], ss[i]

print("-------【38】字符串的排列------")
s = Solution()
print(s.Permutation(["a", "b", "c"], 0))

        

    
#面试题45：把数组排成最小的数
#面试题45：把数组排成最小的数
class Solution_findmin_arr:
    def __init__(self):
        self.res = []
        
    def perm(self, rest_ss, forest_ss):
        
        if len(rest_ss) == 0:
            self.res.append(forest_ss)
        else:
            for i in range(len(rest_ss)):
                self.perm(rest_ss[:i]+rest_ss[i+1:], forest_ss+rest_ss[i])
                
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        #1 把数字转换成字符串
        str_numbers = [str(num) for num in numbers]
        if len(str_numbers) == 0:
            return ""
        
        #2 定义两个字符串的大小函数
        #3 用快排得出排好序的数组
        sort_str = self.quick_sort(str_numbers, 0, len(numbers))
        ans = ""
        for s in sort_str:
            ans += s
        return int(ans)
    
    def compare(self, str1, str2):#判断str1是否小于或等于str2
        """
        flag = 0
        min_len = min(len(str1), len(str2))
        for i in range(min_len):
            if str1[i] < str2[i]:
                return 1
            if str1[i] > str2[i]:
                return 0
        
        if len(str1) > len(str2):
            if str1[min_len] < str2[-1]:
                return 1
            else:
                return 0
        elif len(str1) < len(str2):
            if str1[-1] <= str2[min_len]:
                return 1
            else:
                return 0
        """
        if int(str1+str2) > int(str2+str1):
            return 0
        elif int(str1+str2) <= int(str2+str1):
            return 1
            
    def quick_sort(self, arr, start, end):
        if start < end:
            pivot_index = self.partition(arr, start, end)
            self.quick_sort(arr, start, pivot_index)
            self.quick_sort(arr, pivot_index+1, end)
        return arr
    
    def partition(self, arr, start, end):
        pivot_index = start
        pivot = arr[pivot_index]
        
        for i in range(start+1, end):
            if self.compare(arr[i], pivot):
                pivot_index += 1
                if i != pivot_index:
                    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
        arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
        
        return pivot_index
    
    
        
print("--------把数组排成最小的数------")
s = Solution()
print(s.compare("7", "3"))
print(s.PrintMinNumber([3,32,321]))
        


#第五大部分：其他
print("=======【第五大部分：其他】====")
#面试题3：数组中重复的数字
class Solution:
    def duplicate1(self, numbers):
        duplication = []
        #1排序
        ###***冒泡法排序的python实现(升序)
        for i in range(len(numbers)-1):
            for j in range(len(numbers)-1-i):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    
        #2找出排序后重复的数
        for i in range(len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                duplication.append(numbers[i])
        duplication = list(set(duplication))
            
        return duplication
    
    def duplicate2(self, numbers, duplication):
        #1 用哈希表将信息存起来， k-->数值； v-->该数值出现的次数
        d = {}
        len_nums = len(numbers)
        
        for i in range(len_nums):
            if numbers[i] in d:
                d[numbers[i]] += 1
            else:
                d[numbers[i]] = 1
        
        #2 找出其中的一个v=1对应的k
        for k, v in d.items():
            if v > 1:
                duplication.append(k) ###***duplication是一个数组
                return True
            
        return False
        
print("---------数组中重复的数字--------")
s = Solution()
print(s.duplicate2([2,1,3,1,4], []))


#题目二：不修改数组找出重复的数字

    
#面试题4：二维数组中的查找
def Find(target, array):
    for i in range(array.shape[1]-1):
        if target < array[0][-1]:
            array = np.array(list(map(lambda x:x[:-1], array)))  ###***删除二(n)维数组中的某一列
    for j in range(array.shape[0]-1):   
        if target > array[0][-1]:
            array = array[1:]
    if target == array[0][-1]:
        return 1
    else:
        return 0
    
#面试题5：替换空格
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        #1 将字符串按空格切分
        s_list = s.split(" ")
        
        #2 拼接
        new_s = ""
        for a in s_list:
            
            new_s += a
            new_s += "%20"
        new_s = new_s[:-3]
        
        return new_s
    
    
#*面试题12：矩阵中的路径
#def hasPath(matrix, rows, cols, path):
        

print("---------【5】替换空格---------")
s = Solution()
print(s.replaceSpace("We are happy."))
    

#面试题15：二进制中1的个数     n逐步右移一位； n&1得到末位是不是为一
def NumberOf1(n):
    count = 0
    while n != 0:
        if n&1 :
            count += 1
        n = n >> 1
    return count

def NumberOf1_2(n):
    count = 0
    while n != 0:
        n = n & (n-1)
        count += 1
    return count 


#面试题16：数值的整数次方        规范性，完整性，异常捕获
class Solution:
    def Power(self, base, exponent):
        try:
            if exponent == 0:
                return 1
            elif exponent < 0:
                power = 1
                for i in range(-exponent):
                    power *= base
                power = 1/power
            else:
                power = 1
                for i in range(exponent):
                    power *= base
            return power
        except:
            print("base为0的时候exponent不能为负数！！！")

#*面试题17：打印从1到最大的n位数
def printMaxN(n):
    try:
        for i in range(pow(10, n)-1):
            print(i+1)
        
    except:
        print("Error!! 请检查输入的n是否为正整数")
    
    ###***python可以处理任意大的数，不会溢出


#*面试题20：表示数值的字符串
def isNumeric(s):
    return 0



#面试题21：调整数组顺序使奇数位于偶数前面
def reOrderArray(array):
    first, final = 0, -1
    if len(array) == 0:
        return array
    while len(array) + final - first > 1:
        if array[first]%2 == 1:
            first += 1
        if array[final]%2 == 0:
            final -= 1
        array[first], array[final] = array[final], array[first]
        if len(array) + final - first == 1:
            break
    return array


#面试题29：顺时针打印矩阵
"""
思路：
    顺时针打印一圈，用四个变量left、right、top、bottom表示打印该圈时圈的范围，打印完一圈后更新这四个变量。
    满足left <= right and top <= bottom条件时一直打印。
    注意：单行或单圈也满足left <= right and top <= bottom条件，要再判断在打印这一圈的时候是不是单行或单圈的情况，如果是，只打印一次
"""
class Solution_PrintMatrix:
    def print_matrix(self, matrix):
        
        res = []
        row = len(matrix)
        col= len(matrix[0])
        left = 0
        right = col - 1
        top = 0
        bottom = row - 1
        while left <= right and top <= bottom:
            #从左到右
            for i in range(left, right+1):
                res.append(matrix[top][i])
            #从上到下
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
            #从右到左
            if top != bottom:###***判断此时打印的这一圈是不是单行的情况
                for i in range(right-1, left-1, -1):
                    res.append(matrix[bottom][i])
            #从下到上
            if left != right:#判断此时打印的这一圈是不是单列的情况
                for i in range(bottom-1, top, -1):
                    res.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res
        
    
            
    
print("---------【29】顺时针打印矩阵----------")
sp = Solution_PrintMatrix()
a = np.array([[1,2,3,5,7],[4,5,6,8,9],[7,8,9,5,44],[10,11,12,5,1]])
print(sp.print_matrix(a))




#面试题39：数组中出现次数超过一半的数字
class Solution_Morehalfnum:
    ###***从排好序的数组中找到数量超过一半的元素
    def MoreThanHalfNum_Solution(self, numbers):
        numbers = self.quick_sort(numbers)
        moer_half_num = numbers[0]
        count = 1
        max_count = 0
        for i in range(1, len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                count += 1
            else:
                count = 1
            if count > max_count:
                max_count = count
                moer_half_num = numbers[i]
        if max_count > len(numbers)/2:
            return moer_half_num
        return 0
    
    def quick_sort(self, numbers):
        if len(numbers) == 0:
            return []
        data = numbers[0]
        return self.quick_sort([i for i in numbers[1:] if i <= data]) + [data] + self.quick_sort([j for j in numbers[1:] if j > data])

print("-------数组中出现次数超过一半的数字-------")
smhf = Solution_Morehalfnum()
print(smhf.MoreThanHalfNum_Solution([1,2,3,3,3]))


#*面试题41：数据流中的中位数
class Solution:
    def __init__(self):
        self.data = []
        
    def Insert(self, num):
        # write code here
        ###***把num插入到有序的data中，插入后，data还是有序(从小到大)
        if len(self.data) == 0:
            self.data.append(num)
        elif len(self.data) == 1:
            if self.data[0] < num:
                self.data.append(num)
            else:
                self.data.insert(0, num)
        elif num > self.data[-1]:
            self.data.insert(len(self.data), num)
        else:
            L = 0
            R = len(self.data) - 1
            
            while L<R:
                idx = L + (R-L)//2
                if self.data[idx] < num:
                    L = idx + 1
                else:
                    R = idx
                
            insert_id = idx
            if self.data[idx] < num:
                insert_id += 1
            
            self.data.insert(insert_id, num)
            
        
    
    def GetMedian(self):
        # write code here
        #找出有序数组中的中位数
        if len(self.data)%2 == 0:
            mid_id = len(self.data)//2
            mid = (self.data[mid_id] + self.data[mid_id-1]) / 2.0###*** /2.0
        else:
            mid_id = len(self.data)//2
            mid = self.data[mid_id]
        return mid


print("--------【41】数据流中的中位数------")
s = Solution()
s.Insert(5)
s.Insert(2)
s.Insert(3)
s.Insert(4)
s.Insert(1)
s.Insert(6)


print(s.data)
print(s.GetMedian())


#面试题44：数字序列中某一位的数字
def get_n_num(n):
    if n < 10:
        return n
    else:
        n = n - 10
        l = len(str(n))
        
        for i in range(1, l):
            n = n - (pow(10, i+1) - pow(10, i)) * (i + 1)
            if n < 0:
                n = n + (pow(10, i+1) - pow(10, i)) * (i + 1)
                break
    
    b = n // (i+1)
    c = n % (i+1)
    a = b + pow(10, i)
    return str(a)[c]


#面试题45：把数组排成最小的数
class Solution_findmin_arr:
    def __init__(self):
        self.res = []
        
    def perm(self, rest_ss, forest_ss):
        
        if len(rest_ss) == 0:
            self.res.append(forest_ss)
        else:
            for i in range(len(rest_ss)):
                self.perm(rest_ss[:i]+rest_ss[i+1:], forest_ss+rest_ss[i])


#面试题46：把数字翻译成字符串
def get_transf_count(number):
    number = str(number)
    if len(number) == 0:
        return 0
    elif len(number) == 1:
        return 1
    elif len(number) == 2:
        if int(number) > 25:
            return 1
        else:
            return 2
    else:
        counts = []
        counts.append(1)
        
        if int(number[-2:]) > 25:
            counts.append(1)
        else:
            counts.append(2)
        
        for i in range(2, len(number)):
            if int(number[-(i+1):-(i-1)]) > 25:
                g = 0
            else:
                g = 1
            counts.append(counts[i-1] + counts[i-2] * g)
        
        return counts[-1]

    
#面试题49：丑数
class Solution_Cs1:
    def GetUglyNumber_Solution(self, k):
        index = 0
        cs_count = 0
        cs_list = []
        while True:
            if self.is_cs(index):
                cs_list.append(index)
                cs_count += 1
            index += 1
            if cs_count == k:
                break
        return cs_list[-1]
        
    def is_cs(self, index):#如果是丑数，返回1，否则返回0    这个判断3个while很耗时间的
        if index == 0:
            return 0
        if (index == 1)|(index == 2)|(index == 3)|(index == 4)|(index == 5):
            return 1
        while index % 2 == 0:
            index /= 2
        while index % 3 == 0:
            index /= 3
        while index % 5 == 0:
            index /= 5
        if index == 1:
            return 1
        else:
            return 0

class Solution_Cs2:
    def __init__(self):
        self.cs_list = [1,2,3,4,5]
    def GetUglyNumber_Solution(self, k):
        if k <= 0:
            return 0
        elif k >=1 and k <= 5:
            return self.cs_list[k-1]
        else:
            while len(self.cs_list) != k:
                for cs2 in self.cs_list[1:]:
                    if 2 * cs2 > self.cs_list[-1]:
                        max_2 = 2 * cs2
                        break
                for cs3 in self.cs_list[1:]:
                    if 3 * cs3 > self.cs_list[-1]:
                        max_3 = 3 * cs3
                        break
                for cs5 in self.cs_list[1:]:
                    if 5 * cs5 > self.cs_list[-1]:
                        max_5 = 5 * cs5
                        break
                self.cs_list.append(min(max_2, max_3, max_5))
                
            return self.cs_list[k-1]
    
print("-------------丑数-------------")
import time
scs1 = Solution_Cs1()
t1 = time.time()
print(scs1.GetUglyNumber_Solution(320))
t2 = time.time()
print("the time of Solution1:", t2-t1)

scs2 = Solution_Cs2()
t1 = time.time()
print(scs2.GetUglyNumber_Solution(320))
t2 = time.time()
print("the time of Solution2:", t2-t1)
    
    
def is_cs(index):#如果是丑数，返回1，否则返回0
    if index == 1:
        return 1
    while True:
        count = 0
        if index % 2 == 0:
            index = index / 2
            count += 1
        if index % 3 == 0:
            index = index / 3
        if index % 5 == 0:
            index = index / 5
        if index == 1:
            return 1
        if count < 3:
            return 0  

#面试题50：第一次只出现一次的字符
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return s
        
        ###***字典的用法
        d = {}
        for i in s:
            if i in d:
                d[i] += 1###***如果i是字典d的key，则往相应key的加1
            else:
                d[i] = 1#如果i不是字典里的key,把i放入字典中,令对应的val为1，字典中的每个key都是唯一的，字符按出现的先后顺序
        
        #找出只出现一次的字符
        v_count = 0
        for k, v in d.items():###***items()函数，返回字典迭代的key，val对
            if v == 1:
                v_count += 1
                break
        
        if v_count == 1:
            idx = -1
            for si in s:
                if si == k:
                    break
                idx += 1
            return idx
        else:
            return -1

print("-----第一次只出现一次的字符-------")
s = Solution()
print(s.FirstNotRepeatingChar("google"))
    
#面试题51：数组中的逆序对
"""
思路：
    用一个全局变量，在归并的过程记录逆序对的分数。如《剑指offer》P251示意图
    用递归思想实现代码。递归代码实现详情请看【面试题34】中"递归代码编写总结"
"""
class Solution:
    def __init__(self):
        self.nx_num = 0
    
    #递归，逐层归并最后获得逆序对的总个数 self.nx_num
    def InversePairs(self,arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.InversePairs(arr[:mid])
        right = self.InversePairs(arr[mid:])
        
        return self.merge_nxnum(left, right)
    
    #对有序的数组a1, a2 merge,仍然得到有序的数组。并在归并的过程记录逆序对的个数
    def merge_nxnum(self, arr1, arr2):
        #计算这两个数组的逆序对个数
        len1 = len(arr1)
        len2 = len(arr2)
        id1 = -1
        id2 = -1
        while True:
            if arr1[id1] >= arr2[id2]:
                self.nx_num = self.nx_num + (id2 + 1 + len2)
                if id1 != -len1:
                    id1 += -1
                else:
                    break
                
            else:
                #如果arr[id1] < arr[id2]并且id2！=-len2时
                if id2 != -len2:
                    id2 += -1
                else: #如果arr[id1] < arr[id2] 并且id2==-len2时，就终止循环
                    break
            
        #生成新的有序数组
        id1 = 0
        id2 = 0
        arr_new = []
        while id1 < len1 and id2 < len2:
            if arr1[id1] < arr2[id2]:
                arr_new.append(arr1[id1])
                id1 += 1
            elif arr1[id1] > arr2[id2]:
                arr_new.append(arr2[id2])
                id2 += 1
            else:
                arr_new.append(arr1[id1])
                arr_new.append(arr2[id2])
                id1 += 1
                id2 += 1
        
        if id1 < len1:
            for i in range(id1, len1):
                arr_new.append(arr1[i])
        if id2 < len2:
            for j in range(id2, len2):
                arr_new.append(arr2[j])
        
        return arr_new
    
    
    
    def InversePairs2(self, data):
        rev_ali = []
        for i in range(len(data)):
            for j in range(i, len(data)):
                if data[i] > data[j]:
                    rev_ali.append([data[i], data[j]])
            
        return len(rev_ali)
        
    def sort_data(self, data):
        if len(data) == 0:
            return []
        compare = data[0]
        return self.sort_data([i for i in data[1:] if i > compare]) + [compare] + self.sort_data([j for j in data[1:] if j <= compare])


print("------------【51】数组中的逆序对---------")
s = Solution()
#print(s.merge_sort([7,5,6,4]))

s.InversePairs([7,3,8,4,5,2,1])
#print(s.merge_nxnum([5,7], [4,6]))
print(s.nx_num)


#面试题52：两个链表的第一个公共节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_ComNode:
    def FindFirstCommonNode(self, pHead1, pHead2):
        #1 遍历两个链表的长度，求出长度差m
        count1 = 0
        count2 = 0
        while pHead1:
            count1 += 1
            pHead1 = pHead1.next
        while pHead2:
            count2 += 1
            pHead2 = pHead2.next
        diff = abs(count1 - count2)
        #2 长的先走m步，然后两个指针以同样的速度前进，当第一次两个节点一致时就是第一个公共节点
        if count1 > count2:
            for i in range(diff):
                pHead1 = pHead1.next
            for j in range(count1-diff):
                if pHead1 == pHead2:
                    return pHead1.val
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        else:
            for k in range(diff):
                pHead2 = pHead2.next
            for l in range(count1-diff):
                if pHead1 == pHead2:
                    return pHead2.val
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        
    def FindFirstCommonNode(self, pHead1, pHead2):
        #1 用两个栈把两个链表的节点装起来
        stack1 = []
        stack2 = []
        pop_list1 = []
        pop_list2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        if stack1 == [] or stack2 == []:
            return {}
        if len(stack1) == len(stack2):
            return stack1[0]
        if len(stack1) == 1 or len(stack2) == 1:
            return stack1[0]
        
        #2 两个栈同时依次弹栈，当弹出的节点不同时，上一个弹出的节点就是第一个公共节点
        s1 = stack1
        s2 = stack2
        if s1.pop() != s2.pop():
            return {}
        while stack1 or stack2:
            pop_list1.append(stack1.pop())
            pop_list2.append(stack2.pop())
            if pop_list1[-1] != pop_list2[-1]:
                return pop_list1[-2]

#面试题53：一、在排序数组中查找数字
import math
class Solution_Getnum:
    def GetNumberOfK1(self, data, k):
        if k not in data:
            return -1
        
        count = 0
        for i in data:
            if i == k:
                count += 1
        return count
    
    ###***二分查找的代码框架
    def GetNumberOfK2(self, data, k):
        ###***特别注意各种可能的边界情况
        if k not in data:
            return -1
        
        if len(data) == 1:
            return 1
        
        L = 0
        R = len(data) - 1
        while L < R:
            mid =int(math.floor((R + L)/2))
            if data[mid] > k: #guess()
                R = mid
            elif data[mid] < k:
                L = mid + 1###***左边要加1，防止陷入死循环
            else:
                target_index_left = mid
                target_index_right = mid
                break
        
        count_left = 0
        while data[target_index_left] == k: 
            if target_index_left == 0:###***防止list越界
                if data[target_index_left] == k:
                    count_left += 1
                break
            count_left += 1
            target_index_left -= 1
        
        count_right = -1
        while data[target_index_right] == k:
            if target_index_right == (len(data) - 1):
                if data[target_index_right] == k:
                    count_right += 1
                break
            count_right += 1
            target_index_right += 1
        
        return count_left + count_right
            

print("----------在排序数组中查找数字-----------")
sg = Solution_Getnum()
print(sg.GetNumberOfK1([1,2,3,3,3,3,3,3,4,4,4,6,7,9], 3))
print(sg.GetNumberOfK2([1,2,4,4,4,6,7,9], 4))


#二、0~n-1中缺失的数字
print("--------0~n-1中缺失的数字-------")
###***二分查找的代码框架
def find_loss(sort_array):
    L = 0
    R = len(sort_array) - 1
    while L < R:
        mid = int(math.floor((R+L)/2))
        if mid != sort_array[mid]: #guess()
            R = mid 
        else:
            L = mid + 1 ###***左边要加一个大于0的值，防止陷入死循环。如果是index一般是加1，如果是求如开方的连续值，根据精确要求取0~1的值
    #return mid
    if sort_array[mid] + 2 == sort_array[mid+1]:
        return sort_array[mid] + 1
    else:
        return sort_array[mid] - 1

print(find_loss([10,9,8,7,5,4,3,2,1,0]))
        

#三、数组中数值和下标相等的元素
def find_idxqval(sort_array):
    L = 0
    R = len(sort_array)
    while L < R:
        mid = int(math.floor((R+L)/2))
        if sort_array[mid] > mid:
            R = mid
        elif sort_array[mid] < mid:
            L = mid + 1
        else:
            return mid

#求一个数的开方值
def mysqrt(n, acc, sec_insur):
    L = 0
    R = n
    counter = 0
    while (L < R) and (counter < sec_insur): ###加counter双重保险，防止陷入死循环
        mid = (R + L)/2
        if mid * mid > n:
            R = mid
        else:
            L = mid + acc
        counter += 1
    return mid, counter


#面试题54：二叉搜索树的第k大节点
"""
二叉树的定义：
二叉搜索树，也称有序二叉树,排序二叉树，是指一棵空树或者具有下列性质的二叉树：
1. 若任意节点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
2. 若任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
3. 任意节点的左、右子树也分别为二叉查找树。
4. 没有键值相等的节点。
"""
treeNode = TreeNode(8)
t_ss = treeNode
treeNode.left = TreeNode(6)
treeNode.right = TreeNode(10)
treeNode.left.left = TreeNode(5)
treeNode.left.right = TreeNode(7)
treeNode.right.left = TreeNode(9)
treeNode.right.right = TreeNode(11)

class Solution_Searchtree_kth:
    def __init__(self):
        self.Nodes_list = []
        
    def tin(self, pHead):
        if pHead != None:
            self.tin(pHead.left)
            self.Nodes_list.append(pHead.val)
            self.tin(pHead.right)
        
    
    def find_kth(self, pHead, k):
        self.tin(pHead)
        if k <= 0 or k > len(self.Nodes_list):
            return None
        return self.Nodes_list[k-1]
    


print("-----二叉搜索树的第k大节点-----")
ssk = Solution_Searchtree_kth()
print(ssk.find_kth(t_ss, 1))
print(ssk.Nodes_list)


#面试题55：二叉树的深度
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        stack1 = [pRoot]
        stack2 = []
        layer_num = 0
        while stack1 or stack2:
            if stack1:
                layer_num += 1
            while stack1:
                s1 = stack1.pop()
                #print(s1.val)
                if s1.left:
                    stack2.append(s1.left)
                if s1.right:
                    stack2.append(s1.right)
            
            if stack2:
                layer_num += 1
            while stack2:
                s2 = stack2.pop()
                #print(s2.val)
                if s2.right:
                    stack1.append(s2.right)
                if s2.left:
                    stack1.append(s2.left)
            
        return layer_num
                
print("------二叉树的深度------")
s = Solution()
print(s.TreeDepth(t_ss))

#平衡二叉树
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return 1
        
        p_left = pRoot.left
        p_right = pRoot.right
        left_deepth = self.TreeDepth(p_left)
        right_deepth = self.TreeDepth(p_right)
        
        if abs(left_deepth - right_deepth) <=1:
            return 1
        else:
            return 0
    
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        stack1 = [pRoot]
        stack2 = []
        layer_num = 0
        while stack1 or stack2:
            if stack1:
                layer_num += 1
            while stack1:
                s1 = stack1.pop()
                #print(s1.val)
                if s1.left:
                    stack2.append(s1.left)
                if s1.right:
                    stack2.append(s1.right)
            
            if stack2:
                layer_num += 1
            while stack2:
                s2 = stack2.pop()
                #print(s2.val)
                if s2.right:
                    stack1.append(s2.right)
                if s2.left:
                    stack1.append(s2.left)
            
        return layer_num

print("------平衡二叉树-------")
s = Solution()
print(s.IsBalanced_Solution(t_ss))


#面试题56：数组中数字出现的次数
"""
逻辑运算：
    与(&)、或(|)、非(^)、异或 (通过逻辑运算之间满足交换律，如2^7^2=2^2^7)
        与(&)：1&1 = 1  1&0 = 0  2&1 ==>10&01 = 00==>0
            &和and(python没有&&)的区别
        或(|): 1|1 = 1  1|0 = 1  2|1 ==>10|01 = 11==>3
        非(~): 位值取反，置0为1，或置1为0  ~1 = 0   ~8 ==> ~1000 = 0111==>7
        异或(^): 1^1 = 0  1^0 = 1  0^1 = 1 0^0 = 0  2^8 ==> 0010^1000 = 1010==>10
            一个数与自身的异或为0
位运算：>>   << 
    9 >> 1 ==> 1001>>1 = 100==>4  ==> 9//2
    9 << 1 ==> 1001<<1 = 10010==>18 ==> 9*2
    
python中十进制转换为二、八、十六进制
    bin(8) = "0b1000"
    bin(-8) = "-0b1000"

原码、补码、反码
    9的原码：00001001； 9的反码：00001001(正数的反码码和原码一致)； 9的补码：00001001(正数的补码和原码一致) 
   -9的原码：10001001；-9的反码：11110110(负数的反码等于原码除符号位以外所有的位取反)； -9的补码：11110111(负数的补码等于其反码最低位加1)
"""
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        #1 将数组分成各涵一个只出现一次的两个数组
        xor = array[0]
        length_arr = len(array)
        for i in range(1, length_arr):
            xor = xor ^ array[i]
        
        is1_position = self.bin_nis1(xor)
        
        arr1 = []
        arr2 = []
        for a in array:
            if bin(a)[-is1_position] == "1":
                arr1.append(a)
            else:
                arr2.append(a)
        #2 分别对两个数组异或求不同的两个数字
        ans = []
        ans.append(self.xor(arr1))
        ans.append(self.xor(arr2))
        return ans
    
    def bin_nis1(self, xor):#判断一个十进制数从左起第一个为1的位置
        bin_xor = bin(xor)
        dao_xor = bin_xor[::-1]
        count = 0
        for a in dao_xor:
            count += 1
            if a == "1":
                break 
        return count
    
    def xor(self, array):#一组数组异或的结果
        x = array[0]
        length_arr = len(array)
        for i in range(1, length_arr):
            x = x ^ array[i]
        return x

print("------数组中数字出现的次数---------")
s = Solution()
print(s.FindNumsAppearOnce([2,2,6,4,4,7,3,7]))

#数组中唯一只出现一次的数字(p278)
class Solution:
    def find_once_num(self, array):
        add_bin = self.add_bin_array(array)
        ans = ""
        for i in range(8):
            ans += str(int(add_bin[i]) % 3)
        if ans[0] == "0":
            return int(ans, 2)  ###***二进制转十进制
        else:
            return -int(ans[1:], 2)

    def my_bin(self, x): #8位
        
        if x >= 0:
            n_x = bin(x)[2:]
            if len(n_x) < 8:
                supp_len = 8 - len(n_x)
            s = ""
            for i in range(supp_len):
                s += "0"
            n_x_final = s + n_x
        if x < 0:
            n_x = bin(x)[3:]
            if len(n_x) < 8:
                supp_len = 8 - len(n_x)
            s = "1"
            for i in range(1, supp_len):
                s += "0"
            n_x_final = s + n_x
            
        return n_x_final
    
    def add_bin_array(self, array):
        bin_array = []
        for a in array:
            bin_array.append(self.my_bin(a))
        add_bin = ""
        for i in range(8):
            i_res = 0
            for ba in bin_array:
                i_res += int(ba[i])
            add_bin += str(i_res)
        return add_bin
print("---数组中唯一只出现一次的数字(p278)----")
s = Solution()
print(s.find_once_num([2,-3,2,-3,78,2,-3]))
        

#面试题57：和为s的数字
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) <= 1:
            return None
        L = 0
        R = len(array) - 1
        while L < R:
            if array[L] + array[R] == tsum:
                return array[L], array[R]
            elif array[L] + array[R] > tsum:
                R -= 1
            else:
                L += 1
        return None

print("--------和为s的数字---------")
s = Solution()
print(s.FindNumbersWithSum([1,2,4,7,11,16],10))

#和为s的连续正数序列
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum == 1:
            return []
        find_n = tsum // 2 + 1
        first = 0
        final = find_n
        ans_index = []
        for i in range(first, final):
            sum_ser = 0
            for j in range(i, final):
                val = j + 1
                sum_ser += val 
                if sum_ser == tsum:
                    ans_index.append(self.print_i_j(i, j))
                    break
                if sum_ser > tsum:
                    break
        return ans_index[::1]
    
    def print_i_j(self, i, j):
        res = []
        for k in range(i, j+1):
            res.append(k+1)
        return res

print("-----和为s的连续正数序列-----")
s = Solution()
print(s.FindContinuousSequence(3))
            

#面试题58：翻转字符串 
#一、翻转单词顺序
class Solution:
    def ReverseSentence(self, s):
        # write code here
        words = s.split(" ")
        ss = ""
        while words:
            ss += words.pop() + " "
        ss = ss[:-1]
        return ss

print("-----翻转单词顺序------")
s = Solution()
print(s.ReverseSentence("I am a, student."))
            


#二、左旋转字符串
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if n < 0:
            return ""
        
        if len(s) == 0:
            return ""
        
        len_s = len(s)
        rem = n % len_s
        add_s = s[:rem]
        res = s + add_s
        
        return res[rem:]
    
print("--------左旋转字符串-------")
s = Solution()
print(s.LeftRotateString("abcdefg", 3457))


###***面试题59：队列的最大值   这个解法的信息量很大啊！！！！
class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.min_queue = []
    
    def push(self, x):
        if len(self.min_queue) == 0 or x > self.min_queue[-1]:
            self.min_queue.append(x)
        self.queue1.append(x)
    
    def pop(self):
        if self.queue1 or self.queue2:
            if self.queue2:
                self.queue2.pop()
            else:
                while self.queue1:
                    self.queue2.append(self.queue1.pop())
                self.queue2.pop()
        else:
            return []
    def min_qu(self):
        if len(self.min_queue) == 0:
            return []
        return self.min_queue[-1]
    
    def maxInWindows(self, num, size):
        # write code here
        if size == 0:
            return []
        
        len_num = len(num)
        res = []
        
        for i in range(len_num-size+1):
            for a in num[i:i+size]:
                self.push(a)
            res.append(self.min_qu())
            self.min_queue = []
        return res

print("----队列的最大值------")
s = Solution()
print(s.maxInWindows([2,3,4,2,6,2,5,1], 3))
    


#*面试题60：n个骰子的点数
class Solution:
    def s_pro_totalnum(self, n, s):
        if n > s:
            return 0
        if n == s:
            return 1
        
        ans = np.zeros((13, n))
        #把容易得到的结果求出，为动态规划后边求解做准备
        for i in range(13):
            for j in range(n):
                s_val = i+s-12
                n_val = j+1
            
                if s_val == n_val:
                    ans[i][j] = 1
                if n_val == 1 and n_val < s_val:
                    ans[i][j] = 1
                if n_val > s_val:
                    ans[i][j] = 0
                if 6*n_val < s_val:
                    ans[i][j] = 0
        for n_idx in range(1, n):
            
            for s_idx in range(n_idx+1-s+13, 13):
                
                ans[s_idx][n_idx] = ans[s_idx-1][n_idx-1] + ans[s_idx-2][n_idx-1] + ans[s_idx-3][n_idx-1] + ans[s_idx-4][n_idx-1] + ans[s_idx-5][n_idx-1] + ans[s_idx-6][n_idx-1]
        
        return ans[-1][-1]

print("-------n个骰子的点数---------")
s = Solution()
print(s.s_pro_totalnum(3, 9))
            

#面试题61：扑克牌中的顺子
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        #1 把数组中的0抽出来
        num0_list = []
        for i in range(len(numbers)):
            if numbers[i] == 0:
                num0_list.append(numbers.pop(i))
        
        #2 对数组排序
        sort_numbers = self.quick_sort(numbers, 0, len(numbers))
        
        #3 判断是否连续
        len_sort_numbers = len(sort_numbers)
        flag = 1  ###***巧用flag
        for i in range(len_sort_numbers-1):
            if sort_numbers[i]+1 != sort_numbers[i+1]:
                flag = 0
                break
        if flag:
            return 1
        #如果连续，返回1
        #如果不是连续，判断抽出list里是否有0
            #如果有0。如果有0，判断len_num0_list 是否大于need_0_num，如果大于返回1，没有返回0; 如果没0，返回0
        
        else:
            if num0_list:
                len_num0_list = len(num0_list)
                need_0_num = 0
                for j in range(len_sort_numbers-1):
                    if sort_numbers[j] != sort_numbers[j+1]:
                        need_0_num += sort_numbers[j+1] - sort_numbers[j] - 1
                if len_num0_list >= need_0_num:
                    return 1
                else:
                    return 0
                
            else:
                return 0
        
    def quick_sort(self, arr, start, end):
        if start < end:
            pivot_index = self.partition(arr, start, end)
            self.quick_sort(arr, start, pivot_index)
            self.quick_sort(arr, pivot_index+1, end)
            
        return arr
        
    def partition(self, arr, start, end):
        pivot = arr[start]
        pivot_index = start
        for i in range(start+1, end): ###***start+1
            if arr[i] <= pivot:
                pivot_index += 1
                if i != pivot_index:
                    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
        arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
        
        return pivot_index
    
    
print("------扑克牌中的顺子--------")
s = Solution()
print(s.IsContinuous([9,8,7,6,10]))
                    

#*面试题62:圆圈中的最后剩下的数字
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return None
        if n == 1:
            return ListNode(0)
        
        
        ###***1 创建一个环形链表
        p1 = ListNode(0) ###***要这样赋值保留头节点
        p = p1
        for i in range(1, n):
            pnext = ListNode(i)
            p.next = pnext
            p = pnext
        p.next = p1
        
        #2 从0节点开始，每次删除第m个节点，下一次以删除这个节点的下一个节点开始再删除第m个节点，直到剩下一个节点
        p_need = p1
        while p_need.next:
            p_need = self.del_mNode(p_need, m)
        
        return p_need
    
    def del_mNode(self, pNode, m): #删除链表中从pNode开始的第m个节点，返回删除后的下一个节点
        if pNode.next.next == pNode:#如果是个只剩下两个节点的环形链表
            if m%2 == 0:
                pNode.next.next = None
                pNode.next = None
                return pNode
            else:
                p_need = pNode.next
                p_need.next.next = None
                p_need.next = None
                return p_need
        #正常情况，单项链表和环形链表都适用
        p = pNode
        for i in range(m-2):
            p = p.next
        p.next = p.next.next
        
        return p.next
        
print("-------【62】圆圈中的最后剩下的数字---------")
s = Solution()
t1 = s.LastRemaining_Solution(5, 3)

print(t1.val)
    
            
#面试题63：股票的最大利润
class Solution:
    def stocks_max_pro(self, price):
        #1 记录历史记录中每个时间点的最小价格的股票
        history_min_buy = [price[0]]
        min_buy = price[0]
        for i in range(1, len(price)):
            if price[i] < min_buy:
                min_buy = price[i]
                history_min_buy.append(min_buy)
            else:
                history_min_buy.append(min_buy)
        
        
        #2 用当天价格减去历史最小价格，得到每个时间点卖出的话最大收益
        history_max_pro = []
        for i in range(len(price)-1):
            history_max_pro.append(price[i+1] - history_min_buy[i])
        
        #3 找出历史最大收益   用时间复杂度为O(n)的解法求第一大的值
        max_pro = self.find_kth(history_max_pro, 0, len(history_max_pro), 1)
        
        return max_pro
    
    
    def partition(self, arr, start, end):
        #if start < end:
        pivot_index = start
        pivot = arr[pivot_index]
        for i in range(start+1, end):
            if arr[i] > pivot:
                pivot_index += 1
                if i != pivot_index:
                    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
        arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
        return pivot_index, arr
        #elif start == end:
        #    return start
        #else:
        #    return 
    
    def find_kth(self, arr, start, end, k):
        if k <= 0 or k > len(arr):
            return None
        
        while start < end:
            pivot_index, arr = self.partition(arr, start, end)
            if pivot_index == k-1:
                return arr[pivot_index]
            if pivot_index > k-1:
                end = pivot_index
            else:
                start = pivot_index + 1###***
    

print("------股票的最大利润------")
s = Solution()
print(s.stocks_max_pro([9,11,8,5,7,12,16,14]))


#面试题64：求1+2+......+n
class Solution:
    def Sum_Solution(self, n):
        if n == 1:
            return 1
        return n + self.Sum_Solution(n-1)

print("-------求1+2+......+n-------")
s = Solution()
print(s.Sum_Solution(2))


"""
###***在线编程题的输入格式
import sys
line1 = sys.stdin.readline().split()
line1 = [int(l) for l in line1]
N,P,H,W = line1[0], line1[1], line1[2], line1[3]


输入多行
import sys
m = sys.stdin.readline().split()
m = int(m[0])
data = []
for i in range(m):
    data.append(sys.stdin.readline().split())
"""

#面试题66:构建乘积数组    提高效率-->通过减少重复的计算-->用动态规划法
class Solution:
    def multiply(self, A):
        len_A = len(A)
        if len_A == 0:
            return None
        if len_A == 1:
            return 1
        
        B = []
        C = []
        C.append(1)
        D = []
        D.append(1)
        
        #1 动态规划求出C,D
        for i in range(1, len_A):
            C.append(C[i-1] * A[i-1])
        for j in range(1, len_A):
            D.append(D[j-1] * A[j+(len_A-2*j)])
        
        #2 求出构建后的乘积数组
        D = D[::-1]
        for k in range(len_A):
            B.append(C[k] * D[k])
        return B
    
    def multiply2(self, A):
        # write code here
        len_A = len(A)
        B = []
        for i in range(len_A):
            
            product = 1
            for j in range(len_A):
                if i != j:
                    product *= A[j]
            B.append(product)
        
        return B
    
    
        

print("------【66】构建乘积数组----")
s = Solution()
print(s.multiply([0,1,5,2,6,2,3,2,5,5,21,2,2,2]))






#牛客网题：
"""
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数
字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
思路：通过ascii表解决问题
    1 判断s是否符合要求
    2 如果符合要求，将字符串转化为整数；如果不符合要求，返回0
知识点：
    查ascii码表，"0"-->48,"1"-->49...."9"-->57; "A"-->65, "B"-->66,..."Z"-->90, "a"-->ord("A")+32=97, "b"-->98...
    字符转十进制转换函数：ord("a") = 97
"""
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == "":
            return 0
        
        #1 判断s是否符合要求
        flag = self.is_need(s)
        if flag == 0:
            return 0
        #2 如果符合要求，将字符串转化为整数
        else:
            len_s = len(s)
            if s[0] == "+":
                ans = 0
                for i in range(1, len_s):
                    ans += (ord(s[i]) - 48) * pow(10, len_s-i-1)
            elif s[0] == "-":
                ans = 0
                for i in range(1, len_s):
                    ans += (ord(s[i]) - 48) * pow(10, len_s-i-1)
                ans = 0 - ans
            else:
                ans = 0
                for i in range(len_s):
                    ans += (ord(s[i]) - 48) * pow(10, len_s-i-1)
                    
            return ans
            
        
    def is_need(self, s):
        len_s = len(s)
        flag = 1
        if (s[0] in ["+", "-"]) | ((s[0] >= "0") and (s[0] <= "9")):
            for i in range(1, len_s):
                if s[i] < "0" or s[i] > "9":
                    flag = 0
        else:
            flag = 0
            
        return flag
print("------------字符串转整数----------")
s = Solution()
print(s.StrToInt(""))     
        

"""
题目：我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
思路：考虑最后一块矩形的情况，有两种情况，横着放或竖着放(n>=2时)，设f(n)表示有n个时的方法个数。
    所以f(n) = 最后一个举行横着放的方法数 + 最后一个矩形竖着放的方法数， 即f(n) = f(n-2) + f(n-1)
"""
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        
        ans = [0, 1, 2]
        for i in range(3, number+1):
            ans.append(ans[i-1] + ans[i-2])
        return ans[-1]






