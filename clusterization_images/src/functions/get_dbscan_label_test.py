
# применяет DBSCAN с переданными параметрами
# возвращает список полученных лейблов

# X - список фичей,
# eps=0.1, min_samples=4, metric='cosine' - параметры DBSCAN,
# (подробней https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN)
# scale  -   булево значение стандартизировать или нет перед применение DBSCAN
def get_dbscan_label_test(X, eps=0.1, min_samples=4, metric='cosine', scale = True, norm = True):
    db = DBSCAN(eps=eps, min_samples=min_samples, metric=metric)
    if scale:
       scaler = StandardScaler()
       X = scaler.fit_transform(X)
    if norm:
       X = normalize(X)
    db.fit(X)
    return db.labels_
