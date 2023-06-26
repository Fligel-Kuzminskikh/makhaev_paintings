
# печатает результаты кластерезации методом DBSCAN с различными параметрами

# X - список фичей,
# param_list - список словарей вида {'eps':значение eps, 'min_samples':минимальный размер кластера}
def print_dbscan_test(X, param_list):
    for row in param_list:
       min_samples = row['min_samples']
       eps = row['eps']
       labels =  get_dbscan_label_test(X, eps=eps, min_samples=min_samples)
       
       n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
       n_noise_ = list(labels).count(-1)
       print(f'eps={eps}, min_samples={min_samples}')
       print(f'Количество кластеров : {n_clusters_}. Количество шума: {n_noise_} ')
       print('+'*100)
