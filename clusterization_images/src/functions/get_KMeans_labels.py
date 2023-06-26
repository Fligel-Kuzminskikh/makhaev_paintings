
# применяет KMeans с переданными параметрами
# возвращает список полученных лейблов

# X - список фичей,
# k - количество кластеров,
# n_init= 'auto', random_state=1 - параметры KMeans
# scale  -   булево значение стандартизировать или нет перед применение KMeans
# norm  -   булево значение нормализовать или нет перед применение KMeans
# use_centroids = False - использовать переданный массив центройдов
# centroids = '' - центройды
def get_KMeans_labels(X, k, scale = True, norm = True, use_centroids = False, centroids = '', n_init= 'auto', random_state=1):
    if use_centroids:
       # если передаем центройды
       kmeans = KMeans(n_clusters=max(2, len(centroids)), init=centroids, n_init=1, random_state=random_state)
    else:
       kmeans = KMeans(n_clusters=max(k,2), n_init=n_init, random_state=random_state)
    if scale:
       scaler = StandardScaler()
       X = scaler.fit_transform(X)
    if norm:
       X = normalize(X)
    kmeans.fit(X)
    return kmeans.labels_
