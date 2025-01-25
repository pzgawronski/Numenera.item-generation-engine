import csv


def collect(source_file, target_dict, collection_class):
    with open(source_file, newline='', encoding="utf-8") as source:
        new_reader = csv.reader(source, delimiter=",")
        rows_listed = []
        for row in new_reader:
            rows_listed.append(row)

        for row in rows_listed[1:]:
            new_item = collection_class(row)
            target_dict[new_item.index] = new_item


class Numenera:

    def _get_index(self, hundreds: str, tens: str):
        return int(hundreds) * 100 + int(tens)


class Artifact(Numenera):

    def __init__(self, csv_row: list):
        self.index = self._get_index(csv_row[0], csv_row[1])
        self.name = csv_row[2]
        self.description = csv_row[3]
        self.level = csv_row[4]
        self.depletion = csv_row[5]
        self.form = csv_row[6:]


class Cypher(Numenera):
    pass


class Oddity(Numenera):
    pass
