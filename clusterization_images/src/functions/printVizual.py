
# выводит на печать картинки из переданного списка, согласно кластаризации
# или печатает только один класс, если есть ключ кластера

# img_df - дата фрейм с колонками 'img' - типа PIC/CV, 'title' - имя картинки = ссылка на картинку в выгрузке 
# labels - список лейблов
# key - ключ кластера
# printOneClaster = False, - печатаем все или только выбранный кластер
# sampel_size = 30, suptitle = '', cv2_img = False, name = False - параметры печати
def printVizual(img_df, labels, key=False, printOneClaster = False, sampel_size = 30, suptitle = '', cv2_img = False, name = False):
    df_temp = pd.DataFrame({'img': img_df['img'], 'title': img_df['title'], 'labels':labels})
    if printOneClaster:
       print_claster(df_temp, key, sampel_size = sampel_size, suptitle = suptitle, cv2_img = cv2_img, name =name)
    else:
       print_img_in_classters(df_temp, sampel_size = sampel_size, suptitle = suptitle, cv2_img = cv2_img, name =name)
