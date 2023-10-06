from sklearn.preprocessing import OneHotEncoder

# Создаем объект OneHotEncoder
encoder = OneHotEncoder(handle_unknown='ignore')

# Преобразуем столбец DataFrame в массив numpy
column = data['whoAmI'].values.reshape(-1, 1)

# Применяем метод fit_transform объекта OneHotEncoder к массиву numpy
one_hot = encoder.fit_transform(column).toarray()

# Создаем новый DataFrame из полученных one hot значений и указываем названия столбцов
one_hot_df = pd.DataFrame(one_hot, columns=encoder.get_feature_names(['whoAmI']))

# Выводим результат
one_hot_df.head()