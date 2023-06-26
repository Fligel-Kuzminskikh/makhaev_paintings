# соединяет таблицу изображений и таблицу сюжетов по ключевому полю

# df_plot - датафрейм с сюжетами, df_img - датафрейм с изображениями
# loc_key = '' - название столбца по которому соединяются таблицы (если не указан - 'regNumber')
def setPlotImg(df_plot, df_img, loc_key = ''):
  key = loc_key if loc_key else global_key
  key_plot_list = np.unique(df_plot[key].tolist())
  df_temp = df_img.loc[df_img[key].isin(key_plot_list)]
 
  return df_plot.merge(df_temp, on=key)
