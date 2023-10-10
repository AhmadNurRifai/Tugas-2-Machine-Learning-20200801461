#Soal 1
nama = "Ahmad Nur Rifai"
nim = "20200801461"
mata_kuliah = "Machine Learning"

print("DATA DIRI")
print("Nama : ", nama)
print("NIM  : ", nim)
print("Perkuliahan: ", mata_kuliah)

#soal 2
import numpy as np

# Membuat matriks C
matriksC = np.array([[1, 2, 3],
                     [4, 5, 6]])

print(matriksC)


#Soal 3
import numpy as np

# Membuat matriks dengan orde 3x2
matriks = np.array([[2, 2],
                   [2, 2],
                   [2, 2]])

print(matriks)

#Soal 4
import numpy as np

#Soal 5
import numpy as np

# Membuat matriks 4x8 dengan nilai 32
matriks = np.full((4, 8), 32)

print(matriks)

#Soal 6
import numpy as np

# Membuat matriks 3x30 dengan nilai acak antara 1 hingga 5
matriks = np.random.randint(1, 6, size=(3, 30))

print(matriks)

