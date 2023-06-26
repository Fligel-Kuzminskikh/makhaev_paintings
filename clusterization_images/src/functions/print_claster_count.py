
# выводит на печать словарь вида {кластер:количество элементов в нем}

# labels - список лейблов
def print_claster_count(labels):
    print(dict(Counter(labels)))
