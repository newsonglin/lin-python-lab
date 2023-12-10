with open("C:\\Users\\sli\\Downloads\\activity_295809288.gpx", "r+", encoding="utf-8") as fp:
    lines = fp.readlines()
    for line in lines:
        if "<trkpt lat" in line:
            lonIndex = line.index("lon=\"")
            latIndex = line.index("lat=\"")
            lon = line[lonIndex + 5:lonIndex + 5 + 10]
            lat = line[latIndex + 5:latIndex + 5 + 9]
            print("[" + lon + "," + lat + "],")
