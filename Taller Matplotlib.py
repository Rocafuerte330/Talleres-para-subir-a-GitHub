import numpy as np
import matplotlib.pyplot as plt
# print("PRIMER PUNTO")
# x = np.arange(0, 360)
# x = np.radians(x)
# y = np.sin(x)
# plt.xlim(0,7)
# plt.ylim(-1,1)
# plt.title("Función Seno")
# plt.ylabel("sin(x)")
# plt.xlabel("Ángulo(rad)")
# plt.plot(x,y, "m--")
# plt.show()
# print("-----------------------------------------------------------------------------------------------------")
# x = np.arange(0, 360)
# x = np.radians(x)
# y = np.sin(x)
# plt.xlim(0,7)
# plt.ylim(-1,1)
# plt.title("Función Seno")
# plt.xlabel("Ángulo(rad)")
# plt.plot(x,y, "m--", label =  "Función Seno")
# plt.plot(x,np.cos(x), "g", label = "Función Coseno")
# plt.legend(loc = "upper right")
# plt.show()

# print("-----------------------------------------------------------------------------------------------------")
# print("SEGUNDO PUNTO: GENERAR UN HISTOGRAMA")
# import seaborn as sns
# datos = np.random.randn(50000) *2 + 20  
# plt.title("Histograma")
# plt.xlabel("Valor x")
# plt.ylabel("Probabilidad")
# plt.xlim(12,30)
# plt.ylim(0,0.25)
# # Graficar la línea de densidad que sigue el borde del histograma
# sns.kdeplot(datos, color='m',linestyle="--", linewidth=1.5)
# plt.hist(datos, bins=150, density=True, alpha=0.2, color="red",linewidth=0.1, rwidth=1,edgecolor="black")
# plt.show()

# print("-----------------------------------------------------------------------------------------------------")
# print("TERCER PUNTO")
# x = np.arange(-10,10)
# plt.xlim(-6,6)
# plt.xticks(np.arange(-10, 11, 1))
# plt.ylim(-10,10)
# plt.yticks(np.arange(-10, 11, 1))
# plt.axhline(y=0, color='black', linewidth=0.8, linestyle='--')
# plt.axvline(x=0, color='black', linewidth=0.8, linestyle='--')
# plt.plot(x,2*x+1)
# plt.grid()
# plt.plot(x,-(x**2))
# plt.show()

print("-----------------------------------------------------------------------------------------------------")
print("EJERCICIOS PARA SUBIR A GITHUB")
# 1.Cree un vector de size = 720, con valores aleatorios
# 2.Haga reshape de (120, 6)
# 3.Haga la transpuesta de la matriz y cree dos copias, una usando order F y la otra usando order C
# 4.Genere un subplot con 6 paneles, usando la versión “a mano”, y conproporciones diferentes
# 5.En cada panel hacer un grafico diferente (plot, scatter, bar, histograma, pie, etc) , sus datos serán cada fila de la matriz anterior. 
# 6.Poner títulos, labels,legends, cuadrículas.

print("1. Vector size = 720 con valores aleatorios")
vector = np.random.random((720))
print(f"""La dimensión del vector es: {vector.ndim}
El vector es: {vector[0:10]}...
""")

print("2. Reshape de (120,6)")
vector_reshape = vector.reshape(120,6)
print("Número de dimensiones: ", vector_reshape.ndim)
print("Forma: ", vector_reshape.shape)
print("Tamaño: ", vector_reshape.size)
print(f"{vector_reshape[0:10,:]}...")

print("\n3. Transpuesta y dos copias de la matriz(vector_reshape)")
copiaF = vector_reshape.T.copy()
copiaC = vector_reshape.T.copy()
print(f"La forma de la copia de la matriz en orden F es: {copiaF.shape}")
print(f"La forma de la copia de la matriz en orden C es: {copiaC.shape}")
print(f"La forma de la matriz en oiginal es: {vector_reshape.shape}")

print("\n4. Suplot de 6 paneles 'A mano'")
ax1 = plt.axes([0.3, 0.4, 0.1, 0.1]) 
plt.text(0.5, 0.5, "ax1",fontsize=18, ha='center')
ax2 = plt.axes([0.9, 0.65, 0.2, 0.8])
plt.text(0.5, 0.5, "ax2",fontsize=18, ha='center')
ax3 = plt.axes([0.01, 0.01, 0.3, 0.3])
plt.text(0.5, 0.5, "ax3",fontsize=18, ha='center')
ax4 = plt.axes([0.9,0.1,0.5,0.1])
plt.text(0.5, 0.5, "ax4",fontsize=18, ha='center')
ax5 = plt.axes([0.1, 0.9, 0.7, 0.3])
plt.text(0.5, 0.5, "ax5",fontsize=18, ha='center')
ax6 = plt.axes([0.5, 0.2, 0.1,0.2])
plt.text(0.5, 0.5, "ax6",fontsize=18, ha='center')
plt.show()

print("\n5. En cada panel hacer un grafico diferente")
print("6. Poner títulos, labels,legends, cuadrículas")
x = np.arange(360)
y = np.arange(360)
ax1 = plt.axes([0.3, 0.4, 0.1, 0.1]) 
plt.title("Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.plot(x,y, label = "y(x)")
#----------------------------------------------------------------------
ax2 = plt.axes([0.9, 0.65, 0.2, 0.8])
plt.title("Barras")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.bar(x,y, label = "y(x)")
#----------------------------------------------------------------------
ax3 = plt.axes([0.01, 0.01, 0.3, 0.3])
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
size = 100 * rng.rand(100)
plt.title("Disperción")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.scatter(x, y, c = colors, s = size, alpha = 0.3, cmap = "inferno")
plt.colorbar()
#----------------------------------------------------------------------
ax4 = plt.axes([0.9,0.1,0.5,0.1])
x = np.linspace(20, 50, 30)
dy = 0.5
y =np.sin(x) + dy*np.random.rand(30)
plt.title("Barra_Error")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.errorbar(x, y, yerr = dy, fmt = ".k")
#----------------------------------------------------------------------
ax5 = plt.axes([0.1, 0.9, 0.7, 0.3])
import seaborn as sns
datos = np.random.randn(50000) *2 + 20  
plt.title("Histograma")
plt.xlabel("Valor x")
plt.ylabel("Probabilidad")
plt.grid()
mean = [0,0]
cov = [[1,1],[1,2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T
plt.hist2d(x, y, bins=150, cmap = "Blues")
#----------------------------------------------------------------------
ax6 = plt.axes([0.5, 0.2, 0.1,0.2])
labels = ["Oro", "Agua", "Sangre"]
color = "yellow", "blue", "red"
size = [10,60,30]
plt.title("Pie")
plt.pie(size, labels= labels, colors=color)
plt.show()