from collections import deque

stack = deque()

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

# Display stack
print("Stack:", list(stack))

# Pop element
print("Popped:", stack.pop())

# Peek at top element
print("Top element:", stack[-1] if stack else "Stack is empty")
