def show_percentage(data_list: [str]):
    word_dict = dict()
    for data in data_list:
        word_count = len(data.split())
        if word_count not in word_dict:
            word_dict[word_count] = 1
        else:
            word_dict[word_count] += 1

    total_words = sum(word_dict.values())

    for word_count, repeats in sorted(word_dict.items()):
        percentage = (repeats / total_words) * 100
        print(f"{word_count} word: {percentage:.2f}%")


search_queries = ["watch new movies", "coffee near me", "how to find the determinant", "python",
                  "data science jobs in UK", "courses for data science", "taxi", "google", "yandex", "bing",
                  "foreign exchange rates USD/BYN", "Netflix movies watch online free",
                  "Statistics courses online from top universities"]

show_percentage(search_queries)
