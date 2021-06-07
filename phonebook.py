from contact import Contact


class PhoneBook:
    def __init__(self, file_name: str):
        self.__sd = StoreData(file_name)
        self.__data = self.__sd.load()
        self.__fn = ''
        self.__fd = ''

    def add_contact(self, contact: Contact):
        if contact not in self.__data:
            self.__data.append(contact)
            self.__sd.store(self.__data)

    @property
    def filter(self):
        return self.__fn, self.__fd

    @filter.setter
    def filter(self, new_val):
        try:
            if new_val[0]=='' :
                self.__fn, self.__fd = '',''
                return None

            if new_val[0] in Contact.__annotations__ and type(new_val[1]) is str:
                self.__fn, self.__fd = new_val
            else:
                raise ValueError
        except:
            raise ValueError('first:name, second:value')

    def set_filter(self,*args,**kwargs):
        for filed_name in kwargs:
            self.filter =(filed_name,kwargs[filed_name])
            break
        else:
            self.filter=('','')

    def __iter__(self):
        self.__tmp: list[Contact]
        self.__idx = -1
        if self.__fn == '':
            self.__tmp = self.__data
        else:
            self.__tmp = []
            for contact in self.__data:
                val = getattr(contact, self.__fn)
                if str(val).find(self.__fd) != -1:
                    self.__tmp.append(contact)

        return self

    def __next__(self):
        self.__idx += 1
        if self.__idx < len(self.__tmp):
            return self.__tmp[self.__idx]
        raise StopIteration


class StoreData:
    def __init__(self, file_name: str = 'data.json'):
        self.__name = file_name

    def load(self) -> list[Contact]:
        return []

    def store(self, data: list[Contact]):
        pass
