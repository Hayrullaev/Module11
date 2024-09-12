
def introspection_info(obj):

    obj_type = type(obj).__name__
    # Определение типа объекта
    # Получение атрибутов объекта
    attributes = dir(obj)

    # Получение методов объекта
    methodos = [method for method in attributes if callable(getattr(obj, method))]


    # Определение модуля, к которому объект принадлежит
    module = obj.__class__.__module__

    # Создание словаря с информацией об объекте
    info = {'type': obj_type, 'attributes': attributes,'methods': methodos, 'module': module}

    return info


# Интроспекция числа
number_info = introspection_info(42)
print(number_info)


# Интроспекция строки
string_info = introspection_info('Hello')
print(string_info)

# Интроспекция списка
list_info = introspection_info([1, 20, 4.0, 'word'])
print(list_info)