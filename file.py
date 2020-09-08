#Read a file
with open("javascript.txt", mode="r") as s_file:
    words_all = []
    for line in s_file.readlines():
        words = line.strip().split(" ")
        words_all += words


    unique_words = set(words_all)
    print(len(words_all))
    print(len(unique_words))
    
    with open("unique_words.txt", mode = "w") as writer_file:
        for item in sorted(unique_words):
            writer_file.write(item)
            writer_file.write("\n")

print("Finished")