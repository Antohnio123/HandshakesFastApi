import re


s = '.../sfgdfgdfg'
match = re.match(r'^(\.)+/', s)


page = 'http://google.com/users/common/native/drug/'

url='..../contacts/career/jobs'
dots = len(re.findall('\.', url.split('/')[0]))
root = '/'.join(page.split('/')[:dots:])
url='/'.join([root,'/'.join(url.split('/')[1:])])
if match:
    print('Вхождение засечено, количество точек = '+ str(hight))
    print(root)
    print (url)
else:
    print('Вхождения НЕТ!')