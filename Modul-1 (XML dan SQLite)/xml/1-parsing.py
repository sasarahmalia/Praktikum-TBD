import xml.etree.ElementTree as ET

# Membaca file xml 
tree = ET.parse("xml/books.xml")
root = tree.getroot()

# Menampilkan informasi tentang setiap buku 
for boook in root.findall('book'):
    # Mengakses informasi buku 
    title = book.find('title').text
    author = book.find('author').text
    price = book.find('price').text
    
    # Menampilkan informasi buku
    print("Title:", title)
    print("Author:", author)
    print("Price:", price)
    print()