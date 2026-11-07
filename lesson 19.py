def linear(items):
    steps = 0
    for item in items:
        steps += 1
    return  steps

items = [1, 2, 3, 4]
# print(linear(items))

def quadratic(items):
    steps = 0
    for first in items:
        for second in items:
            steps += 1
    return steps
#
# print(quadratic([1, 2, 3, 4]))

def constant(items):
    steps = 0
    for _ in range(3):
        steps += 1
    return steps
# print(constant(items)

items = [1, 2, 3, 4]

print("O(1):", constant(items))
print("O(n):", linear(items))
print("O(n²):", quadratic(items))

class Stack:
    def __init__(self):
        self._items = []
    def push(self, item):
        self._items.append(item)
    def is_empty(self):
        return len(self._items) == 0
    def pop(self):
        if self.is_empty():
            raise IndexError("empty stack")
        else:
            return self._items.pop()

# stack = Stack()
#
# try:
#     stack.pop()
# except IndexError:
#     print("Stack is empty")


def reverse_text(text):
    stack = Stack()
    for char in text:
        stack.push(char)
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    return result
def is_palindrome(s):
    clean_text = s.lower().replace(" ", "")
    return clean_text == reverse_text(clean_text)

print(reverse_text("Python"))
print(reverse_text("გამარჯობა"))
stack = Stack()
print(is_palindrome("ანა"))
print(is_palindrome("A b a"))
print(is_palindrome("Python"))
# stack.push("ა")
# stack.push("ბ")
# print(stack.pop())
# print(stack.pop())