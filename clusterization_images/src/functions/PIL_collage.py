
from PIL import ImageFilter, ImageDraw, ImageFont

# размеры картинок-миниатюр для вывода 
GLOBAL_thumb_size = (128, 128)
# положение картинки на миниатюре, если она не вписывается в квадрат 
GLOBAL_resize_type = 'center'

# количество картинок в ряду коллажа
GLOBAL_сollage_cols = 5
# фон картинок если не вписываются в превью, если не задан в качестве фона используем размытое изображени
GLOBAL_bg_color = (232, 232, 232, 0)

# путь к шрифту, используемому при добавлении надписи на изображение
GLOBAL_font_family = "./src/DinCyRg_.ttf"
# размер шрифта, по умолчанию при добавлении надписи на изображение
GLOBAL_font_size = 30
# цвет шрифта, по умолчанию при добавлении надписи на изображение
GLOBAL_font_color = (9, 9, 9, 255)

def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height, ascent, descent)

def paste_text(
       img_source, img_text, 
       inner_size = (0,0),
       text_position = 'inner', 
       bg_color = GLOBAL_bg_color, 
       font_family = GLOBAL_font_family, 
       font_size=GLOBAL_font_size, 
       fill=GLOBAL_font_color, 
       align = 'left'):    
    
    font = ImageFont.truetype(font_family, font_size)
    text_width, text_height, text_ascent, text_descent = get_text_dimensions(str(img_text), font)
    
    if (text_position == 'inner_top') | (text_position == 'inner_bottom'):
       img = img_source.copy()      
       
       if text_position == 'inner_top':
           y = (img_source.size[1] // 2) - (inner_size[1]//2) - text_height - text_descent
       else:
           y = (img_source.size[1] // 2) + (inner_size[1]//2) + text_height
    
    else:
       # добавляем отсуп под текст          
       adding_size = text_height  + text_descent    
       img = Image.new('RGBA', (img_source.size[0], img_source.size[1] + adding_size), color = bg_color)    
       cord_w = 0               
       cord_h = adding_size if text_position == 'title' else 0           
       img.paste(img_source, box=(cord_w, cord_h))
       y = img_source.size[1] if text_position == 'bottom' else  0                 
    
    x = (img.size[0]-text_width)/2 if align== 'center' else 0    
    position = (x, y)
    
    draw = ImageDraw.Draw(img)    
    #draw.text(position, str(img_text), fill=fill, font=font, align=align)    
    draw.multiline_text(position, str(img_text), fill=fill, font=font, align=align)   
    
    return img

# преведение картинок к заданному размеру для удобства коллажирования

# img - картинка формата PIL
# size = GLOBAL_thumb_size - размер к которому приводим картинки
# bg_color = GLOBAL_bg_color - цвет фона блока если изображение не вписываются в превью, если не задан в качестве фона используем размытое изображени
def resize_img(
    img_source, 
    size = GLOBAL_thumb_size, 
    resize_type = GLOBAL_resize_type, 
    bg_color = GLOBAL_bg_color, 
    border = 0,
    img_text_list = []
    ):  
    
    img = img_source.copy()
    thumbnail_size = (size[0] - 2*border, size[1] - 2*border)
    
    img.thumbnail(thumbnail_size)    
    current_size = img.size
    # если картинка не вписывается в квадрат, создаем фон из размытого изображения / или заданного цвета
    if (current_size[0] < thumbnail_size[0]) | (current_size[1] < thumbnail_size[1]):
       if bg_color:
          new_img = Image.new('RGBA', size, color = bg_color)
       else:
          new_img = img.filter(filter=ImageFilter.GaussianBlur)              
          new_img = new_img.resize(thumbnail_size)  
       
       if resize_type == 'center': #вставляем по центру квадрата
          cord_w = (size[0]//2) - current_size[0]//2
          cord_h = (size[1]//2) - current_size[1]//2  
       else:
          cord_w = (size[0]//2) - current_size[0]//2
          cord_h = border
       new_img.paste(img, box=(cord_w, cord_h))    
    
       # если есть текст - вставляем
       if len(img_text_list) != 0:
          for row in img_text_list:
              img_text = row['text']
              font_size  = row['font_size']
              text_align  = row['text_align']
              text_position = row['text_position']
                
              new_img = paste_text(new_img, img_text, inner_size = current_size, text_position = text_position, font_size=font_size, align = text_align)
       return new_img

    return img

# находим суммарную/максимальную высоту всех картинок в листе
def get_total_h(img_list, return_max = False):    
    rezult_list = []
    for img in img_list:
        rezult_list.append(img.size[1])
    if return_max:
        rezult = max(rezult_list)
    else:
        rezult = sum(rezult_list)
    return rezult

# складываем картинки по высоте
def set_full_img(img_list, total_w, bg_color = GLOBAL_bg_color):
    total_h = get_total_h(img_list)
    new_img = Image.new('RGBA', (total_w, total_h), color = bg_color)
    y = 0
    for img in img_list:
        new_img.paste(img, (0, y))
        y += img.size[1]
        
    return new_img

# создание коллажа
def create_collage(img_list, cols = GLOBAL_сollage_cols, size = GLOBAL_thumb_size):
    thumb_width = size[0]
    thumb_height = size[1]
    # если список пустой - создаем пустую картинку заданной ширины
    if len(img_list) == 0:
       width = cols*thumb_width
       height = thumb_height

       new_img = Image.new('RGBA', (width, height))

       return new_img

    # определяем высоту и ширину коллажа    
    # чтобы не подключать math ради одного округления вверх такая странная конструкция
    rows = len(img_list) // cols if (len(img_list) // cols) == (len(img_list) / cols) else (len(img_list) // cols) + 1
    
    width = cols*thumb_width
    height = rows*thumb_height
    
    new_img = Image.new('RGBA', (width, height))
        
    i, x, y = 0, 0, 0
    for row in range(rows):        
            if i == len(img_list):
              break
            for col in range(cols):
                if i == len(img_list):
                  break                    
                new_img.paste(img_list[i], (x, y))
                i += 1
                x += thumb_width
            y += thumb_height
            x = 0

    return new_img

# конвертируем для коллажа cv2 в PIL
def cv2PIL(opencv_image):
    color_coverted = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)  
    return Image.fromarray(color_coverted)

# уменьшаем и выводим
def makeCollage(list_img_to_collage, cols = GLOBAL_сollage_cols, cv2_img = False):
    if cv2_img:
       list_img_to_collage = to_pool(list_img_to_collage, eval('cv2PIL'))
    images_small = to_pool(list_img_to_collage, eval('resize_img'))
    images_collage = create_collage(images_small, cols = cols)
    
    return images_collage

# уменьшаем и выводим с заданными параметрами
def makeCollage_size(list_img_to_collage, cols = GLOBAL_сollage_cols, size = GLOBAL_thumb_size, bg_color = GLOBAL_bg_color, cv2_img = False):
    if cv2_img:
       list_img_to_collage = to_pool(list_img_to_collage, eval('cv2PIL'))
    images_small = [resize_img(item, size = size, bg_color = bg_color) for item in list_img_to_collage]
    images_collage = create_collage(images_small, cols = cols, size = size)
    
    return images_collage

