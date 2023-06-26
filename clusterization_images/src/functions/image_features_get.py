
# получает тензор изображения с помощью clip-model
# возвращает обект типа tensor()

# image - вектор изображения формата PIL
def image_features_get(image):
    inputs = processor(images=image, return_tensors="pt")
    image_features = model.get_image_features(**inputs)

    return image_features.detach()
