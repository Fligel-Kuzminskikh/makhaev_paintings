
# печатает результаты кластерезации методом DBSCAN с различными параметрами

# X - список фичей,
# param_list - список словарей вида {'eps':значение eps, 'min_samples':минимальный размер кластера}
# getScore = False - печатать оценку кластеризации
# Y='' - список классов для валидации
# score_funcs_list = '' - список кортежей формата (название_функции, функция) (по умолчанию global_score_funcs)
def print_dbscan_test(X, param_list, getScore = False, Y='', score_funcs_list = ''):
    for row in param_list:
       min_samples = row['min_samples']
       eps = row['eps']
       labels =  get_dbscan_label_test(X, eps=eps, min_samples=min_samples)
       
       n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
       n_noise_ = list(labels).count(-1)
       print(f'eps={eps}, min_samples={min_samples}')
       print(f'Количество кластеров : {n_clusters_}. Количество шума: {n_noise_} ')
       print(print_claster_count(labels))
       if getScore:
          score_funcs_list = score_funcs_list if score_funcs_list else global_score_funcs
          score_list = getMetricsRezult(labels, Y, score_funcs_list)
          print(*score_list, sep='\n')
       print('+'*100)
