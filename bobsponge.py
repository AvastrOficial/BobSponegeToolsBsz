import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

Bl = '\033[30m'  # VARIABLE BUAT WARNA CUYY
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'
Am = '\033[1;33m'

# utilities

# decorator for attaching run_banner to a function
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)
    return wrapper


@is_option
def phoneGW():
    User_phone = input(f"\n {Wh}Ingresa el número ejemplo: {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}")  # INPUT NUMBER PHONE
    default_region = "ID"  # DEFAULT NEGARA INDONESIA

    parsed_number = phonenumbers.parse(User_phone, default_region)  # VARIABLE PHONENUMBERS
    region_code = phonenumbers.region_code_for_number(parsed_number)
    provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Gr}Extracción de información del número {Wh}==========")
    print(f"\n {Wh}Ubicación             :{Gr} {location}")
    print(f" {Wh}Código de Región      :{Gr} {region_code}")
    print(f" {Wh}Zona Horaria          :{Gr} {timezoneF}")
    print(f" {Wh}Operador              :{Gr} {provider}")
    print(f" {Wh}Número válido         :{Gr} {is_valid_number}")
    print(f" {Wh}Número posible        :{Gr} {is_possible_number}")
    print(f" {Wh}Formato Internacional :{Gr} {formatted_number}")
    print(f" {Wh}Formato Móvil         :{Gr} {formatted_number_for_mobile}")
    print(f" {Wh}Número original       :{Gr} {parsed_number.national_number}")
    print(f" {Wh}Formato E.164         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Código de País        :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Número Local          :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Tipo                  :{Gr} Este es un número móvil")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Tipo                  :{Gr} Este es un número fijo")
    else:
        print(f" {Wh}Tipo                  :{Gr} Este es otro tipo de número")


@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}Ingresa el nick : {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "YouTube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}Usuario no identificado{Ye}!")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n {Wh}========== {Gr}MOSTRAR INFORMACIÓN NOMBRE DE USUARIO {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}")


