
# выводит на печать результаты кластаризации DBSCAN

# labels - список полученных лейблов
def print_сlustering_param(labels):
  n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
  n_noise_ = list(labels).count(-1)
  print(f'Количество кластеров : {n_clusters_}. Количество шума: {n_noise_} ')
