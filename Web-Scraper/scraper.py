""" Scraps data from the website Century21 """
import requests
from bs4 import BeautifulSoup as bs
import pandas


base_url = "https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
prop_list = []
# Go through each page
for page in range(0, 31, 10):
    page_url = base_url + str(page)

    # Load pages
    r = requests.get(page_url)
    c = r.content
    soup = bs(c, "html.parser")

    # Get the properties
    property_divs = soup.find_all("div", {"class": "propertyRow"})
    for item in property_divs:
        # Dictionary
        d = {}
        # Find Specific data
        d["Address"] = item.find_all("span", {"class", "propAddressCollapse"})[0].text
        d["Locality"] = item.find_all("span", {"class", "propAddressCollapse"})[1].text
        price = item.find("h4", {"class", "propPrice"})
        d["Price"] = price.text.replace("\n", "").replace(" ", "")
        try:
            d["Beds"] = item.find("span", {"class", "infoBed"}).find("b").text
        except:
            d["Beds"] = "Uknown"
        for column_group in item.find_all("div", {"class": "columnGroup"}):
            iterable = zip(column_group.find_all("span", {"class": "featureGroup"}),
                           column_group.find_all("span", {"class": "featureName"}))
            for feature_group, feature_name in iterable:
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text

        prop_list.append(d)

df = pandas.DataFrame(prop_list)
df.to_csv("Output.csv")
