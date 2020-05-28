first_term = float(input("Enter the first term of Geometric Series\n"))
common_ratio = float(input("Enter the common ratio of Geometric Series\n"))

ten_terms = []

for i in range(0, 10):
    ten_terms.append(first_term * (common_ratio ** i))

print(ten_terms)
