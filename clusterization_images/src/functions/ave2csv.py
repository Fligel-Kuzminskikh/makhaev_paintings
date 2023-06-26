
# сохраняем в файл результаты
def save2csv(df, param='data'):
    file_name = 'out/' + param + '_' + str(randint(100, 2000)) +'.csv'
    df.to_csv(file_name, index= False )
