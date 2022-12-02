import pandas as pd
from modules.webScrap.main import getUrls, webScraping, fill

urlJoin = '?page='
anchor = 'button'
anchorClass = 'vtex-button bw1 ba fw5 v-mid relative pa0 lh-solid br2 min-h-small t-action--small bg-action-primary b--action-primary c-on-action-primary hover-bg-action-primary hover-b--action-primary hover-c-on-action-primary pointer'


def scrap(url, category):
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


def defaultScrap(url, category):
    urls = getUrls(url, urlJoin, anchor, anchorClass)
    data = []

    for item in urls:
        response = scrap(item, category)
        data = data + response

    return data