# OPTIONS
options = [
    {
        'num': 1,
        'text': 'Informacion con numero',
        'func': phoneGW
    },
    {
        'num': 2,
        'text': 'Informacion con nick',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': 'Salir',
        'func': exit
    }
]


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Presiona enter para continuar')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Salir')
        time.sleep(2)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():
    # BANNER TOOLS
    clear()
    stderr.writelines(f"""
    {Am}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⠛⠛⠲⠦⣤⣤⣴⠶⠛⣋⣉⠉⠉⠛⠶⠶⢤⡤⠶⠚⠛⠉⠉⣁⣍⡙⠓⠶⣤⣤⣤⣤⣵⠶⠶⠶⢶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⢀⣴⣶⡄⠀⠀⠀⠈⣉⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠋⡍⠙⠇⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠈⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣠⡄⠘⠛⠋⠀⠀⠀⣀⣼⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠻⢿⠃⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠋⠀⠀⠀⠀⣀⣤⣾⣟⣉⠉⠙⠓⢦⣀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠟⠛⢷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⡶⠶⣶⣶⣿⣿⣿⢿⣿⣿⣿⣶⣄⠀⠙⢶⡀⠀⠀⠀⢠⡴⠋⢁⣤⣶⣶⣿⣿⣿⣿⣷⣶⡶⢶⣶⡶⠞⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⢀⣾⣿⣿⣹⣷⣾⣿⣷⣿⣏⢹⣿⣷⡄⠀⢻⡄⠀⣴⠋⢀⣴⣿⡿⢋⣽⣷⣿⣯⣭⡿⢻⣿⣦⠀⠙⢦⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡇⢀⣿⡿⣠⣾⣿⣿⣿⣿⠃⠀⠀⢹⣯⣻⣿⡄⠀⣿⣰⠃⢰⣿⡏⣻⣾⣿⣿⣿⣿⠋⠉⠙⣿⡙⣿⣷⡀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣾⣿⠁⣿⣿⣿⣿⣿⣿⣷⣤⣴⣿⣿⡿⢿⣿⠀⢸⡏⠀⣿⣿⢀⣿⣿⣿⣿⣿⣿⣄⣀⣠⣿⣿⠛⣿⡇⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣿⡟⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⣿⠀⢸⡇⠀⣿⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡇⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠹⣿⣟⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣸⣿⠃⢀⣿⡇⠀⢻⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣾⣿⠃⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣇⠀⡽⣿⣷⡏⢻⣿⣿⣿⣿⡿⠟⢷⣌⣿⠏⢀⣼⠟⢿⡄⠈⢿⣷⣤⡿⢿⣿⣿⣿⣿⣿⣿⠋⣠⣿⠏⠀⣰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⡀⠈⠻⠿⣦⣾⣅⣀⣩⣤⣶⡿⠟⢁⣰⡟⣻⠀⢸⠻⣄⠀⠙⢿⣶⣄⣹⣟⣋⣉⣿⣬⣷⠿⠃⢀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠳⣤⣀⡀⠈⠉⠉⠉⠉⢁⣠⡴⠟⠋⠀⣿⠀⢸⠀⠘⠷⣤⣀⡈⠉⠛⠛⠛⠛⠛⠋⣀⣠⡴⠟⢡⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠉⠉⠛⠛⠛⠛⠋⡍⠉⠀⠀⠀⠀⣿⠀⢸⠀⠀⠀⠀⠉⠛⠓⠲⠶⠶⠶⠶⠞⠛⠉⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡖⠀⠀⠀⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⢸⣦⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⣿⣿⠀⢸⠿⣄⡀⠀⠀⠀⠀⢀⡞⠉⢻⣆⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠋⣿⠀⢸⠀⠈⢷⡀⠀⠀⢀⡾⠀⠀⠀⢻⡀⢸⡇⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⠀⠀⣴⣶⣤⡄⠀⠀⢀⣼⠃⠀⠀⠀⡟⠀⢸⡇⠀⠈⡇⢠⠀⢸⠁⢀⣠⣄⣸⡇⠈⢀⡾⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⣿⠀⠀⠙⠻⠟⠃⠀⠀⢿⣍⡴⠀⠀⢀⡇⠀⢸⡇⠈⢷⣴⠟⠀⠘⢦⣌⠛⠿⠛⠀⠀⢀⡇⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⡷⠶⠚⠓⠲⠶⠶⢶⣶⠛⠓⠲⢶⣾⡇⠀⢸⣿⡦⢤⡤⠶⣾⡶⠶⣤⣤⣤⠶⣤⣀⣼⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢻⡿⢿⣀⣀⣀⠀⠀⠀⠀⠀⠉⠳⠤⠜⣹⡇⠀⢸⡇⠱⣦⡤⠚⠉⠀⠀⠀⠀⠀⠀⠀⢹⢿⡶⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⡿⣯⣿⣿⣿⣿⠛⣿⣿⣿⣷⣾⣿⠃⠀⠈⣿⣶⣿⣾⡿⠶⣾⣷⣶⣶⣶⣶⢶⣾⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠾⣧⢸⡀⠈⠉⠉⠉⠁⠀⠈⠙⠉⠙⠛⣿⣄⠀⣰⡿⠛⠛⠛⠃⠀⠙⠛⠛⠛⠛⠋⠀⡏⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠸⣷⡤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣬⣭⣿⣯⣀⣀⣀⣀⣀⣤⣠⣤⣄⣤⣤⣄⣰⣧⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢇⠀⣿⠀⢰⣿⣤⣀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⣽⣟⣛⡛⠛⣿⣿⠉⠉⣽⠇⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡌⣇⣿⠀⠀⠈⠉⢹⠛⢻⡋⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⣿⠛⣟⠛⠋⠀⠀⣿⣰⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣹⡟⠀⠀⠀⠀⢸⡇⢾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢶⡏⠀⠀⠀⠀⢻⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠟⠃⠀⠀⠀⠀⢸⣏⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣽⡃⠀⠀⠀⠀⠸⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡅⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⣧⡀⣠⣾⠁⣸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡏⢸⣷⡄⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀      ⣸⣿⣿⣿⣿⣷⣾⣿⣙⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣛⣿⣛⣛⣛⣙⣛⣛⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣻⣿⣿⣛⣻⣿⣿⣿⣛⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀

           {Wh}[ + ]  TOOLS - BOBSPONGE - OSINT - BSZ  [ + ]
           
    """)
    print(option_text())
    try:
        opt = int(input(f'{Wh}[ {Gr}+ {Wh}] {Wh}Ingresa una opción: '))
        execute_option(opt)
    except ValueError:
        print(f'{Re}[ ! ] Solo números permitidos !')
        time.sleep(2)
        option()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Salir')
        time.sleep(2)
        exit()


