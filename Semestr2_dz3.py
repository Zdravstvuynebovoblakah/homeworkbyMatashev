import numpy as np
import pandas as pd
# Pandas - расширение NumPy (структурированные массивы). Строки и столбцы индексируются метками, а не только числовыми значениями 
# Series, DataFrame, Index

## Series
# data = pd.Series ([0.25, 0.5, 0.75, 1.0])
# print (data)
# print (type (data))

# print (data.values)
# print (type (data.values))

# print (data.index)
# print (type (data.index))

# data = pd.Series ([0.25, 0.5, 0.75, 1.0])

# print (data[0])
# print (data[1:3])

# data = pd.Series ([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print (data)

# print (data['a'])
# print (data['b': 'd'])

# print (type(data.index))

# data = pd.Series ([0.25, 0.5, 0.75, 1.0], index= [1, 10, 7, 'd']) 
# print (data)

# print (data[1])
# print (data[10: 'd'])

# population_dict = {
# 'сity 1': 1001,
# 'city_2': 1002,
# 'city 3': 1003,
# 'city_4': 1004,
# 'city 5': 1005,
# }
# population = pd. Series (population_dict)
# print (population)

# ## DataFrame двумерный массив с явно определенными индексами. 
# # Последовательность "согласованных" объектов Series 
# population_dict = {
# 'city_1': 1001,
# 'city 2': 1002,
# 'city_3': 1003,
# 'city_4': 1004,
# 'city_5': 1005,
# }

# area_dict = {
# 'city_1': 9991,
# 'city_2': 9992,
# 'city 3': 9993,
# 'city 4': 9994,
# 'city 5': 9995,
# }

# population = pd. Series (population_dict)
# area = pd.Series (area_dict)

# # print (population)
# # print (area)

# states = pd.DataFrame({
# 'populationl': population, 
# 'areal': area,
# })
# print (states)
# print (states.values) 
# print (states.index) 
# print (states.columns)
# print (type (states.values)) 
# print (type (states.index)) 
# print (type (states.columns))

#print (states['areal'])

# DataFrame. Способы создания 
# - через объекты Series
# - списки словарей
# - словари объектов ѕеrіеѕ
# - двумерный массив NumPy
# - структурированный массив Numpy

# Index - способ организации ссылки на данные объектов Seriese и DataFrame. 
# Index неизменяем упорядочен, является мультимножеством (могут быть повторяющиеся значения)
# ind = pd.Index([2,3,5,7,11])
# print (ind[1])
# print (ind[::2])
# ind[1] = 5
# Index - следует соглашениям объекта set (python)

# indA = pd.Index([1,2,3,4,5])
# indB = pd.Index([2,3,4,5,6])

# print(indA.intersection(indB))

# Выборка данных из Series - словарь
# data = pd.Series ([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print ('a' in data)
# print ('z' in data)
# print (data.keys())
# print (list(data.items()))

# - массив
# data = pd.Series ([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print (data['a': 'c'])
# print (data[0:2])
# print (data[ (data > 0.5) & (data < 1)])
# print (data[['a', 'd']])

# атрибуты - индексаторы

# data = pd.Series ( [0.25, 0.5, 0.75, 1.0], index=[1, 3, 10, 15])
# print (data[1]) 
# print (data.loc[1])
# print (data.iloc[2])

# выборка из DataFrame
# аля словарть

# pop = pd.Series( {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_4': 1004,
#     'city_5': 1005,
# }
# )

# area = pd.Series( {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_4': 9994,
#     'city_5': 9995,
# }
# )


#data = pd.DataFrame({'area1': area, 'pop1': pop, 'pop': pop})
# print (data)

# print (data['area1'])
# print (data.area1)

# print (data.pop1 is data['pop1'])
# print (data.pop is data['pop'] )

# data['new'] = data['area1']
# data['new1'] = data['area1'] / data['pop']
# print (data)

# двумерный NumPy-массив
# data = pd.DataFrame({'area1' : area, 'pop1': pop})
# print (data)

# print(data.values)

# print (data.T)
# print(data['area1'])
# print (data.values[0:3])

# атрибуты-индексаторы
# print (data)
# print (data.iloc[:3, 1:2])
# print (data.loc[: 'city_4', 'pop1': 'pop'])
# print (data.loc[data['pop'] > 1002, ['area1', 'pop']])
# data.iloc[0,2]= 999999
# print (data)

#rng = np.random.default_rng()
# s = pd.Series (rng. integers (0,10,4))
# print (s)
# print (np.exp(s))

# pop = pd.Series( {
#     'city_1': 1001,
#     'city_2': 1002,
#     'city_3': 1003,
#     'city_41': 1004,
#     'city_51': 1005,
# }
# )

# area = pd.Series( {
#     'city_1': 9991,
#     'city_2': 9992,
#     'city_3': 9993,
#     'city_42': 9994,
#     'city_52': 9995,
# }
# )
# data = pd.DataFrame({'areal': area, 'popl': pop})
# print (data)

