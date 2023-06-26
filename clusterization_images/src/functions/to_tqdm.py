
# для передачи в счетчик выполнения обработки списка любой функцией

# item_list - список элементов
# method - функция-обработчик
def to_tqdm(item_list, method):
  rezult_list = []
  for res in tqdm(map(method, (i for i in item_list)),
                     total = len(item_list)):
             rezult_list.append(res)
  return rezult_list
