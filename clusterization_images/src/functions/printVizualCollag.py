
# создает коллаж, согласно кластаризации

# img_df - дата фрейм с колонками 'img' - типа PIC, 'title' - имя картинки = ссылка на картинку в выгрузке 
# labels - список лейблов
# key - ключ кластера
# sampel_size = 30, size = GLOBAL_thumb_size, cols = GLOBAL_сollage_cols, cv2_img = False - параметры печати
def printVizualCollag(img_df, labels, key=0, sampel_size = 30, size = GLOBAL_thumb_size, cols = GLOBAL_сollage_cols, cv2_img = False):
    df_temp = pd.DataFrame({'img': img_df['img'], 'title': img_df['title'], 'labels':labels})
    rezult_list = df_temp[df_temp['labels'] == key]['img'].tolist()
    if len(rezult_list) > sampel_size:
       rezult_list = sample(rezult_list, sampel_size)
    
    return makeCollage_size(rezult_list, size = size, cols = cols, cv2_img = cv2_img)
