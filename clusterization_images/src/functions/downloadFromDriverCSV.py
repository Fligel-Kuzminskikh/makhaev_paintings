
# скачать с гугл-диска таблицу в формате csv
# возвращает таблицу

# url - ссылка доступа, полученная с гугл-диска
def downloadFromDriverCSV(url, sep=','):
   file_id=url.split('/')[-2]
   dwn_url='https://drive.google.com/uc?id=' + file_id
   df = pd.read_csv(dwn_url, encoding = 'utf8', sep = sep)

   return df
