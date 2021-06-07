from phonebook import PhoneBook
from contact import Contact

if __name__ == '__main__':
    pb1=PhoneBook('contact.json')
    c1=Contact('Anna','3475894607','Tampa',2008)
    pb1.add_contact(c1)
    pb1.add_contact(Contact('Pavlo','3475894608','Lviv'))
    #pb1.set_filter(name='P')
    #pb1.set_filter(date_of_birth='2003')
    for contact in pb1:
        print(contact)