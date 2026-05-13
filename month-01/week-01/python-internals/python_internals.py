# # Reference counting is exact and predictable.
# # getrefcount always adds 1 (function argument).
# # Interned strings have a baseline count from the intern cache.
# # Every variable assignment adds exactly 1 more.
# # a = b = c = 'hello' → 3 variables + intern cache + getrefcount arg = 5

# # Reference counting is Python's primary memory management mechanism.
# # getrefcount gives you a window into it but the numbers aren't always
# # precise because of immortal objects, REPL history, intern caches,
# # and temporary function arguments. The concept is solid — the
# # measurement tool is imperfect.





# #because a and b point to the same list object in memory, changes to b will affect a.
# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)  # why did a change?



# print(id(a))  # memory address of a
# print(id(b))  # memory address of b, should be the same as a
# print(a is b)  # check if a and b reference the same object

# print([1, 2, 3] is a) 
# print([1,2,3] is b)
# print([1,2,3] is [1,2,3])




# # The id for both of these is the same.
# # The first line is added to a spot in memory
# # When the function print() is complete that space in memory is freed
# # Then the second line takes that spot in memory
# # Although they have the same spot in memory, they are used at different times
# # thus they dont "share" the same list object in memory at the same time.
# # making is return false
# print(id([1, 2, 3]))  # memory address of a new list object
# print(id([1, 2, 3]))  # memory address of another new list



# Before creating strings, memory usage reflects only tracemalloc's
# own tracking overhead — this is the observer effect: the measurement
# tool itself consumes memory.
#
# After creating 10,000 unique strings, memory increases significantly
# because each string is a distinct object in memory. Unique strings
# created at runtime (e.g. "hello" + str(i)) cannot be interned —
# Python only interns string literals that look like identifiers.
#
# Using a = "hello world" in a loop would NOT show this growth because
# reference counting frees each string immediately when a is reassigned.
# Holding references in a list forces all 10,000 to exist simultaneously.


import tracemalloc

tracemalloc.start()


memory = tracemalloc.get_traced_memory()
print(memory)

strings = []


for i in range (100000):
    strings.append("hello world" + str(i))  # create unique strings that cannot be interned


memory = tracemalloc.get_traced_memory()
print(memory)
