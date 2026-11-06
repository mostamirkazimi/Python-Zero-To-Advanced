from collections import deque

tasks = deque()

tasks.append("Python")
tasks.append("Machine Learning")

print(tasks)

tasks.popleft()

print(tasks)