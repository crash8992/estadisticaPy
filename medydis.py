import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

notas = [5, 6, 10, 8, 9, 6, 4, 7, 5, 4]

media = np.mean(notas)
mediana = np.median(notas)
varianza = np.var(notas, ddof=1)  
desviacion_std = np.std(notas, ddof=1)

# Imprimir resultados
print("Datos:", notas)
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Varianza: {varianza:.2f}")
print(f"Desviación estándar: {desviacion_std:.2f}")

# Boxplot para visualizar la dispersión
plt.figure(figsize=(6, 4))
sns.boxplot(data=notas, orient='h', color='skyblue')
plt.title('Boxplot de Notas de la asignatura')
plt.xlabel('notas')
plt.grid(True)
plt.tight_layout()
plt.show()
