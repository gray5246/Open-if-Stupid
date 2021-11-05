if __name__ == '__main__':
    import folium
    import csv
    volcs = open("data/volcanoes.tsv")
    dialect = csv.Sniffer().sniff(volcs.read(1000))
    volcs.seek(0)
    reader = csv.DictReader(volcs)