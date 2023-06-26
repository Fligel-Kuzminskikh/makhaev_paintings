
# создает словарь deskriptors, переданных изображений
# возвращает список deskriptors переданных изображений

# sift_dict - словарь вида 
# {'img':вектор изображения формата CV2, 'gray':вектор ч/б изображения формата CV2, 'title':название изображения, 'kp':массив ключевых точек}
def set_sift_des(sift_dict):  
  gray = pd.DataFrame(sift_dict)['gray'].tolist()
  # находим минимальное количество ключевых точек для всех изображений
  len_kp_list = [len(item['kp']) for item in sift_dict]
  lemit = min(set(len_kp_list)) 
  # Оставляем лучшие точки
  kp_list = [item['kp'][:lemit] for item in sift_dict]  
  kp_dict = pd.DataFrame({'gray': gray, 'kp': kp_list}).to_dict(orient='records')
  
  des_list = to_tqdm(kp_dict, eval('get_sift_des'))

  return des_list
