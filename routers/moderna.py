from fastapi import APIRouter
import pandas as pd

from controllers.moderna.defaultScrap import defaultScrap

router = APIRouter(
    prefix='/moderna',
    tags=['Drogaria Moderna']
)


@router.get('/higiene-e-beleza')
async def higiene_beleza():
    data = defaultScrap('https://www.drogariamoderna.com.br/higiene-e-beleza', 'Higiene e Beleza')
    return data


@router.get('/medicamentos')
async def medicamentos():
    data = defaultScrap('https://www.drogariamoderna.com.br/medicamentos-de-a-z', 'Medicamentos')
    return data


@router.get('/amamentacao')
async def amamentacao():
    data = defaultScrap('https://www.drogariamoderna.com.br/amamentacao', 'Amamentação')
    return data


@router.get('/genericos')
async def genericos():
    data = defaultScrap('https://www.drogariamoderna.com.br/genericos', 'Genéricos')
    return data


@router.get('/dermocosmeticos')
async def dermocosmeticos():
    data = defaultScrap('https://www.drogariamoderna.com.br/dermocosmeticos', 'Dermocosméticos')
    return data


@router.get('/conveniencia')
async def conveniencia():
    data = defaultScrap('https://www.drogariamoderna.com.br/conveniencia', 'Conveniência')
    return data


@router.get('/diu')
async def diu():
    data = defaultScrap('https://www.drogariamoderna.com.br/diu', 'Diu')
    return data


@router.get('/cuidados-especiais')
async def cuidados_especiais():
    data = defaultScrap('https://www.drogariamoderna.com.br/cuidados-especiais', 'Cuidados Especiais')
    return data
