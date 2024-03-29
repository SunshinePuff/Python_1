"""2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. 
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. 
Объяснить полученный результат."""

a = 5
print("%d = %s" % (a, bin(a)))
b = 6
print("%d = %s" % (b, bin(b)))

#бит в позиции 0 первого операнда (a) вычисляется с битом в позиции 0 второго операнда (b),
#соответственно бит в позиции 1 первого операнда (a) 
#вычисляется с битом в позиции 1 второго операнда (b) и т.д. 
print("%d & %d = %d (%s)" % (a,b,a&b,bin(a&b)))

#Битовый оператор ИЛИ (OR) есть бинарным и обозначается символом |. 
#Оператор реализует побитовое логическое сложение по образцу операторов & и ^
print("%d | %d = %d (%s)" % (a,b,a|b,bin(a|b)))

#Битовый оператор исключительное ИЛИ (исключающе ИЛИ XOR) обозначается символом ^ и 
#выполняет операцию сложения по модулю 2 для любого бита операндов.
#Оператор исключающего ИЛИ (XOR) оперирует двоичными разрядами. 
#Каждый операнд рассматривается как последовательность бит.
print("%d ^ %d = %d (%s)" % (a,b,a^b,bin(a^b)))

# сдвига влево << (умножение на 2); 
# сдвига вправо >> (целочисленное деление на 2)
print("%d << 2 = %d (%s)" % (b,b<<2,bin(b<<2))) 
print("%d >> 2 = %d (%s)" % (b,b>>2,bin(b>>2)))


bit_and = 5 & 6 # AND
bit_or = 5 | 6 # OR
bit_xor = 5 ^ 6 # XOR

print(f'Побитовые операции над числами 5 и 6:\n'
      f'5 & 6 = {bit_and}\n'
      f'5 | 6 = {bit_or}\n'
      f'5 ^ 6 = {bit_xor}')