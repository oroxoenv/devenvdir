# import time

# from icecream import ic
from dataclasses import dataclass


@dataclass
class Header:
    number_address                      : int = 133
    state_city                          : str = 'SP'
    city_state_cpf                      : str = 'Leme'
    district_address                    : str = 'Centro'
    cep                                 : str = '13610-125'
    landline_number                     : str = '(19)3573-6300'
    url                                 : str = 'www.leme.sp.gov.br'
    email_educational                   : str = 'educacao@leme.sp.gov.br'
    address                             : str = 'Av. Maria Augusta Thomaz'
    municipal_educational_institution   : str = 'SECRETARIA MUNICIPAL DE EDUCAÇÃO'



@dataclass
class Student:
    name            : str
    birthdate       : str
    school_grade    : str



@dataclass
class BeginBody:
    content   : str
    title     : str = 'RELATÓRIO DO DESENVOLVIMENTO INDIVIDUAL DO ALUNO - INICIAL'



@dataclass
class MiddleBody:
    content   : str
    title     : str = 'RELATÓRIO DO DESENVOLVIMENTO INDIVIDUAL DO ALUNO - PERCURSO'



@dataclass
class EndBody:
    content   : str
    title     : str = 'RELATÓRIO DO DESENVOLVIMENTO INDIVIDUAL DO ALUNO - FINAL'



