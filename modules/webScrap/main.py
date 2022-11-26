from requests_html import HTMLSession
from bs4 import BeautifulSoup


def webScraping(url: str, parentTag, parentTagClass, childTag, childTagClass, type=None):
    session = HTMLSession()
    page = session.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = []

    if not type:
        for item in soup.findAll(parentTag, attrs={'class': parentTagClass}):
            tag = item.find(childTag, attrs={'class': childTagClass})
            result.append(tag.text)
    elif type == 'image':
        for item in soup.findAll(parentTag, attrs={'class': parentTagClass}):
            tag = item.find('img')
            result.append(tag.get('src'))

    return result


def fill(array: list, qtde: int, fill):
    qtde = qtde - len(array)
    for i in range(qtde):
        array.append(fill)


if __name__ == '__main__':
    url = 'https://www.drogariamoderna.com.br/higiene-e-beleza'
    session = HTMLSession()
    page = session.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for item in soup.findAll('div', attrs={'class': 'vtex-store-components-3-x-productBrandContainer'}):
        print(item)
