import pandas as pd
import numpy as np

def beginning():
    py_list = [3,12,24,9]

    print(3*py_list)

    np_array = np.array(py_list)
    print(3*np_array)

    np_array = np.array([3,12,24,9])
    zero_array = np.zeros(4)
    ones_array = np.ones(4)
    spaced_array = np.linspace(7,40,12)
    random_array = np.random.randint(1,13,4)
    py_list = np_array.tolist()

def dimensions():
    np_array = np.array([1,2,4,15])
    np_2d_array = np.array([[3,4,5],[5,14,23],[12,6,8],[34,21,27]])
    np_3d_array = np.array([[[3,1,2],[6,3,1],[7,9,2]],
                            [[5,12,22],[61,32,13],[74,91,22]],
                            [[31,11,22],[611,33,12],[71,92,23]]])
    print(np.shape(np_array))
    print(np.shape(np_2d_array))
    print(np.shape(np_3d_array))
    print(np.reshape(np_2d_array,(2,6)))
    print(np.reshape(np_2d_array,12))
    print(np.reshape(np_2d_array,(1,12)))
    print(np_2d_array.flatten())

def methods():
    np_array = np.array([12,6,34,-2,7,28])
    print(type(np_array))
    print(np_array.max())
    print(np.max(np_array))
    print(np_array.argmax())

    print(np.sort(np_array))
    print(np.sort(np_array)[::-1])
    sort_array = np.sort(np_array) #copia
    np_array.sort() #original ordenado

    np_2d_array = np.array([[3,4,5],[5,14,23],[12,6,8],[34,21,27]])
    print(np.sort(np_2d_array,axis=0))
    print(np.sort(np_2d_array,axis=1))

    print(np.mean(np_array))
    print(np.std(np_array))

    arrays = np.array([1,2,4,15,0])
    arrays_ = np.array([3,4,1,150,0])
    print(arrays + arrays_)
    print(arrays - arrays_)
    print(arrays * arrays_)
    print(arrays / arrays_)
    print(arrays ** 2)
    print(arrays ** 2)
    print(arrays ** (1/2))
    print(np.sqrt(arrays))

    print(np.log(arrays))
    print(arrays.dot(arrays_))

def index_slices():
    np_array = np.array([1,2,4,15])
    np_2d_array = np.array([[3,4,5],[5,14,23],[12,6,8],[34,21,27]])

    a = np_array[:]
    a = np_array[2:]
    a = np_array[:4]
    a = np_array[2:5]
    a = np_array[-3:]
    a = np_array[-3:-1]

    a = np_array[-3:-1]
    a[:] = 5 #muda o array atual na memoria

    a = np_array[-3:-1].copy()
    a[:] = 5 #muda o array copy

    print(np_2d_array[:2,:2])
    print(np_2d_array[[0,2],[1,2]])
    print(np_2d_array[[[0],[2]],[1,2]])

    print(np_array > 5)
    print(np_array[np_array > 5])
    np_array[np_array > 5] = 55