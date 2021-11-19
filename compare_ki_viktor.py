"""Iteriert durch das Array und Vergleicht ob das erkannte Zeichen/Wort dem korrekten entspricht.
    Bei einem Treffer wird 1 ins neuen Array eingefügt und hitcount erhöht. Bei einem falsch/nicht
    erkannten Zeichen wird -1 ins Array eingefügt. Am Ende wird noch berechnet, wie viel Prozent richtig erkannt wurden."""

""" Original steht hier für das Array, dass die korrekte Lösung beinhaltet. Azure steht für das Array mit den von Azure
    erkannten Werten. Google steht für das Array mit den von Google erkannten Werten."""

from statistics import mean

def compare(original, azure, google):


    azure_correct = []
    azure_confidence_correct = []
    azure_confidence_false = []
    i1 = 0
    hitcount1 = 0
    for x in azure:
        if x[1] == original[i1][1]:
            azure_correct.append(1)
            hitcount1 += 1
            azure_confidence_correct.append(x[2])
        else:
            azure_correct.append(-1)
            azure_confidence_false.append(x[2])
        i1 += 1
    azure_correct_percentage = hitcount1 / len(azure_correct)
    azure_confidence_correct_percentage = mean(azure_confidence_correct)
    azure_confidence_false_percentage = mean(azure_confidence_false)

    # print(azure_correct)
    # print(azure_correct_percentage)
    # print(azure_confidence_correct)
    # print(azure_confidence_correct_percentage)
    # print(azure_confidence_false)
    # print(azure_confidence_false_percentage)

    google_correct = []
    google_confidence_correct = []
    google_confidence_false = []
    i2 = 0
    hitcount2 = 0
    for x in google:
        if x[1] == original[i2][1]:
            google_correct.append(1)
            hitcount2 += 1
            google_confidence_correct.append(x[2])
        else:
            google_correct.append(-1)
            google_confidence_false.append(x[2])
        i2 += 1
    google_correct_percentage = hitcount2 / len(google_correct)
    google_confidence_correct_percentage = mean(google_confidence_correct)
    google_confidence_false_percentage = mean(google_confidence_false)

    # print(google_correct)
    # print(google_correct_percentage)
    # print(google_confidence_correct)
    # print(google_confidence_correct_percentage)
    # print(google_confidence_false)
    # print(google_confidence_false_percentage)

    return (azure_correct, azure_correct_percentage, azure_confidence_correct, azure_confidence_correct_percentage,
            azure_confidence_false, azure_confidence_false_percentage, google_correct, google_correct_percentage,
            google_confidence_correct, google_confidence_correct_percentage, google_confidence_false,
            google_confidence_false_percentage)


"""Zu Testzwecken erstellte Arrays"""

original = [([1385, 319, 1431, 319, 1431, 356, 1385, 356], '137', 0.9800000190734863),
            ([793, 371, 826, 371, 826, 401, 793, 401], 'CR', 0.9900000095367432),
            ([837, 371, 893, 372, 893, 403, 837, 402], '72,3', 0.9900000095367432)]

azure = [([1385, 319, 1431, 319, 1431, 356, 1385, 356], '135', 0.25),
         ([793, 371, 826, 371, 826, 401, 793, 401], 'CB', 0.16),
         ([837, 371, 893, 372, 893, 403, 837, 402], '72,3', 0.9900000095367432)]

google = [([1385, 319, 1431, 319, 1431, 356, 1385, 356], '135', 0.26),
          ([793, 371, 826, 371, 826, 401, 793, 401], 'CR', 0.9900000095367432),
          ([837, 371, 893, 372, 893, 403, 837, 402], '72,3', 0.9900000095367432)]

print(compare(original, azure, google))