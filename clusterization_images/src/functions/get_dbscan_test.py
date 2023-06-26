
#  результаты кластерезации методом DBSCAN с различными параметрами
# возвращает лист словарей вида {'eps':значение eps, 'min_samples':минимальный размер кластера, 'n_clusters_':количество кластеров, 'n_noise_':количество шума}
# отсортированный по возрастанию шума

# X - список фичей,
# param_list - список словарей вида {'eps':значение eps, 'min_samples':минимальный размер кластера}
# min_claster_count = 2 - минимальное количество кластеров, которое должно получится в выборке
# getScore = False - печатать оценку кластеризации
# Y='' - список классов для валидации
# score_funcs_list = '' - список кортежей формата (название_функции, функция) (по умолчанию global_score_funcs)

def get_dbscan_test(X, param_list, min_claster_count = 2, getScore = False, Y='', score_funcs_list = ''):
    rezult = []
    for row in param_list:
       min_samples = row['min_samples']
       eps = row['eps']
       labels =  get_dbscan_label_test(X, eps=eps, min_samples=min_samples)       
       n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
       n_noise_ = list(labels).count(-1)
       if getScore:
          score_funcs_list = score_funcs_list if score_funcs_list else global_score_funcs
          rezult.append({'eps':eps, 'min_samples':min_samples, 'n_clusters_':n_clusters_, 'n_noise_':n_noise_, 'score_list':getMetricsRezult(labels, Y, score_funcs_list)})
       else:
          rezult.append({'eps':eps, 'min_samples':min_samples, 'n_clusters_':n_clusters_, 'n_noise_':n_noise_})

    rezult = list(filter(lambda item: item['n_clusters_'] > min_claster_count, rezult))
    rezult = sorted(rezult, key=lambda item: item['n_noise_'])
    
    return rezult
