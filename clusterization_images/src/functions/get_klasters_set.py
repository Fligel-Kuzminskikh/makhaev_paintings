
# нахождение оптимального количества кластеров для KMeans,
# методом силуэта
# возвращает средние значение силуэта для выбранного количества кластеров

# X - список фичей,
# num = 10 -  параметр KMeans, количество примененеий метода для рассчета среднего значения силуэта,
# scale  -   булево значение стандартизировать или нет перед применение KMeans
# norm  -   булево значение нормализовать или нет перед применение KMeans

def get_KMeans_silhouette_score(X, k, num = 10, scale = True, norm = True):
    kmeans = KMeans(n_clusters=max(k,2), n_init= 'auto', random_state=num)
    if scale:
       scaler = StandardScaler()
       X = scaler.fit_transform(X)
    if norm:
       X = normalize(X)
    kmeans.fit(X)
    cluster_labels = kmeans.labels_
    silhouette_avg = silhouette_score(X, cluster_labels)

    return silhouette_avg

# рассчитывает значение силуэта для различных k в заданном диапазоне
# возвращаем словарь вида {количество кластеров:значение силуэта}

# X - список фичей,
# start = 10, end = 110, step_list = [10, 5, 1] - диапазон в которых проверяме значения k и шаг с которым выполняем проверку
# set_len = 3 - размер возвращаемого словаря
# scale  -   булево значение стандартизировать или нет перед применение KMeans
# norm  -   булево значение нормализовать или нет перед применение KMeans
def get_klasters_set(X, start = 10, end = 110, step_list = [10, 5, 1], set_len = 3, scale = True, norm = True):
    current_start = start
    current_end = end
    for step in step_list:
        # считаем для каждого k значение силуэта        
        k_dict = {max(k, 2): get_KMeans_silhouette_score(X, k, scale = scale, norm = norm) for k in range(current_start, current_end, step)}
        # сортируем результаты по значениям силуэта
        k_dict = dict(sorted(k_dict.items(), key=lambda item: item[1], reverse = True))

        # print(k_dict)
        # берем два k с самыми высокими значениями и сортируем их по возрастанию k
        # таким образом получаем новые значения current_start и current_end
        param = sorted(list(k_dict.items())[0:2])
        current_start, current_end = param[0][0], param[1][0] + 1

    # берем первые значения из списка (по умолчанию - 3)
    rezult = list(k_dict.items())[0:set_len]
    # получем список кластеров
    #return [i[0] for i in rezult]
    return rezult
