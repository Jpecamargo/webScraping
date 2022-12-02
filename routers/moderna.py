from fastapi import APIRouter
import pandas as pd

from controllers.moderna.defaultScrap import defaultScrap
from modules.webScrap.main import pagination

router = APIRouter(
    prefix='/moderna',
    tags=['Drogaria Moderna']
)


@router.get('/higiene-e-beleza')
async def higiene_beleza(limit: int = 15, page: int = 1):
    response = defaultScrap('https://www.drogariamoderna.com.br/higiene-e-beleza', 'Higiene e Beleza')
    data = pagination(response, limit, page)

    return data


@router.get('/medicamentos')
async def medicamentos(limit: int = 15, page: int = 1):
    response = defaultScrap('https://www.drogariamoderna.com.br/medicamentos-de-a-z', 'Medicamentos')
    data = pagination(response, limit, page)

    return data


@router.get('/amamentacao')
async def amamentacao(limit: int = 15, page: int = 1):
    response = defaultScrap('https://www.drogariamoderna.com.br/amamentacao', 'Amamentação')
    data = pagination(response, limit, page)

    return data


@router.get('/genericos')
async def genericos(limit: int = 15, page: int = 1):
    response = defaultScrap('https://www.drogariamoderna.com.br/genericos', 'Genéricos')
    data = pagination(response, limit, page)

    return data


@router.get('/dermocosmeticos')
async def dermocosmeticos(limit: int = 15, page: int = 1):
    response = defaultScrap('https://www.drogariamoderna.com.br/dermocosmeticos', 'Dermocosméticos')
    data = pagination(response, limit, page)

    return data


@router.get('/conveniencia')
async def conveniencia(limit: int = 15, page: int = 1):
    response = defaultScrap('https://www.drogariamoderna.com.br/conveniencia', 'Conveniência')
    data = pagination(response, limit, page)

    return data


@router.get('/diu')
async def diu(limit: int = 15, page: int = 1):
    response = defaultScrap('https://www.drogariamoderna.com.br/diu', 'Diu')
    data = pagination(response, limit, page)

    return data


@router.get('/cuidados-especiais')
async def cuidados_especiais(limit: int = 15, page: int = 1):
    response = defaultScrap('https://www.drogariamoderna.com.br/cuidados-especiais', 'Cuidados Especiais')
    data = pagination(response, limit, page)

    return data
