from Observable import NewsAgency
from Observer import Newspaper,SMS

if __name__ == '__main__':
    reuters = NewsAgency('Reuters')
    efe = NewsAgency('EFE')


    la_vanguardia = Newspaper("La Vanguardia")
    el_pais = Newspaper("El Pais")
    joan = SMS(626347612)

    reuters.add_observer(la_vanguardia)
    reuters.add_observer(el_pais)
    efe.add_observer(el_pais)
    reuters.add_observer(joan)

    reuters.publish_news('PSOE winner of european elections in Spain')
    efe.publish_news('El partit socialista guanya les eleccions europees')