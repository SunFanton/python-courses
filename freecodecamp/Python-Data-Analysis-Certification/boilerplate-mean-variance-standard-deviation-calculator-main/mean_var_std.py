import numpy as np

'''
En NumPy, los términos axis 1 y axis 2 se refieren a los ejes de un arreglo multidimensional. Los ejes son fundamentales para entender cómo se realizan operaciones a lo largo de un arreglo, como la suma, el promedio, la concatenación, etc.

Para entender mejor cómo funcionan, es útil pensar en un arreglo multidimensional como una tabla o matriz:

axis 0: Es el eje de las filas (primer eje, el que va hacia abajo en una matriz 2D).
axis 1: Es el eje de las columnas (segundo eje, el que va hacia los lados en una matriz 2D).
axis 2: Sería el eje adicional para un arreglo tridimensional, donde el eje 2 sería el que va "profundizando" en la tercera dimensión.
Ejemplo con matrices 2D:
Imagina que tienes un arreglo 2D como el siguiente:

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
Este arreglo tiene 3 filas y 3 columnas.

axis 0: Se refiere a las filas. Cuando se aplica una operación a lo largo de axis=0, esta operación se realiza a través de las filas (de arriba a abajo).
axis 1: Se refiere a las columnas. Cuando se aplica una operación a lo largo de axis=1, esta operación se realiza a través de las columnas (de izquierda a derecha).
Ejemplo de operaciones a lo largo de los ejes:
Si quieres sumar todos los elementos a lo largo de un eje específico:

# Sumar a lo largo del eje 0 (filas)
suma_axis0 = np.sum(arr, axis=0)
print(suma_axis0)  # Output: [12 15 18] (suma de cada columna)

# Sumar a lo largo del eje 1 (columnas)
suma_axis1 = np.sum(arr, axis=1)
print(suma_axis1)  # Output: [ 6 15 24] (suma de cada fila)
En arreglos multidimensionales:
Si tienes un arreglo 3D (por ejemplo, un cubo de datos), el axis 2 se refiere al eje en la tercera dimensión. Aquí hay un ejemplo con un arreglo 3D:

arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])

# Sumar a lo largo del eje 0 (primera dimensión)
suma_axis0_3d = np.sum(arr_3d, axis=0)
print(suma_axis0_3d)
# Output: [[[ 6  8]
#           [10 12]]]

# Sumar a lo largo del eje 1 (segunda dimensión)
suma_axis1_3d = np.sum(arr_3d, axis=1)
print(suma_axis1_3d)
# Output: [[[ 4  6]]
#          [[12 14]]]

# Sumar a lo largo del eje 2 (tercera dimensión)
suma_axis2_3d = np.sum(arr_3d, axis=2)
print(suma_axis2_3d)
# Output: [[ 3  7]
#          [11 15]]
'''

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape(3,3)
    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    axis = [0, 1, None]

    for ax in axis:
        mean = np.mean(arr, axis=ax).tolist() if ax is not None else np.mean(arr)
        calculations.get('mean').append(mean)

        variance = np.var(arr, axis=ax).tolist() if ax is not None else np.var(arr)
        calculations.get('variance').append(variance)

        std = np.std(arr, axis=ax).tolist() if ax is not None else np.std(arr)
        calculations.get('standard deviation').append(std)

        maxi = np.max(arr, axis=ax).tolist() if ax is not None else np.max(arr)
        calculations.get('max').append(maxi)

        mini = np.min(arr, axis=ax).tolist() if ax is not None else np.min(arr)
        calculations.get('min').append(mini)

        suma = np.sum(arr, axis=ax).tolist() if ax is not None else np.sum(arr)
        calculations.get('sum').append(suma)

    return calculations


#print(calculate([0,1,2,3,4,5,6,7,8]))