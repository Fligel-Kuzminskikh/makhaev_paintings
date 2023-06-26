
# метод для нахождения оптимального eps для DBSCAN,
# используется для дальнейшего построения графика "колена"
# возвращает средние дистанции между точками набора, полученные методом NearestNeighbors

# X - список фичей,
# num = 21 -  параметр earestNeighbors, количество соседей = MinPts, которое будет использоваться в DBSCAN,
# print_plt = False - булево значение печать график или нет
# scale  -   булево значение стандартизировать или нет перед применение NearestNeighbors
# norm  -   булево значение нормализовать или нет перед применение NearestNeighbors
def get_neighbors(X, num = 21, print_plt = False, scale = True, norm = True):
  neigh = NearestNeighbors(n_neighbors=num)
  if scale:
       scaler = StandardScaler()
       X = scaler.fit_transform(X)
  if norm:
       X = normalize(X)
  nbrs = neigh.fit(X)
  distances, indices = nbrs.kneighbors(X)
  distances = np.sort(distances[:,num-1], axis=0)
  if print_plt:
     fig = plt.figure(figsize = (18, 9))
     plt.plot(distances)
     plt.xlabel('Points')
     plt.ylabel('Distance')

  return distances


# возвращает значенеи "колена"

# dist - дистанции между соседями, полученные методом NearestNeighbors
# print_plt = False - булево значение печать график или нет
def get_kneeLocatore(dist, print_plt = False):
    x, y = np.arange(len(dist)), dist
    kneedle = KneeLocator(x, y, S=1.0, curve="convex", direction="increasing")
    if print_plt:
       kneedle.plot_knee_normalized()
    
    knee_point = kneedle.knee
    elbow_point = kneedle.elbow
    return knee_point, elbow_point
