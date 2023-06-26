
# для многоканальной обработки списка любой функцией

# item_list - список элементов
# method - функция-обработчик
def to_pool(item_list, method):
    with Pool(processes=os.cpu_count()) as pool:
         rezult_list = []
         for res in tqdm(pool.imap(method, (i for i in item_list)),
                     total = len(item_list)):
             rezult_list.append(res)
    return rezult_list

def to_tqdm(item_list, method):
  rezult_list = []
  for res in tqdm(map(method, (i for i in item_list)),
                     total = len(item_list)):
             rezult_list.append(res)
  return rezult_list
