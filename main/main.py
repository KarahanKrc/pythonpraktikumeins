from AutocompleteNgrams import AutocompleteNgrams


def main():
    # Pfad zur Test-CSV-Datei
    test_csv_file = "/Users/karahankrc/Downloads/StudentTask/avltree_head.csv"

    # Erstellt Instanz mit der CSV Datei
    autocomplete_ngrams = AutocompleteNgrams(test_csv_file)

    # get-Methode mit waves als Beispiel (Konstante Laufzeit)   ->  Get-Methode // Karahan
    ngram_to_search = "i-aa"
    frequency = autocomplete_ngrams.get(ngram_to_search)
    print(f"Frequenz von '{ngram_to_search}': {frequency}")

    # get-k-possible-suggestion mit wa als Beispiel (Logarithmische Laufzeit)   ->      Suggestion // Kawa
    input_string = "head"
    k = 3
    suggestions, searched_nodes = autocomplete_ngrams.get_k_possible_suggestions(input_string, k)
    print(f"Vorschläge für '{input_string}': {suggestions}")
    print(f"Anzahl untersuchter Nodes: {searched_nodes}")


if __name__ == "__main__":
    main()
