# STACK
# A. In MOMO we are pushing 3 steps and undo the last one
# 1.It's initially empty
momo_stack=[]
print(f"initial empty stack: {momo_stack}")

# 2. push the steps onto stack
# the append() is method to add the item to the end of our stack
momo_stack.append("step 1")
print(f"Push 'step 1':  {momo_stack}")

momo_stack.append("step 2")
print(f"Push 'step 2': {momo_stack}")

momo_stack.append("step 3")
print(f"Push 'step 3': {momo_stack}")

# 3. undo last by popping last step off the stack
# The pop() method removes and return the last items
undone_step=momo_stack.pop(2)
print(f"\nUndoing last step ... Removed '{undone_step}'")

# display what is left 
print(f"Final stack: {momo_stack}")

# B. 1. Initialize an empty list to act as the stack for the notes.
ur_stack=[]
print(f"Initial stack: {ur_stack}")

# 2. Push the 3 notes onto the stack using append()
ur_stack.append("Note 1")
ur_stack.append("Note 2")
ur_stack.append("Note 3")

print(f"Stack after pushing: {ur_stack}")

# 3. Pop one note from top. this remove Note 3
popped_note= ur_stack.pop(2)
print(f"\nPopped '{popped_note}' from top")
print(f"Stack after popping: {ur_stack}")

# C. Reverse RWANDAICT with stack
def reverse_string_with_stack(s):
    """
    Reverses a string using a stack data structure.
    """
    # Create an empty list to act as a stack
    stack = []

    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)

    # Pop all characters from the stack and build the reversed string
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# The string to be reversed
original_string = "RWANDAICT"

# Call the function and print the result
reversed_string = reverse_string_with_stack(original_string)
print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")

# Queue
# A NYABUGOGO BUS PARK
from collections import deque

# 1. Initialize the queue with 12 buses
# We can represent the buses by their position in the initial queue
# (e.g., "Bus 1", "Bus 2", etc.)
bus_queue = deque([f"Bus {i}" for i in range(1, 13)])

print(f"Original queue: {list(bus_queue)}\n")

# 2. Simulate 6 buses departing (popping from the left side of the deque)
num_departures = 6
for i in range(num_departures):
    departed_bus = bus_queue.popleft()
    print(f"Departed: {departed_bus}")

print(f"\nRemaining queue: {list(bus_queue)}")

# 3. Identify the bus at the front
front_bus = bus_queue[0]

print(f"\nAfter 6 departures, the bus at the front is: {front_bus}")

# B RSSB
from collections import deque

# 1. Initialize the queue with 5 clients
# We'll use their entry order as their identifier.
rssb_queue = deque(["Client 1", "Client 2", "Client 3", "Client 4", "Client 5"])

print(f"The initial queue is: {list(rssb_queue)}")

# 2. To find the third person, you simply access the third element
# In Python, list/deque indices start from 0.
# So, the third element is at index 2.
third_client = rssb_queue[2]

print(f"The third person in the queue is: {third_client}")

# To demonstrate the FIFO principle, let's serve the first two clients
print("\nServing the first two clients...")
rssb_queue.popleft() # Client 1 is served
rssb_queue.popleft() # Client 2 is served

print(f"The queue now is: {list(rssb_queue)}")

# The original "Client 3" is now at the front of the queue
print(f"The new client at the front is: {rssb_queue[0]}")

