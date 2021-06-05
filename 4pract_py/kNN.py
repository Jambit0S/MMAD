import numpy as np
import math
from sklearn.preprocessing import normalize

def k_nearest(X, k, obj):
# нормализация столбцов(кроме последнего) 
  sub_X = X[:, 0:-1]
  new = np.zeros((17, 2))
  new[:16,:2] = sub_X
  new[16] = obj
  new = normalize(new, axis=0, norm='max')
  for i in range(sub_X.shape[0] - 1):
      sub_X[i] = new[i]
      obj = new[16]  
  print(obj)
  print(new[16])
# евкливово расстояние от obj до каждого объекта sub_X 
  a = [dist(i, obj) for i in sub_X]
# получение индексов соседей по мере их удаления от obj
  b = np.argsort(a)
  b = b[0:k]    
# выбор в отдельный вектор классы k ближайших соседей
  nearest_classes = X[[b], -1]    
# определение наиболее встречающегося класса в этом векторе 
  unique, counts = np.unique(nearest_classes, return_counts=True)
  object_class = unique[np.argmax(counts)]
# возвращение полученного значения из функции 
  return object_class

# вычисление евклидова расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))
