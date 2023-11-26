from AutocompleteNgrams import AutocompleteNgrams
from AVLTree import AVLTree


def main():
    # Pfad zur Test-CSV-Datei
    test_csv_file = "/Users/karahankrc/Downloads/StudentTask/1_gram.csv"

    # Erstellt Instanz mit der CSV Datei
    autocomplete_ngrams = AutocompleteNgrams(test_csv_file)

    # get-Methode mit waves als Beispiel (Konstante Laufzeit)
    ngram_to_search = "waves"
    frequency = autocomplete_ngrams.get(ngram_to_search)
    print(f"Frequenz von '{ngram_to_search}': {frequency}")

    # get-k-possible-suggestion mit wa als Beispiel (Logarithmische Laufzeit)
    input_string = "wa"
    k = 3
    # suggestions, searched_nodes = autocomplete_ngrams.get_k_possible_suggestions(input_string, k)
    # print(f"Vorschläge für '{input_string}': {suggestions}")
    # print(f"Anzahl untersuchter Nodes: {searched_nodes}")
    # print("AVL Tree:")
    # autocomplete_ngrams.AVLTree.print_tree();


if __name__ == "__main__":
    main()
