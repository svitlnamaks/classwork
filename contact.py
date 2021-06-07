from dataclasses import dataclass, field
import datetime


@dataclass
class Contact:
    name:str=field(compare=False)
    phone_num:str
    city:str=field(compare=False)
    date_of_birth:datetime.date=field(default_factory=lambda :(datetime.datetime.now()-datetime.timedelta(days=18*365)).date(),compare=False)



