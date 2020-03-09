# Проверка ссылок на странице должна предполгать первоначальную обработку этих ссылок.
# Надо обработать некоторые абсолютные ссылки, которые укзаны без http: (есть на сайте ya.ru)
# И обработать относительные ссылки:  отправляющие в корень, с текущей страницы, с подъёмом на N папок, и якоря


from urllib import request, error
import re


# Метод проверки ссылок на работоспособность
def urlcheck (url, page):
    if url != '':
# Проверяем ссылку на абсолютность
        if url[0:7] == 'http://':
            pass
        elif url[0:2] == '//':
            url = ''.join(['http:', url])
        else:
# Обрабатываем относительную ссылку (внутри сайта)
            matchobj = re.match(r'^(\.)*/', url)                    # проверяем ссылку на относительность и вхождение точек в начале
            if matchobj:
                dots = len(re.findall('\.', url.split('/')[0]))     # определяем количество точек в начале
                if dots == 0:
                    root = '/'.join(page.split('/')[0:3])
                    url=''.join([root,url])
                else:
                    root='/'.join(page.split('/')[:dots:])
                    url = '/'.join([root, '/'.join(url.split('/')[1:])])
            elif url[0] == '#':                                         # Проверяем якорь
                url='/'.join([page, url])
# А теперь тестим работоспособность ссылки библиотекой urllib
        try:
            req = request.Request(str(url))
            req=req.get_full_url()
            request.urlopen(req)
            print(' The URl = ' + req +' is working properly')
            return True
        except (error.URLError, ValueError) as e:
            print(' The URl = ' + url +' has a problem')
            return False
            pass
    else:
        pass


# Метод поиска ссылок на странице.  Он же и проверяет ссылки, используя метод urlcheck
def linkcheck(web_site):
    n=1
    req = request.Request(web_site)
    response = request.urlopen(req)
    web_page = str(response.read())
    print(web_page)
    # В коде страницы ссылки начинаются с набора символов  href="
    b = 0
    try:
        while web_page:
            Ind1 = web_page[b:].index('href=')
            Ind2 = web_page[(b+Ind1+6):].index('"')
            link = web_page[(b+Ind1+6):(b+Ind1+6+Ind2)]
            b += Ind1+Ind2 + 7
            print (str(n) + ' Checking the link ' +  link)
            n+=1
            urlcheck(link, web_site)
    except ValueError:
        pass

# target = 'http://google.com'
# target = 'http://ya.ru'
target = 'https://vozmu.ru/strany'
linkcheck(target)