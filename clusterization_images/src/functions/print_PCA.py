
# выводит на печать количество дисперсии, объясненной каждой компонентой

# pca - объект pca
def print_PCA(pca):
    for i, component in enumerate(pca.components_):
        print("{} component: {}% объясненной дисперсии".format(i + 1, 
          round(100 * pca.explained_variance_ratio_[i], 2)))
