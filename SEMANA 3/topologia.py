import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Elementos del conjunto
X = {1, 2, 3}

# Colección de subconjuntos
T1 = [{}, {1}, {1, 2}, {1, 2, 3}]

# Creación de la figura
plt.figure(figsize=(10, 10))

# Definición de los subconjuntos para el diagrama de Venn
subsets = (1, 0, 0, 1, 1, 0, 1)

# Creación del diagrama de Venn
venn = venn3(subsets=subsets, set_labels=('1', '2', '3'))

# Etiquetas para cada conjunto
venn.get_label_by_id('100').set_text('1')
venn.get_label_by_id('110').set_text('1, 2')
venn.get_label_by_id('111').set_text('1, 2, 3')

# Mostrar el gráfico
plt.title("Diagrama de Venn para la colección T1")
plt.show()
