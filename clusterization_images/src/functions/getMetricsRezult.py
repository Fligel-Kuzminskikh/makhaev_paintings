
# возвращает результаты проверки кластеризации различными метриками

# x- предсказанные метки, y - истинные метки
# score_funcs_list - список кортежей формата (название_функции, функция)

def getMetricsRezult(x, y, score_funcs_list):
    rezult_list = []
    for func in score_funcs_list:
        score_func = func[1]
        score_name = func[0]
        rezult = score_func(y, x)
        rezult_list.append({'score_name': score_name, 'score':rezult})
    return rezult_list
        
        
