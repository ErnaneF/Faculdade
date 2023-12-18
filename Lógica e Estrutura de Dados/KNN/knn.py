from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Carregando o conjunto de dados Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Dividindo o conjunto de dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criando um classificador k-NN com 3 vizinhos
k = 3
knn_classifier = KNeighborsClassifier(n_neighbors=k)

# Treinando o classificador
knn_classifier.fit(X_train, y_train)

# Fazendo previsões no conjunto de teste
y_pred = knn_classifier.predict(X_test)

# Avaliando a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy * 100:.2f}%')