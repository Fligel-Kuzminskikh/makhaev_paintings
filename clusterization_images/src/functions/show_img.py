
# вывод изображений

# image_list - список словарей вида {'img':вектор изображения в формате PIL или CV2,'title':название}
# name - булиан - выводить или нет заголовок изображения
# col - количество колонок 
# cv2_img - булиан - передается картинка в формате CV2
# suptitle - общий заголовок
def show_img(image_list, name = True, col = 5, cv2_img = False, suptitle='', title_key = global_key):
    row = len(image_list) // col + 1

    plt.figure(figsize=(6.4, 2.4*row))
    for i in range(0,len(image_list)):
        plt.subplot(row, col, i + 1)
        plt.suptitle(suptitle)
        plt.axis('off')
        if name:
           title = str(image_list[i][title_key])
        else:
           title =  'N' + str(i+1) 
        plt.title(f"{title}") 
        if cv2_img:
           plt.imshow(cv2.cvtColor(image_list[i]['img'], cv2.COLOR_BGR2RGB))
        else:
           plt.imshow(image_list[i]['img'])
