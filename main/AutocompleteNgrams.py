import csv
from AVLTree import AVLTree
from ConstantDatastructure import ConstantDatastructure
from LogarithmicDatastructure import LogarithmicDatastructure


class AutocompleteNgrams:

    def __init__(self, filename: str):
        """ Initialisiert AutocompleteNgrams
        :param filename: Der Dateipfad zum csv file
        """
        self.logarithmic_time_structure = LogarithmicDatastructure()
        self.constant_time_structure = ConstantDatastructure()
        self.read_csv_file(filename)

    def read_csv_file(self, filename: str):
        """ Liest die Daten von einem csv file und fügt sie dem self.avl_tree hinzu.

        :param filename: Der Dateipfad zum csv file
        """
        # TODO: ERLEDIGT
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                # Stellen Sie sicher, dass die Zeile mindestens ein Element hat
                if row:
                    # Trennen Sie das erste Element (Spalte A) in Schlüssel und Frequenz
                    key = row[0]
                    frequency = row[1]
                    self.logarithmic_time_structure.insert(key, frequency)
                    self.constant_time_structure.insert(key, frequency)
                else:
                    print(f"Zeile enthält keine Werte: {row}")


    def get(self, ngram: str):
        """
        :param ngram: Das N-gram, welches gefunden werden soll.
        :return: Wenn das n-gram gefunden wurde, wird die Frequenz des N-grams zurückgegeben,
                falls es nicht gefunden werden konnte wird None zurückgegeben.
        """
        # TODO: ERLEDIGT
        # frequency = self.constant_time_structure.get(ngram)
        frequency = self.logarithmic_time_structure.get(ngram)
        return frequency

    def get_k_possible_suggestions(self, input_string: str, k: int):
        """
        :param input_string: Der String für den Fortsetzungen vorgeschlagen werden.
        :param k: Die Anzahl an gewünschten Vorschlägen.
        :return: Eine Liste mit den k Vorschlägen,
                die Anzahl untersuchter Nodes im AVL Baum.
        """
        ngrams_dict, searched_nodes = self.logarithmic_time_structure.get_k_possible_suggestions(input_string, k)

        # Sortieren der N-Gramme nach Frequenz und Begrenzung auf k Vorschläge
        sorted_suggestions = sorted(ngrams_dict.items(), key=lambda item: item[1], reverse=True)[:k]
        suggestions = [suggestion[0] for suggestion in sorted_suggestions]

        return suggestions, searched_nodes

