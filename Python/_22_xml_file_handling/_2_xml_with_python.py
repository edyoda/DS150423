from bs4 import BeautifulSoup

file = open(r"C:\Users\vashi\OneDrive\Documents\DS150423\Python\_22_xml_file_handling\xml_file.xml","r")

soup = BeautifulSoup(file,"html.parser")
# print(soup)
# print(type(soup))

# find_all converts the data into list
data = soup.find_all("student")
# print(data)
# print(type(data))

# find is used to fetch the data on the bases of tag_name
# name = soup.find("naam")
# print(name)
# print(name.text)

# for i in data:
#     print(i.find("naam").text)

name = soup.find("naam",{"name":"second"})
print(name)
print(name.text)