if __name__ == '__main__':
    import folium
    import csv
    volcs = open("data/volcanoes.tsv")
    dialect = csv.Sniffer().sniff(volcs.read(1000))
    volcs.seek(0)
    reader = csv.DictReader(volcs, dialect=dialect)
    rows = list(reader)
    acm = 0
    for row in rows:
        if row['Country'] != "Indonesia":
            rows.remove(row)
        acm += 1
    for row in rows:
        location = [row['Latitude'], row['Longitude']]
        mark = folium.Marker(location, icon=folium.Icon(color='red'))
    map = folium.Map(location=(-8.108, 112.922), zoom_start=5, tiles='Stamen Terrain')
    map.save('data/map1.html')
    for row in rows:
        location = [row['Latitude'], row['Longitude']]
        mark = folium.Marker(location, icon=folium.Icon(color='red'))

