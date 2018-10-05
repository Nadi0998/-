# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.a = []
        for item in items:
            if len(kwargs) > 0:
                if kwargs['ignore_case']:
                    item = item.lower()
            if item not in self.a:
                self.a.append(item)

        #a = list(list(filter(x not in a, items))[0] for x in items)


    def __next__(self):
        # Нужно реализовать __next__
        if self.n < len(self.a):
            result = self.a[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        self.n = 0
        return self