# rng = np.random.default_rng()
# dfA= pd.DataFrame (rng. integers (0,10, (2,2)), columns=['a', 'b']) 
# dfB = pd.DataFrame (rng. integers (0, 10, (3,3)), columns=['a', 'b', 'c'])
# print (dfA)
# print (dfB)
# print (dfA + dfB)

# A = rng. integers (0, 10, (3,4))

# print (A)
# print (A[0])
# print (A- A[0])

# df = pd.DataFrame (A, columns=['a', 'b', 'c', 'd'])
# print (df)

# print (df.iloc[0])
# print (df - df.iloc[0])
# print (df.iloc[0, ::2])
# print (df - df.iloc[0,2])


# NА-значения: NaN, null, -99999
# Pandas. Два способа хранения отсутствующих значений 
# индикаторы Nan, None
# null
# None - объект (накладные расходы). Не работает с sum, min


# vall = np.array([1, None, 2,3]) 
# # print (vall.sum()) #err

# val1 = np.array([1, np.nan, 2,3]) 
# print (val1)

# print (val1.sum()) #не то
# print (np.nansum(val1)) # ок

# x = pd. Series (range (10), dtype=int) 
# print (x)

# x[0] = None
# x[1] = np.nan
# print (x)

# x1 = pd.Series (['a', 'b', 'c']) 
# x1[0] = None
# x1[1] = np.nan
# print (x1)

# x2 = pd.Series ([1,2,3, np.nan, None, pd.NA])
# print (x2)

# x3 = pd.Series ([1,2,3, np.nan, None, pd.NA], dtype='Int32') 
# print (x3)
# print (x3.isnull())
# print (x3[x3.isnull()]) 
# print (x3[x3.notnull()])
# print(x3.dropna())

# df = pd.DataFrame(
# [
# [1,2,3, np.nan, None, pd.NA], 
# [1,2,3,4,None,6],
# [1, np. nan,3,4, np.nan, 6],
# ]
# )

# print (df)
# print (df.dropna ()) 
# print (df.dropna (axis=0)) 
# print (df.dropna (axis=1))

# how
# - all - все значения NA
# - any - хотя бы одно значение
# - thresh=x - хотя-бы x не NA 

# print (df.dropna(axis=1, how='all'))
# print(df.dropna(axis=1, how='any')) 

# 1. Привести различные способы создания объектов типа Series

# - списки Python или массивы NumPy
# Из списка Python
list = [1, 2, 3, 4, 5]
slist = pd.Series(list)
print(slist)

# Из массива NumPy
array = np.array([10, 20, 30, 40])
sarr = pd.Series(array)
print(sarr)

# - скалярные значение
a = 7
sscal = pd.Series(a, index=[0, 1, 2, 3])  
print(sscal)

# - словари
dict = {'a': 1, 'b': 2, 'c': 3}
sdict = pd.Series(dict)
print(sdict)

# 2. Привести различные способы создания объектов типа DataFrame
# - через объекты Series
s1 = pd.Series([1, 2, 3], name='A')
s2 = pd.Series([4, 5, 6], name='B')
df = pd.concat([s1, s2], axis=1)
print(df)

# - списки словарей
data = [
    {'A': 1, 'B': 4},
    {'A': 2, 'B': 5},
    {'A': 3, 'B': 6}
]
df = pd.DataFrame(data)
print(df)

# - словари объектов Series
s1 = pd.Series([1, 2, 3], name='A')
s2 = pd.Series([4, 5, 6], name='B')
data = {'A': s1, 'B': s2}
df = pd.DataFrame(data)
print(df)

# - двумерный массив NumPy
data = np.array([[1, 4], [2, 5], [3, 6]])
df = pd.DataFrame(data, columns=['A', 'B'])
print(df)

# - структурированный массив Numpy
data = np.array([(1, 4), (2, 5), (3, 6)],
                 dtype=[('A', 'i4'), ('B', 'i4')])
df = pd.DataFrame(data)
print(df)

# 3. Объедините два объекта Series с 
# неодинаковыми множествами ключей (индексов) так, 
# чтобы вместо NaN было установлено значение 1

s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 2], index=['b', 'd'])

result = s1.combine_first(s2).fillna(1)
print(result)


# 4. Переписать пример с транслирование для DataFrame так, 
# чтобы вычитание происходило по СТОЛБЦАМ
rng = np.random.default_rng()
A = rng. integers (0, 10, (3,4))
df = pd.DataFrame (A, columns=['a', 'b', 'c', 'd'])

print(df)
print( )
print((df.T - df.iloc[:,0].T).T) # топорный
print( )
print(df.subtract(df.iloc[:,0], axis=0)) # замороченный

# 5. На примере объектов DataFrame
#  продемонстрируйте использование методов ffill() и bfill()
data = {
    'A': [None, 2, 3, 4, np.nan],
    'B': [np.nan, 2, 3, 4, pd.NA],
    'C': [pd.NA, 2, 3, 4, None]
}

df = pd.DataFrame(data)
print(df)

df_ffill = df.ffill()
print(df_ffill)

df_bfill = df.bfill()
print(df_bfill)
