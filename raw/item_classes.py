import textwrap as wrap
import random as r

LINEWIDTH = 80
SEPARATOR = "=" * LINEWIDTH

class Numenera:

    @staticmethod
    def _get_index(csv_row: list):

        """
        :param csv_row: single row of comma-separated values containing an item
        :return: item index starting from 101
        """

        hundreds = csv_row[0]
        tens = csv_row[1]
        return int(hundreds) * 100 + int(tens)

    @staticmethod
    def _get_level(csv_level: str):

        level_list = csv_level.split(sep="+")

        if "d" in level_list[0]:
            dice_split = level_list[0].split("d")
            die_roll = int(dice_split[1])
            level_list[0] = r.randint(1, die_roll)

        level_list_int = [int(level) for level in level_list]

        return sum(level_list_int)

    @staticmethod
    def _text_wrapper(text):
        return wrap.fill(text, width=LINEWIDTH)



class Artifact(Numenera):

    def __init__(self, csv_row: list):
        self.index = self._get_index(csv_row)
        self.name = csv_row[2]
        self.description = csv_row[3]
        self.level_diced = csv_row[4]
        self.level_calc = self._get_level(self.level_diced)
        self.depletion = csv_row[5]
        self.form = csv_row[6]

    def __str__(self):
        display_string = "\n".join([
            f"{SEPARATOR}",
            f"{self.name.upper()} (lvl {self.level_calc} // {self.level_diced})",
            f"Depletion: {self.depletion}",
            f"{SEPARATOR}",
            f"{self._text_wrapper(self.form)}",
            f"",
            f"{self._text_wrapper(self.description)}",
            f"{SEPARATOR}"
        ])

        return display_string


class Cypher(Numenera):

    def __init__(self, csv_row: list):
        self.index = self._get_index(csv_row)
        self.name = csv_row[2]
        self.description = csv_row[3]
        self.level_diced = csv_row[4]
        self.level_calc = self._get_level(self.level_diced)
        raw_forms = csv_row[5:]
        self.forms = list(filter(None, raw_forms)
)
    def __str__(self):
        display_string  = "\n".join([
            f"{SEPARATOR}",
            f"{self.name.upper()} (lvl {self.level_calc} // {self.level_diced})",
            f"Single use",
            f"{SEPARATOR}",
            f"{self._text_wrapper(r.choice(self.forms))}",
            f"",
            f"{self._text_wrapper(self.description)}",
            f"{SEPARATOR}"
        ])

        return display_string


class Oddity(Numenera):

    def __init__(self, csv_row: list):
        self.index = self._get_index(csv_row)
        self.description = csv_row[2]

    def __str__(self):
        display_string = "\n".join([
            f"{SEPARATOR}",
            f"{self._text_wrapper(self.description)}",
            f"{SEPARATOR}"
        ])

        return display_string
