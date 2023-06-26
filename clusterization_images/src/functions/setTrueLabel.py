
# возвращает метку кластера для переданного изображения

# line - словарь вида {'img': изображение формата PIA/CV2, 'title':путь к файлу, 'regNumber':id по которому матчатся таблицы}
# loc_key = '' - название столбца по которому соединяются таблицы (если не указан - 'regNumber')
def setTrueLabel(line, loc_key = ''):
  key = loc_key if loc_key else global_key
  img_id = int(line[key])
  return valid_table_df.loc[valid_table_df[key] == img_id]['label_true'].tolist()[0]
