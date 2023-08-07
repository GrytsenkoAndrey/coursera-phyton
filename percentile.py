a = [1, 2, 0, 10, 50, 42, 38]
b = [1, 2, 0, 10, 50, 42, 38, 5]

# avg a
print(sum(a) / len(a))
print('\n')
# avg b
print(sum(b) / len(b))
print('\n')

# mediana a
sort_a = sorted(a)
len(sort_a)
sort_a[3]

#mediana b
sort_b = sorted(b)
len(sort_b)

sort_b[3]
sort_b[4]

(sort_b[3] + sort_b[4])/2


def mf(a, b):
    return a + b

print(mf(3, 7))