def text_content_analyzer(f):
    words = []
    nbOfSentences = 0
    punctuation = []
    wordsCount = {}

    for line in f:
        nbOfSentences += len(re.split(r'[.!?]+', line.strip()))-1
        lineWords = line.split()

        words = words + lineWords
        for word in lineWords:
            if word in wordsCount:
                wordsCount[word] += 1
            else:
                wordsCount[word] = 1
   
    print("Total word count: %1.0f" %len(words))
    print(wordsCount)
    print("Unique words: " , len(wordsCount.keys()))
    print(nbOfSentences)
    return len(words), wordsCount, len(wordsCount.keys()), nbOfSentences