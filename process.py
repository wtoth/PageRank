import pandas as pd
from ast import literal_eval

def clean_errors():
    df = pd.read_csv("crawled_site.csv", converters={"links": literal_eval})
    df = df[df.links.apply(lambda x: x[0]) != "Page Error"]
    return df

#Remove all external urls & anchor tags (#)
#Will likely have to be updated for other websites
def only_internal(link_list):
    internal_links = []
    for link in link_list:
        try:
            if link[0] == "/":
                if "#" in link:
                    link = link.split("#")[0]
                internal_links.append(link)
        except:
            pass
    return internal_links


def clean_external_links(data):
    data["links"] = data["links"].apply(only_internal)
    data.to_csv("cleaned_site.csv")
