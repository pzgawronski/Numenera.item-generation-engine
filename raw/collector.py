import csv


def collect(source_file, collection_class):

    """
    :param source_file: item list converted from google docs into comma-separated values
    :param collection_class: item type (Artifact, Cypher, or Oddity)
    :return new_item_dict: item list converted from csv into python-based dict; index-based
    """

    with open(source_file, newline='', encoding="utf-8") as source:
        new_reader = csv.reader(source, delimiter=",")
        rows_listed = []
        for row in new_reader:
            rows_listed.append(row)

        new_item_dict = {}

        for row in rows_listed[1:]:
            new_item = collection_class(row)
            new_item_dict[new_item.index] = new_item

        return new_item_dict


class Numenera:

    def _get_index(self, csv_row: list):

        """
        :param csv_row: single row of comma-separated values containing an item
        :return: item index starting from 101
        """

        hundreds = csv_row[0]
        tens = csv_row[1]
        return int(hundreds) * 100 + int(tens)


class Artifact(Numenera):

    def __init__(self, csv_row: list):
        self.index = self._get_index(csv_row)
        self.name = csv_row[2]
        self.description = csv_row[3]
        self.level = csv_row[4]
        self.depletion = csv_row[5]
        self.form = csv_row[6:]


class Cypher(Numenera):

    def __init__(self, csv_row: list):
        self.index = self._get_index(csv_row)
        self.name = csv_row[2]
        self.description = csv_row[3]
        self.level = csv_row[4]
        self.form = csv_row[5:]


class Oddity(Numenera):

    def __init__(self, csv_row: list):
        self.index = self._get_index(csv_row)
        self.description = csv_row[2]
