text = "TTACGTAAAGTGGATGGATGAAGAGCAGAGGCTACGACAAGTAGAGGCTATGAAGAGCAGAGGCTAGTGGATGGAGTGGATGGAGTGGATGGAGAGGCTATGAAGAGCACGACAAGTACGACAAGTATGAAGAGCTTACGTAATTACGTAAAGAGGCTAGTGGATGGAGTGGATGGACGACAAGTAGAGGCTAGAGGCTTTACGTAAATGAAGAGCAGAGGCTAGTGGATGGACGACAAGTAGTGGATGGTTACGTAAACGACAAGTAGTGGATGGATGAAGAGCAGAGGCTAGAGGCTATGAAGAGCAGAGGCTATGAAGAGCAGTGGATGGATGAAGAGCATGAAGAGCAGAGGCTAGAGGCTTTACGTAATTACGTAAACGACAAGTTTACGTAAAGAGGCTAGAGGCTAGAGGCTTTACGTAAACGACAAGTATGAAGAGCAGAGGCTAGTGGATGGAGAGGCTTTACGTAAAGAGGCTTTACGTAAATGAAGAGCAGAGGCTTTACGTAAAGTGGATGGACGACAAGTAGTGGATGGATGAAGAGCTTACGTAAAGTGGATGGTTACGTAAATGAAGAGCATGAAGAGCACGACAAGTAGTGGATGGTTACGTAATTACGTAATTACGTAAACGACAAGTACGACAAGTATGAAGAGCAGTGGATGGATGAAGAGCTTACGTAAAGAGGCTAGTGGATGGACGACAAGTATGAAGAGCACGACAAGTAGAGGCTAGAGGCTACGACAAGTTTACGTAAACGACAAGTTTACGTAAACGACAAGTATGAAGAGCATGAAGAGCAGAGGCTAGAGGCTAGTGGATGGATGAAGAGCATGAAGAGC"
k = 10

def FrequentWords(text, k):
    count = [0] * (len(text) - k + 1)
    for i in range(len(text) - k + 1):
        for j in range(len(text) - k + 1):
            if text[j:j + k] == text[i:i + k]:
                count[i] += 1
    for i in range(len(text) - k + 1):
        if count[i] == max(count):
            print(text[i:i + k], max(count))
            break


FrequentWords(text,k)
