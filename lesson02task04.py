# Задание 4
# Даны три числа a, b, c.
# Определите, существует ли треугольник с такими сторонами.
# Если треугольник существует, выведите строку YES, иначе выведите строку NO.
#
a,b,c = 123,267,214
valid = "NO" if (a + b <= c) or (b + c <= a) or (c + a <= b) else "YES"
print(valid)
