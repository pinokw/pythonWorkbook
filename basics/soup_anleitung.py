import bs4 as bs4

html=request("Webseite")
soup=bs4(html_file, "html.parser")

match_title=soup.title.text
match_div=soup.div # erstes div
match_div2=soup.div(class="Sonst") # DIV mit der classe SONST

# Durchsuchen
for article in soup.find_all('div', class_='article'):
    headline=article.p.text # das was in p steht

for link in soup.find_all('a', href=True):  # alle Links finden
    print (link['href'])