
# сортировка ключевых точек

#kp - массив ключевых точек, полученных из SIFT

def get_sorted_kp(kp):
    return sorted(kp, key = lambda x: x.response, reverse= True)
