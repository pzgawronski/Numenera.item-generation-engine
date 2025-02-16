import csv


class Collector:

    def __init__(self, source_file: str, collection_class):
        """
        :param source_file: item list converted from Google Docs into comma-separated values
        :param collection_class: item type (Artifact, Cypher, or Oddity)
        :return new_item_dict: item list converted from csv into Python-based dict; index-based
        """

        with open(source_file, newline='', encoding="utf-8") as source:
            new_reader = csv.reader(source, delimiter=",")
            rows_listed = []
            for row in new_reader:
                rows_listed.append(row)

            self.collection = {}

            for row in rows_listed[1:]:
                new_item = collection_class(row)
                self.collection[new_item.index] = new_item
