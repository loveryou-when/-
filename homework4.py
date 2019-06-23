import requests
urls=[]
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML= response.text
print(HTML)

response = requests.get(url,timeout=1)
if response != 200:
    print(' 爬取失败'%url)

urls =HTML.split('\n')
for url in urls:
    name=url.split('/')[-1]
    response = requests.get(url)
    content = response.content
    with open(name,'wb')as f:
        f.write(content)
    break

