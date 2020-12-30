import os
import pandas as pd


class LiveProjectPopularityBasedRecs:

    def __init__(self):

        self.charts = {}
        charts_folder = "charts"
        if os.path.isdir(charts_folder):

            for file in os.listdir("charts"):
                name, ext = file.split('.')
                if ext == "csv" and len(name) > 0:
                    self.charts[name] = pd.read_csv("{}/{}".format(charts_folder, file), index_col=0)
        else:
            print("Genre Global and Charts not implemented!")

    def genre_chart(self, genre):
        if genre in self.charts:
            return self.charts[genre]
        elif "Top" in self.charts:
            return self.charts["Top"]
        else:
            return ""


