# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.items = list(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.my_list = list()
        self.i = 0
        #sum(1 for _ in items)
        self.len_items = len(self.items)




    def __next__(self):
        # Нужно реализовать __next__
        if self.i < self.len_items:
            if self.items[self.i] not in self.my_list:
                self.my_list.append(self.items[self.i])
                return self.items[self.i]
            if self.ignore_case == True:
                if ord(self.items[self.i]) >= 65 or ord(self.items[self.i]) <= 91:
                    self.my_list.append(chr(ord(self.items[self.i])+32))
                if ord(self.items[self.i]) >= 97 or ord(self.items[self.i]) <= 122:
                    self.my_list.append(chr(ord(self.items[self.i])-32))
            self.i += 1
            return self.__next__()
        else:
            raise StopIteration()



    def __iter__(self):
        return self
