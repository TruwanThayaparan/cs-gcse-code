Book1 = ("Book One", "Author One", 2020, "Fiction")
Book2 = ("Book Two", "Author Two", 2021, "Non-Fiction")
Book3 = ("Book Three", "Author Three", 2019, "Mystery")
Book4 = ("Book Four", "Author Four", 2023, "Science Fiction")
Book5 = ("Book Five", "Author Five", 2022, "Biography")

print("-" * 30)

print(Book1)
print(len(Book1))

print(Book2)
print(len(Book2))

print(Book3)
print(len(Book3))

print(Book4)
print(len(Book4))

print(Book5)
print(len(Book5))

print("-" * 30)

(key1, value1_1, value1_2, value1_3) = Book1
(key2, value2_1, value2_2, value2_3) = Book2
(key3, value3_1, value3_2, value3_3) = Book3
(key4, value4_1, value4_2, value4_3) = Book4
(key5, value5_1, value5_2, value5_3) = Book5

print("Unpacked values for Book1:")
print(key1)
print(value1_1)
print(value1_2)
print(value1_3)

print("Unpacked values for Book2:")
print(key2)
print(value2_1)
print(value2_2)
print(value2_3)

print("Unpacked values for Book3:")
print(key3)
print(value3_1)
print(value3_2)
print(value3_3)

print("Unpacked values for Book4:")
print(key4)
print(value4_1)
print(value4_2)
print(value4_3)

print("Unpacked values for Book5:")
print(key5)
print(value5_1)
print(value5_2)
print(value5_3)

print("-" * 30)
