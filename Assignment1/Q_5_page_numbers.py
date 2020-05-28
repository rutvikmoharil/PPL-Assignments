total_pages = int(input("Enter total pages of the book"))

book = []
for i in range(1, total_pages + 1):
    book.append(i)

available = []
a = 1
print("Enter available pages in the book and press 0 after entering:\n")

while(a != 0):
    a = int(input())
    if a != 0:
        available.append(a)


for i in range(1, total_pages + 1):
    if i not in available:
        print(i)





