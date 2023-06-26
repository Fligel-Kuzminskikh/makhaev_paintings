
# загрузка файлов по словарю
# name - имя
# link_dir - словарь
# sep = "," - разделитель
def csv2DF(name, link_dir = url_dict, sep = ","):
    url = link_dir[name]
    df = pd.read_csv(url, encoding = 'utf8', sep = sep )
    return df
