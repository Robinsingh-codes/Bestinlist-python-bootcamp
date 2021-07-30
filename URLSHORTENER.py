import pyshorteners
print(' My project to short the long urls to short ones')
print("KINDLY ENTER THE LONG URL AND BELIEVE ME!")
url=input()
s = pyshorteners.Shortener(api_key='d1225095f00dde0aa4dd9474a6b04cc4933f6cf3')
print('The Bit.ly short url is ', s.bitly.short(url))

print('The short url using TINYURL is ', s.tinyurl.short(url))

print('THANK YOU!  NOW YOU CAN USE SHORT URL WHICH IS EASY TO USE ')
