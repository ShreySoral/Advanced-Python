import requests
r=requests.post("https://httpbin.org/post?a=b",data={'shrey':'value'})
print(r.text)