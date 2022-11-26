import pandas as pd
from modules.webScrap.main import webScraping, fill


def defaultScrap(url, category):
    name = webScraping(
        url,
        'h3',
        'vtex-product-summary-2-x-productNameContainer mv0 vtex-product-summary-2-x-nameWrapper overflow-hidden c-on-base f5',
        'span',
        'vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body'
    )

    price = webScraping(
        url,
        'span',
        'vtex-product-price-1-x-sellingPriceValue vtex-product-price-1-x-sellingPriceValue--summary',
        'span',
        'vtex-product-price-1-x-currencyContainer vtex-product-price-1-x-currencyContainer--summary'
    )

    image = webScraping(
        url,
        'div',
        'dib relative vtex-product-summary-2-x-imageContainer vtex-product-summary-2-x-imageStackContainer vtex-product-summary-2-x-hoverEffect',
        'img',
        None,
        'image'
    )

    qtde = len(name)
    fill(price, qtde, 'Indisponnível')

    df = pd.DataFrame({'Product': name, 'Price': price, 'Image': image, 'Category': category})
    data = df.to_dict('records')
    return data
