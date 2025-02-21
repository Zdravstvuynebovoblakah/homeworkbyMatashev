import numpy as np
import array
import sys 
#Типы данных Python
x = 1
print(type(x))
print(sys.getsizeof(x))
x = 'hello'
print(type(x))
x = True
print(type(x))
l1 = list({})
print(sys.getsizeof(l1))
l2 = list([1,2,3])
print(sys.getsizeof(l2))
l3 = list([1,'2',True])
print(sys.getsizeof(l3))
#array - только для 1 типа данных
a1 = array.array('i', [1,2,3])
print(sys.getsizeof(a1))
print(type(a1))

## 1. Какие еще существуют коды типов?
#    - 'b' - signed char (целое со знаком) 
#    - 'B' - unsigned char (целое без знака)
#    - 'u' - Unicode character (старая строка юникода)
#    - 'w' - Unicode character (новая строка юникода)
#    - 'h' - signed short (короткое целое со знаком)
#    - 'H' - unsigned short (короткое целое без знака)
#    - 'i' - signed int (целое со знаком)
#    - 'I' - unsigned int (целое без знака)
#    - 'l' - signed long (длинное целое со знаком)
#    - 'L' - unsigned long (длинное целое без знака)
#    - 'q' - signed long long (очень длинное целое со знаком)
#    - 'Q' - unsigned long long (очень длинное целое без знака)
#    - 'f' - float  с плавающей запятой)
#    - 'd' - double (двойная точность, с плавающей запятой)

## 2. НАпиишите код подобный приведенному выше но с другим типом
a2 = array.array('f', [1.24, 4, 8])
print(sys.getsizeof(a2))
print(type(a2))

np.array([1, 2, 3])
print(type(a1),a1)
#повышающее приведение типов
a = np.array([1.23, 2, 3, 4], dtype=int)
print(type(a), a)
a = np.array([range(i, i+3) for i in [2, 4, 6]])
print(a, type(a))
a = np.zeros(10, dtype = int)
print(a, type(a))
print(np.ones((3,5), dtype=float))
print(np.full((4,5), 3.1415))
print(np.arange(0, 20, 2))
print(np.eye(4))
##3 Напишите код для создания массива с 5 значениями располагающимися через равные интервалы в диапазоне от 0 до 1
a3 = np.linspace(0, 1, 5)
#print(a3)
## 4Напиишитие код для создания массива с 5 нормально распределенными слуйчаными значениями в диапазоне от 0 до 1
a4 = np.random.uniform(0, 1, 5)
#print(a4)
## 5 Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат ожиданием == 0 и дисперсией 1
a5 = np.random.normal(0, 1, 5)
#print(a5)
## 6 НАпишите код для создания массива с 5  сулчайными числами в диапазоне [0, 10]
#print(np.array(i for i in range(5) x(i) == math.floor(math.rand(0,10))))

##  МАССИВЫ
# x1=np.random.randint(10,size=3)
# x2=np.random.randint(10,size=(2,3))
# x3=np.random.randint(10,size=(2,3,4))
# print(x2)
# print(x1.ndim, x1.shape, x1.size)
# print(x2.ndim, x2.shape, x2.size)
# print(x3.ndim, x3.shape, x3.size)

# a=np.array([1,2,3,4,5])
# print(a[-2])
# a[1]=20
# print(a)
# a=np.array([[1,2],[3,4]])
# print(a[0,0])
# a[1,0]=100
# print(a)

# a=np.array([1,2,3,4])
# b=np.array([1.0,2,3,4])
# print(a)
# print(b)

# a[0]=10
# print(a)
# a[0]=10.122
# print(a)

# срез [нач:кон:шаг]

# a=np.array([1,2,3,4,5,6])

# print(a[:3]) # до 3-го
# print(a[3:])
# print(a[1:-1])
# print(a[1::2])
# print(a[:6:2])

# print(a[::-1])# меняет старт и финиш
# #[кон:нач:шаг]
# 7. Написать код для создания срезов массива 3 на 4
a7 = np.array([[100, 12,  33,  22],
              [7, 6,  7,  21],
              [911, 3, 11, 79]])
# - первые две строки и три столбца
a71 = a7[:2, :3]
#print(a71)
# - первые три строки и второй столбец
a72 = a7[:3, 1:2]
#print(a72)
# - все строки и столбцы в обратном порядке
a73 = a7[::-1, ::-1]
#print(a73)
# - второй столбец
a74 = a7[:, 1]
#print(a74)
# - третья строка
a75 = a7[2, :]
#print(a75)

# #срез=ссылка
# a=np.array([1,2,3,4,5,6])

# b=a[:3]
# b[0]=100
# print(a)
# 8. Продемонстрируйте, как сделать срез-копию
a8 = np.copy(a)
a8[1][0]=1111
# print(a)
# print(a8)

# a=np.arange(1,13)

# print(a.reshape(2,6))
# print(a.reshape(3,4))

# 9. Продемонстрируйте использование new  axis для получения вектора столбца и вектора строки
a9 = np.array([1, 2, 3, 4, 5])
#print(a9)

column = a9[:, np.newaxis]
#print(column)

row = a9[np.newaxis]
#print(row)

# x=np.array([1,2,3])
# y=np.array([4,5])
# z=np.array([6])

# print(np.concatenate([x,y,z]))

# x=np.array([1,2,3])
# y=np.array([4,5,6])

# r1=np.vstack([x,y])
# print(r1)

# print(np.dstack([r1,r1]))
# 10. Как работает метод dstack
a = np.array([[7, 0], [366, 14]])
b = np.array([[5669, 3266], [213, 457]])
c = np.dstack((a, b))
#print(c)
a = np.array([10, 12, 33])
b = np.array([71, 25, 37])
c = np.dstack((a, b))
#print(c) 
#11. Как работают методы split, vsplit, hsplit, dsplit
# - split
a = np.array([[[1], [2], [3]], [[4],[ 5], [6]], [[7], [8], [9]]])
b = np.split(a, 3, 0)
c = np.split(a, 3, 1)
d = np.split(a, 1, 2)
print(b,c,d)
# vsplit = split( , , 0), hsplit = split( , , 1), dsplit = split( , , 2)

# вычисления с массивами
# векторезированая опер.=к каждому

# x=np.arange(10)
# print(x)

# print(x*2+1)


# print(np.add(np.multiply(x,2),1))

# универсальные ф-ии - ф-ии ...

# - -1 / // ** %
# 12. Привести пример использования всех универсальных функций, которые были приведены

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

# 12. Арифметические операции
print( np.add(x, y))      # Сложение
print( np.subtract(x, y)) # Вычитание
print( np.multiply(x, y)) # умножение
print( np.divide(y, x))   # Деление
print( np.negative(x))    # Унарный минус
print( np.floor_divide(x,y)) #Деление с округлением
print( np.power(x,y))    # Степень
print( np.mod(x,y))      # Остаток от деления
print( np.sin(x))        # Синус
print( np.cos(x))        # Косинус
print( np.tan(x))        # Тангенс:
print( np.arcsin(x))     # Арксинус
print( np.arccos(x))     # Аркосинус
print( np.arctan(x))     # Арктангенс:
print( np.exp(x))        # Натуральный логарифм
print( np.log(x))        # Экспонента

 
x=np.arange(5)

#y=np.array([0,0,0,0,0,0,0,0,0,0])
# y=np.zeros(10)
# print(y)
# print(np.multiply(x,10, out=y[::2]))
# print(y)

# x= np.arange(1,5)

# print(x)
# print(np.add.accumulate(x))

x=np.arange(1,10)
print(np.multiply.outer(x,x))