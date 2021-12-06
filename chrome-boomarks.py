import chrome_bookmarks
import csv
f = open("bookmarks.csv", "a", newline="")
writer = csv.writer(f)
for folder in chrome_bookmarks.folders:
    print(folder.name)
    print(folder.folders)
for url in chrome_bookmarks.urls:
    writer.writerow(url.url)
    writer.writerow(url.name)

