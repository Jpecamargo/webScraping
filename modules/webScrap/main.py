from requests_html import HTMLSession
from bs4 import BeautifulSoup


def fill(array: list, qtde: int, fill):
    qtde = qtde - len(array)
    for i in range(qtde):
        array.append(fill)


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


def getUrls(baseUrl: str, urlJoin: str, anchor: str, anchorClass: str):
    pages = []
    i = 0

    while True:
        i += 1
        session = HTMLSession()
        url = baseUrl + urlJoin + str(i)
        page = session.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        nextPage = soup.find(anchor, {'class': anchorClass})

        if nextPage is None:
            break

        pages.append(url)

    return pages


def pagination(data, limit: int, page: int):
    startIndex = (limit * page) - limit
    endIndex = (limit * page)
    data = data[startIndex: endIndex]

    return data


if __name__ == '__main__':
    url = 'https://www.drogariamoderna.com.br/cuidados-especiais'
    urlJoin = '?page='
    anchor = 'button'
    anchorClass = 'vtex-button bw1 ba fw5 v-mid relative pa0 lh-solid br2 min-h-small t-action--small bg-action-primary b--action-primary c-on-action-primary hover-bg-action-primary hover-b--action-primary hover-c-on-action-primary pointer'

    pages = getUrls(url, urlJoin, anchor, anchorClass)
    print(pages)
