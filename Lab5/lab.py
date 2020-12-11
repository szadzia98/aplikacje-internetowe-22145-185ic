import requests
from bs4 import BeautifulSoup
import csv
import re

strona = requests.get("https://docs.python.org/3.9/library/msilib.html?highlight=os%20lib#module-msilib")
print("strona = \n", strona.text[0:40])
print(strona.status_code)

post3 = requests.get("https://jsonplaceholder.typicode.com/posts/3")
json_text: dict = post3.json()
print("url = ", post3.url)
print("json_text = ", json_text)
print("history = ", post3.history)
print("title = ", json_text['title'])

html_doc = """<html>
<head>
    <title>Moja pierwsza strona!</title>
</head>
<body>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec posuere elit at malesuada tempor. Donec eget ligula in ante auctor luctus. Phasellus iaculis porttitor gravida. Donec eget sem lorem. Morbi a libero imperdiet, viverra tellus ac, consequat tortor. Suspendisse nibh massa, accumsan non neque a, vestibulum commodo dui.</p>
<p>Phasellus vestibulum ut <br>erat sit amet ullamcorper. Nam at elit feugiat, dapibus ante vitae, ullamcorper dui. Nunc rutrum at nibh tincidunt mattis. In finibus sed ante vel mollis. Donec at semper metus. Aenean quis consectetur risus. Sed suscipit felis sed ex pretium euismod. In fermentum mi a odio porttitor, dapibus aliquet leo accumsan. Suspendisse pretium augue et faucibus euismod. Quisque risus metus, ultricies nec tortor at, efficitur convallis nunc.</p>
<ul>
    <li>Pierwszy punkt</li>
    <li>Drugi punkt</li>
    <li>Trzeci punkt</li>
</ul>
<ol>
    <li>Pierwszy punkt</li>
    <li>Drugi punkt</li>
    <li>Trzeci punkt</li>
</ol>
<table border="3" bgcolor="#ff00ff" class="tabela blog">
    <tr><th>Naglowek 1</th><th>Naglowek 2</th></tr>
    <tr><td>komorka 11</td><td>komorka 12</td></tr>
    <tr><td>komorka 21</td><td>komorka 22</td></tr>
</table>
<a href="http://google.pl">Arcyciekawa strona</a>
</body>
</html>"""

soup = BeautifulSoup(html_doc, "lxml")

first_p = soup.select("p")[0].text
print("First p =\n", first_p)

another_p = soup.select("p")[1].text
print("Another p =\n", another_p)

# title
print("TITLE")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.text)
print(soup.title.contents)
print("\n")

# ul
print("UL")
print(soup.ul.text)
print("\n")


# atrybuty
print("ATRYBUTY")
print(soup.table["border"])
print(soup.table.has_attr("border"))
print(soup.table.has_attr("href"))
print(soup.table.attrs)
print("\n")


# find
print("FIND")
print(soup.find_all("p"))
print(soup.find(border="3"))
print("Find klasy = ", soup.find(class_="tabela"))
print("Select klasy = ", len(soup.select("table.tabela")))
print(soup.find(href=True))
# print("Find src = \n", soup.find(src=False)) # be careful!

print("\n")

# next
print("NEXT")
print(soup.th.next_element)
print(soup.tr.next_sibling)
print(soup.tr.next_sibling.next_sibling)

page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
)
soup = BeautifulSoup(page.content, "html.parser")

# Create all_h1_tags as empty list
all_h1_tags = []

# Set all_h1_tags to all h1 tags of the soup
for element in soup.select("h1"):
    all_h1_tags.append(element.text)

# Create seventh_p_text and set it to 7th p element text of the page
seventh_p_text = soup.select("p")[6].text

print(all_h1_tags, seventh_p_text)

top_items = []

# Extract and store in top_items according to instructions on the left
products = soup.select("div.thumbnail")
print("Liczba top items = ", len(products))
for elem in products:
    title = elem.select("h4 > a.title")[0].text
    review_label = elem.select("div.ratings")[0].text
    info = {"title": title.strip(), "review": review_label.strip()}
    top_items.append(info)

print(top_items)

image_data = []

# Extract and store in top_items according to instructions on the left
images = soup.select("img")
print("Liczba obrazków =", len(images))
for image in images:
    # print(type(image))
    src = image.get("src")
    alt = image.get("alt")
    image_data.append({"src": src, "alt": alt})

print(image_data)

all_links = []

# Extract and store in top_items according to instructions on the left
links = soup.select("a")
print("Liczba linków = ", len(links))
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ""

    href = ahref.get("href")
    href = href.strip() if href is not None else ""
    all_links.append({"href": href, "text": text})

print(all_links)

all_products = []

# Extract and store in top_items according to instructions on the left
products = soup.select('div.thumbnail')
for product in products:
    name = product.select('h4 > a')[0].text.strip()
    description = product.select('p.description')[0].text.strip()
    description = re.sub("[\n\t.,\"]","",description)

    price = product.select('h4.price')[0].text.strip()
    reviews = product.select('div.ratings')[0].text.strip()
    image = product.select('img')[0].get('src')

    all_products.append({
        "name": name,
        "description": description,
        "price": price,
        "reviews": reviews,
        "image": image
    })


keys = all_products[0].keys()
print("keys = ", keys)

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)
