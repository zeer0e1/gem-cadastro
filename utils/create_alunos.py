import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 50

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from aluno.models import Instrumento, Aluno, Localidade

    Aluno.objects.all().delete()
    Instrumento.objects.all().delete()
    Localidade.objects.all().delete()

    fake = faker.Faker('pt_BR')
    instrumentos = ['Violino', 'Violoncelo', 'Trombone',
                    'Clarinete', 'Sax Tenor', 'Sax Reto', 'Trombone']
    localidades = ['Jardim Cardoso', 'Vitória Régia','Itavuvu','Santa Lucia']
    estados_civis = ['Casado', 'Solteiro']
    operadoras = ['Vivo', 'Claro', 'Tim']

    django_categories = [Instrumento(nome=nome) for nome in instrumentos]
    django_categories2 = [Localidade(localidade=localidade)
                          for localidade in localidades]

    for category in django_categories:
        category.save()

    for category2 in django_categories2:
        category2.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        nome_completo = profile['name']
        localidade = choice(django_categories2)
        estado_civil = choice(estados_civis)
        telefone = fake.phone_number()
        operadora = choice(operadoras)
        date_nascimento: datetime = fake.date_this_year()
        inicio_gem: datetime = fake.date_this_year()
        instrumento = choice(django_categories)

        django_contacts.append(
            Aluno(
                nome_completo=nome_completo,
                localidade=localidade,
                estado_civil=estado_civil,
                telefone=telefone,
                operadora=operadora,
                date_nascimento=date_nascimento,
                inicio_gem=inicio_gem,
                instrumento=instrumento
            )
        )

    if len(django_contacts) > 0:
        Aluno.objects.bulk_create(django_contacts)
