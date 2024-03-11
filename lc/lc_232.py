# Leetcode Problem #232: Implement Queue using Stacks

# Description: Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty). Implement the MyQueue class: void push(int x) Pushes element x to the back of the queue, int pop() Removes the element from the front of the queue and returns it, int peek() Returns the element at the front of the queue, boolean empty() Returns true if the queue is empty, false otherwise.

class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []
    def push(self, x: int) -> None:
        self.a.append(x)
    def pop(self) -> int:
        if not self.b:
            self.fillQueue()

        return self.b.pop()
    def peek(self) -> int:
        if not self.b:
            self.fillQueue

        return self.b[-1]
    def empty(self) -> bool:
        return not self.a and not self.b
    def fillQueue(self):
        while self.a:
            self.b.append(self.a.pop())

q = MyQueue()






