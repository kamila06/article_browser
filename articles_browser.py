import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser

response = requests.get('https://mataja.pl/')
html = response.text

soup = BeautifulSoup(html, 'html.parser')

content_div = soup.find(class_ = 'grids classic-layout entries')

titles_and_links = {}
for element in content_div.find_all('article'):
    article_title = element.h2.a.string
    article_link = element.figure.a.get('href')
    titles_and_links[article_title] = article_link

def callback(url):
    webbrowser.open_new(url)
    pass

window = Tk()
for t, l in titles_and_links.items():
    link = Label(window, text = t, fg="blue", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", lambda e, url=l:callback(url))

window.mainloop()