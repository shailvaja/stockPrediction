import requests
import zipfile
import io
import database_queries
class Data:
    def __init__(self, dt):
        self.date = dt
        self.date = dt.strftime("%d%m%y")
    bse_link = r'https://www.bseindia.com/download/BhavCopy/Equity/'
    file_name = 'EQ_ISINCODE_'
    file_extension = '.zip'
    link = ''
    csv_rows = 0
    prev_count = 0
    next_count = 0



    def full_link(self):
        self.link = str(self.bse_link) + str(self.file_name) + str(self.date) + str(self.file_extension)

    def get_zip(self):
        url = self.link
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
            "Upgrade-Insecure-Requests": "1", "DNT": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}
        r = requests.get(url, headers = headers,  stream=True)
        if r.ok:
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall("Files/")
        else:
            return 1

    def update_csv(self):
        text = open('EQ_ISINCODE_060122.CSV', "r")

        # join() method combines all contents of
        # csvfile.csv and formed as a string
        text = ''.join([i for i in text])

        # search and replace the contents
        text = text.replace("06-Jan-22", "2022-01-06")


        # output.csv is the output file opened in write mode
        x = open('EQ_ISINCODE.CSV', "w")

        # all the replaced text is written in the output.csv file
        x.writelines(text)
        x.close()

    def get_prev_count(self):
        None
    def get_next_count(self):
        None

    def check_if_loaded(self):
        None

    def delete_csv(self):
        None


    def get_data(self):
        self.full_link()
        self.update_csv()
        if self.get_zip() != 1:
            database_queries.load_csv_table('EQ_ISINCODE.CSV', 'Closing')



