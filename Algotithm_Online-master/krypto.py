import numpy as np
import string


class City:
    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y


# nltk.download()
list_city = []

list_city.append(City(52.2326863, 20.7810167, "Warszawa"))
list_city.append(City(54.360763, 18.4098512, "Gdansk"))
list_city.append(City(53.4293685, 14.344447, "Szczecin"))
list_city.append(City(51.1271647, 16.9218245, "Wroclaw"))
list_city.append(City(50.0468548, 19.9348336, "Krakow"))
list_city.append(City(52.5069704, 13.2846502, "Berlin"))
list_city.append(City(54.1476708, 12.0068719, "Rostok"))
list_city.append((City(51.3419134, 12.2535532, "Lipsk")))
list_city.append(City(50.0598058, 14.325542, "Praga"))
list_city.append(City(49.2021611, 16.5079211, "Brno"))
list_city.append(City(48.1359244, 16.9758349, "Bratyslawa"))
list_city.append(City(48.6975566, 21.0991105, "Koszyce"))
list_city.append(City(47.4813602, 18.9902208, "Budapeszt"))


def odleglosc_miast(list_city):
    list_dist = []
    x = len(list_city)
    for j in range(x):
        for i in range(len(list_city) - 1):
            print(i)
            list_dist.append(
                (
                    list_city[0].name + "-" + list_city[i + 1].name,
                    1.15
                    * np.sqrt(
                        ((list_city[i + 1].x - list_city[0].x) ** 2)
                        + (
                            (
                                (
                                    np.cos((list_city[0].x * np.pi) / 180)
                                    * (list_city[i + 1].y - list_city[0].y)
                                )
                                ** 2
                            )
                        )
                    )
                    * (40075.704 / 360),
                )
            )
        del list_city[0]
    return list_dist


xx = odleglosc_miast(list_city)
f = open("city_file", "w")
for i in xx:
    f.write(str(i) + "\n")

f.close()
