import csv
from Collector import Collector


class Recorder:
    def __init__(self):
        self.fieldnames = ["Negative", "Neutral", "Positive"]

        with open('data.csv', 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            csv_writer.writeheader()

    def record(self, prob):
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)

            info = {
                "Negative": prob[0],
                "Neutral": prob[1],
                "Positive": prob[2]
            }

            csv_writer.writerow(info)
            print(prob[0], prob[1], prob[2])
