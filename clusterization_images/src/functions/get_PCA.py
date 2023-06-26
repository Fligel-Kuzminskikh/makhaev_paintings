
# Сокращение размерности Метод главных компонент
# Возвращает трансформированный список фечей и объект pca

# X - список фичей,
# components = 2 - размерность до которой сокращаем
def get_PCA(X, components = 2):
    pca = PCA(components)  
    projected = pca.fit_transform(X)
    
    return projected, pca
