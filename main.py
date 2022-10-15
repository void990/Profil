"Сделано для канала: https://t.me/WhiteTermux, над кодом не старался :)"

import rich
import os, sys
import random
import string
import banner

from faker import Faker
from faker.providers import internet
from rich.console import Console
from rich.prompt import Prompt

console = Console()

lang = Prompt.ask(
'[bold white][+][/] [bold red]choose language[/]',
choices=['ru', 'en']
)


if lang == "ru":
   lang_code = "ru_RU"

elif lang == "en":
     lang_code = "en_US"

else:
     lang_code = "ru_RU"


fake = Faker(lang_code)


def Faker_Functions():

    name = fake.name()
    address = fake.address()
    date_time = fake.date_time()
    ipv4 = fake.ipv4()
    ipv6 = fake.ipv6()
    mac_address = fake.mac_address()
    user_agent = fake.user_agent()
    company = fake.company()
    company_email = fake.company_email()
    url = fake.url()
    
     
    #email - Генерация почт в самой библе говно как и сам весь этоь код))

    email = "".join(random.sample(string.ascii_letters, k = 10))

    domens = [
        "@gmail.com",
        "@yahoo.com",
        "@mail.ru",
        "@yandex.ru",
    ]

    domens = random.choice(domens)


    console.rule('DATA')
    console.print(f'''
    [bold red][:][/] Name[red]:[/] {name}
    [bold red][:][/] Address[red]:[/] {address}
    [bold red][:][/] Data Time[red]:[/] {date_time}
    [bold red][:][/] Email[red]:[/] {email}{domens}
    [bold red][:][/] IPV4[red]:[/] {ipv4}
    [bold red][:][/] IPV6[red]:[/] {ipv6}
    [bold red][:][/] User Agent[red]:[/] {user_agent}
    [bold red][:][/] Mac Address[red]:[/] {mac_address}
    [bold red][:][/] Compamy[red]:[/] {company}
    [bold red][:][/] URL Company[red]:[/] {url}
    [bold red][:][/] Email Company[red]:[/] {company_email}
    ''')
    console.rule('[bold white]https://t.me/WhiteTermux')
    
Faker_Functions()    
    
    


