

# Import the required Module
import tabula
import csv
# Read a PDF File
# df=tabula.read_pdf("./assets/foo.pdf", encoding='utf-8', pages='all')[0]
tabula.convert_into("./assets/foo.pdf", "./assets/foo.csv", output_format="csv", pages='all')
# df.to_csv('./assets/foo.csv')
# df = tabula.read_pdf("./assets/foo.pdf", pages='all')
# convert PDF into CSV
# for i in df:
#     i.to_csv('./assets/foo.csv', encoding='utf-8')
#     print(i)

with open('./assets/foo.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
        if(row['Name'] == 'Bruno Nash'):
            print(row['Age'])