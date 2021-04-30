# 用户：李航
# 开发时间：2021/4/30 14:44
# 思路是：「输入栈」会把输入顺序颠倒；如果把「输入栈」的元素逐个弹出放到「输出栈」，再从「输出栈」弹出元素的时候，则可以负负得正，实现了先进先出。
class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2