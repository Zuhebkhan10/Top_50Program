# Find the first of index occurrence.(Implementing substring serch)
def first_index(main,sub):
    n=len(main)
    m=len(sub)

    for i in range(n-m+1):
        if main[i:i+m]==sub:
            return i
    return -1
print(first_index("Hello duniya", 'duniya'))


# text = "hello world"
# pattern = "world"
#
# index = -1
#
# for i in range(len(text) - len(pattern) + 1):
#     if text[i:i+len(pattern)] == pattern:
#         index = i
#         break
#
# print(index)
