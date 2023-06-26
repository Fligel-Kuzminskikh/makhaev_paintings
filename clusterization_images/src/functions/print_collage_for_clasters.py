
# словарь для расшифровки уровней опосредованностей
GLOBAL_tree_dict = {
    0:'Не имеет отношение к Махаеву',
    1:'Авторский оригинал',
    2:'По оригиналу Махаева',
    3:'По гравюре с оригинала',
    4:'Массовая продукция',
    5:'Копия копии'
}

# печатаем только по сюжетам
# df - датафрейм результатов для печати вида:
#     колонка id, связывающая с пулом изображений (по умолчанию 'regNumber'),
#     поле с номером сюжета (по умолчанию 'labels'), 
# img_df = data_img - дата изображений для визуализации
# thumb_size=GLOBAL_thumb_size - размер миниатюр каждого изображения в итоговом коллаже
# cols = GLOBAL_сollage_cols - количество колонок в коллаже
# col_key = 'labels' - id поля с номером сюжета
def print_labels(df, 
                 img_df = data_img, 
                 thumb_size=GLOBAL_thumb_size,                            
                 cols = GLOBAL_сollage_cols,
                 col_key = 'labels'
                 ):
    labels_list = np.unique(df[col_key])

    full_img_w = thumb_size[0]*cols

    collage_list = []

    for i in labels_list:
        plot_title = 'Сюжет №' + str(i)
        collage_list_plot = []
        
        # берем все id сюжета = i
        key_list = df[(df[col_key] == i)][global_key].tolist()
        if len(key_list) == 0:
           continue        

        img_list_temp = img_df[img_df[global_key].isin(key_list)].copy().to_dict(orient='records')        
        
        for item in img_list_temp:
            text_list = [{'text': item[global_key], 'font_size': 12,'text_align': 'center','text_position':'inner_bottom'}]
            if printTrueConnect:
                    connect_key = df[df[global_key] == item[global_key]][col_connect].tolist()[0]                    
                    true_connect = GLOBAL_tree_dict[connect_key]
                    
                    text_list.append({'text': true_connect,'font_size': 12,'text_align': 'center','text_position':'inner_top'})
            img = resize_img(item['img'], size = thumb_size, border = 24, img_text_list = text_list)
            collage_list_plot.append(img)  
            
        max_img_h = max(thumb_size[1], get_total_h(collage_list_plot, return_max = True))        
        plot_img =  create_collage(collage_list_plot, cols = cols, size = (thumb_size[0], max_img_h))
        plot_img = paste_text(plot_img, plot_title, text_position = 'title')
        collage_list.append(plot_img)

    full_img = set_full_img(collage_list, full_img_w) 
    return full_img

# печатаем по классам + уровням опосредованности
# df - датафрейм результатов для печати вида:
#      колонка id, связывающая с пулом изображений (по умолчанию 'regNumber'),
#      поле с номером сюжета (по умолчанию 'labels'),
#      колонка с номером предсказанного уровня опосредовательности (по умолчанию 'class_predict')
#      при необходимости печати реального уровня колонка с номером реального уровня опосредовательности (по умолчанию 'connectedness')
# img_df = data_img - дата изображений для визуализации
# thumb_size=GLOBAL_thumb_size - размер миниатюр каждого изображения в итоговом коллаже
# cols = GLOBAL_сollage_cols - количество колонок в коллаже
# col_key = 'class_predict'- id поля с номером уровня
# col_plot = 'labels' - id поля с номером сюжета
# printTrueConnect = False, - дополнять изображение реальным уровнем опосредовательности
# col_connect = 'connectedness' - id поля с номером реального уровня опосредовательности 
def print_labels_classif(df, 
                          img_df = data_img, 
                          thumb_size=GLOBAL_thumb_size,                            
                          cols = GLOBAL_сollage_cols,
                          col_key = 'class_predict',
                          col_plot = 'labels',
                          printTrueConnect = False,
                          col_connect = 'connectedness'
                         ):
    labels_list = np.unique(df[col_plot])
    level_list = np.unique(df[col_key])

    full_img_w = thumb_size[0]*cols

    collage_list = []

    for i in labels_list:
        plot_title = 'Сюжет №' + str(i)
        collage_list_plot = []

        for j in level_list:        
            level_title = GLOBAL_tree_dict[j]

            # берем все id сюжета = i и уровня опосредовательности = j
            key_list = df[(df[col_plot] == i) & (df[col_key] == j)][global_key].tolist()
            if len(key_list) == 0:
                continue        

            img_list_temp = img_df[img_df[global_key].isin(key_list)].copy().to_dict(orient='records')        
            collage_list_level = []
            for item in img_list_temp:  
                text_list = [{'text': item[global_key], 'font_size': 12,'text_align': 'center','text_position':'inner_bottom'}]
                if printTrueConnect:
                    connect_key = df[df[global_key] == item[global_key]][col_connect].tolist()[0]                    
                    true_connect = GLOBAL_tree_dict[connect_key]
                    
                    text_list.append({'text': true_connect,'font_size': 12,'text_align': 'center','text_position':'inner_top'})
                img = resize_img(item['img'], size = thumb_size, border = 24, img_text_list = text_list)                  
                collage_list_level.append(img)  

            max_img_h = max(thumb_size[1], get_total_h(collage_list_level, return_max = True))        
            level_img = create_collage(collage_list_level, cols = cols, size = (thumb_size[0], max_img_h))                
            level_img = paste_text(level_img, level_title, font_size=24, text_position = 'title')

            collage_list_plot.append(level_img)    

        plot_img = set_full_img(collage_list_plot, full_img_w)
        plot_img = paste_text(plot_img, plot_title, text_position = 'title')
        collage_list.append(plot_img)

    full_img = set_full_img(collage_list, full_img_w) 
    return full_img


# создает произвольный коллаж из переданных параметров без разделения по уровням

# df - дата фрейм связанный с img_df ключом
# img_df - дата фрейм с колонками 'img' - типа PIC/CV2, 'title' - имя картинки = ссылка на картинку в выгрузке 
# sampel_size = 300, size = GLOBAL_thumb_size, cols = GLOBAL_сollage_cols, cv2_img = False - параметры печати

def printVizualCollag_univers(df, img_df = data_img, sampel_size = 300, size = GLOBAL_thumb_size, cols = GLOBAL_сollage_cols, cv2_img = False):
    list_temp = df[global_key].tolist()
    rezult_list = img_df[img_df[global_key].isin(list_temp)]['img'].tolist()  
   
    if len(rezult_list) > sampel_size:
       rezult_list = sample(rezult_list, sampel_size)
    
    return makeCollage_size(rezult_list, size = size, cols = cols, cv2_img = cv2_img)