def run_banner():
    clear()
    print(f"""
{Gr}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣳⣄⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡤⡴⠁⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣯⣷⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⡀⠀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠏⠀⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⢿⡿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢁⣬⣉⣉⣙⣻⣶⠀⠀⠀⠀⠀⢠⣤⣤⣄⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⠈⣿⠃⠀⠀⢻⣿⣿⣿⠟⣿⢷⡆⠀⢀⣴⣶⣦⣤⣄⡀⠀⠳⠄⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀
⠀⠀⢻⣿⣿⣿⣿⣿⣿⣏⠀⢿⠀⠀⠀⠀⠉⠛⠛⠁⢀⣾⠁⠀⢸⡍⠙⣉⢿⣿⣿⡷⠂⠀⠀⠸⣿⣿⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣄⣸⠀⠀⠀⠀⠀⠀⢀⡴⠈⠁⠀⠀⠘⣟⠂⠈⠉⠉⠉⠀⠀⠀⠀⢀⣾⠋⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣦⣀⠀⣀⠀⠀⠹⢧⣤⣀⡀⣀⣀⡈⡷⢤⡀⠀⠀⠀⠀⠀⡧⣼⠃⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟
⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣋⡀⠘⠿⣤⣄⣀⣀⣀⡉⠉⠉⠉⠉⠁⠀⠳⠀⠀⠀⢀⡔⠁⣿⣀⣀⣾⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣷⣷⡀⠀⠀⠻⣍⠋⠛⠛⠓⠚⠲⢶⣶⣤⡤⣷⠄⢠⠃⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⢍⠓⠲⠤⠤⢶⣶⡿⠋⠀⠀⢠⠏⠀⣴⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠢⠄⠉⠉⠁⠀⠀⠀⠐⠁⢀⣼⣿⣟⡛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠞⣻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⢿⣿⣦⣌⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⢀⠇⢹⠿⣦⣄⣀⣀⡀⣀⣀⣠⡴⢶⠟⠉⠀⠀⠹⣯⣽⣧⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⢸⢀⡿⠒⠚⣿⡟⣻⣿⣿⣸⡁⢀⡎⠀⠀⠀⠀⠀⢻⠁⢻⣏⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠖⠒⠒⢾⣍⣀⣀⣠⣿⡟⠋⠁⠉⠓⠧⣞⣀⣀⠀⠀⠀⠀⢸⠀⠀⣿⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠙⠿⣄⠀⠀⠀⠀⠀⠀⠈⠓⠉⠑⢦⣄⣸⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣯⡏⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⠤⠤⠤⠖⠒⠉⠁⠉⠉⠑⢦⣀⡀⠀⠀⢀⣠⠞⠁⢳⣷⠀⠀⢠⠇⡇⠀⠀⠀
⠀
   {Wh}[ + ]  SACAMOS LA INFO POR TI PERRO [ + ]⠀⠀⠀
""")


def main():
    option()


if __name__ == '__main__':
    main()
