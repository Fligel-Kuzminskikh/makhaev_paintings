
# создает список параметров и проводит для них тестирование DBSCAN
# в зависимости от флага выводит на печать результаты 
# возвращает лист словарей вида {'eps':значение eps, 'min_samples':минимальный размер кластера, 'n_clusters_':количество кластеров, 'n_noise_':количество шума}
# отсортированный по возрастанию шума

# X - список фичей,
# eps_list - список eps для которых будет формироваться лист параметров
# samples_list = [3, 4] - список min_samples для которых будет формироваться лист параметров
# print=False - булево значение печатать результаты тестов 
# getScore = False - печатать оценку кластеризации
# Y='' - список классов для валидации
# score_funcs_list = '' - список кортежей формата (название_функции, функция) (по умолчанию global_score_funcs)
def set_dbscan_param(X, eps_list, samples_list = [3, 4], print=False, getScore = False, Y=''):
    min_samples_list = []
    for i in samples_list:
        min_samples_list = min_samples_list + len(eps_list) * [i]
    param_list = pd.DataFrame(list(zip(eps_list*len(samples_list), min_samples_list)),columns =['eps', 'min_samples']).to_dict(orient='records')
    if print:
       print_dbscan_test(X, param_list, getScore = getScore, Y=Y)
    else:
       return get_dbscan_test(X, param_list, getScore = getScore, Y=Y)
