import numpy as np
import random

def dist(A, B):
  # TODO: реализуйте вычисление евклидова расстояния для двух точек A и B в N-мерном пространстве
  # Помните, что размерность пространства может быть произвольной (не только 2D).
  # Для взятия разностей по каждому измерерию можно использовать код: A - B
  # Для возведения в квадрат можете использовать оператор ** (например, 3**2 == 9) или функцию np.power
  # Для вычисления суммы используйте функцию sum или np.sum
  # Для вычисления квадратного корня используйте функцию np.sqrt
  # r = ...
  
    r = 0
    for i in range(len(A)):
        r += (A[i] - B[i])*(A[i] - B[i])
    print("r = ", np.sqrt(r),"A = ", A,"B = ", B)
    return np.sqrt(r)    

# возвращает список индексов ближайших центров по каждой точке
def class_of_each_point(X, centers):
  m = len(X)
  k = len(centers)

  # матрица расстояний от каждой точки до каждого центра
  distances = np.zeros((m, k))
  for i in range(m):
    for j in range(k):
      distances[i, j] = dist(centers[j], X[i])

  # поиск ближайшего центра для каждой точки
  return np.argmin(distances, axis = 1)


def kmeans(k, X):
  m = X.shape[0]
  n = X.shape[1]
  print("m = ", m, "n = ", n)
  centers = np.ones(shape=(k, n), dtype=float)
  curr_iteration = prev_iteration = np.zeros(m)
#  print(prev_iteration)
  # TODO: сгенерировать k кластерных центров со случайными координатами.
  # Должна получиться матрица случайных чисел размера k*n (k строк, n столбцов).
  # Для генерации матрицы случайных чисел используйте код:
  #   centers = np.random.random((k, n))
  # Функция random генерирует случайные числа в диапазоне от 0 до 1, поэтому
  # не забывайте, что координаты центров не должны выходить
  # за границы минимальных и максимальных значений столбцов (признаков) матрицы X.
  # Для вычисления минимальных и максимальных значений по столбцам (признакам)
  # матрицы X используйте функции min(X, axis=0) и max(X, axis=0) библиотеки NumPy соответственно.
  # centers = ...
  Min = np.min(X, axis=0)
  Max = np.max(X, axis=0)
  for i in range(k):
      for j in range(n):
          centers[i][j] = random.uniform(Min[j], Max[j])
  # приписываем каждую точку к заданному классу
  curr_iteration = class_of_each_point(X, centers)
  # цикл до тех пор, пока центры не стабилизируются
  # TODO: условие выхода из цикла - векторы curr_iteration и prev_iteration стали равны
  # Для сравнения двух массивов NumPy можете использовать один из вариантов:
  #   np.all(a1 == a2), где a1 и a2 массивы NumPy.
  # или
  #   np.any(a1 != a2)
  # Для реализации логического отрицания в Python используйте not
  # Поэкспериментируйте в консоли Python с функциями all и any, чтобы понять, как они работают.
  print(prev_iteration)
  print(curr_iteration)
  
  while True:
    prev_iteration = curr_iteration

    # вычисляем новые центры масс
    for i in range(k):
      sub_X = X[curr_iteration == i,:]
      if len(sub_X) > 0:
        centers[i,:] = np.mean(sub_X, axis=0)

    # приписываем каждую точку к заданному классу
    curr_iteration = class_of_each_point(X, centers)
    if np.all(prev_iteration == curr_iteration):
        return centers
  return centers

