
# применяет OPTICS с переданными параметрами
# возвращает список полученных лейблов

# X - список фичей,
# min_samples=5, xi=0.05, min_cluster_size=0.05, cluster_method='xi',  metric='co - параметры OPTICS,
# (подробней https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS)
# scale  -   булево значение стандартизировать или нет перед применение OPTICS
# norm  -   булево значение нормализовать или нет перед применение OPTICS
def get_OPTICS_label_test(X, 
                          min_samples=5, xi=0.05, min_cluster_size=0.05, cluster_method='xi',  metric='cosine',                           
                          scale = True, norm = True):

    optics_model = OPTICS(min_samples=min_samples, metric=metric, cluster_method=cluster_method, xi=xi, min_cluster_size=min_cluster_size)
    
    if scale:
       scaler = StandardScaler()
       X = scaler.fit_transform(X)
    if norm:
       X = normalize(X)
    optics_model.fit(X)
        
    labels = optics_model.labels_[optics_model.ordering_]
    
    return labels
    
