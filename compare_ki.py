"""Compares Image https://wiprojektstorage.blob.core.windows.net/processed/pwhjnurtwmhepqdg.jpg"""
from statistics import mean
import csv
import requests


def number_correct(google, azure, original):
    google_correct = 0
    azure_correct = 0
    for i in range(len(original)):
        if google[i][0] == original[i]:
            google_correct = google_correct + 1

        if azure[i][0] == original[i]:
            azure_correct = azure_correct + 1
    return google_correct, azure_correct


def percentage_correct(google, azure, original):
    google_correct, azure_correct = number_correct(google, azure, original)
    google_percentage = google_correct / len(original)
    azure_percentage = azure_correct / len(original)

    return google_percentage, azure_percentage


def wrong_recognized(google, azure, original):
    google_wrong = []
    azure_wrong = []

    for i in range(len(original)):
        if google[i][0] != original[i]:
            google_wrong.append([original[i], google[i][0]])

        if azure[i][0] != original[i]:
            azure_wrong.append([original[i], azure[i][0]])

    return google_wrong, azure_wrong


def confidence_false(google, azure, original):
    google_wrong = []
    azure_wrong = []
    highest_confidence_google = 0.0
    highest_confidence_azure = 0.0

    for i in range(len(original)):
        if google[i][0] != original[i] and google[i][1] != 0:
            google_wrong.append(google[i][1])
            if google[i][1] > highest_confidence_google:
                highest_confidence_google = google[i][1]

        if azure[i][0] != original[i] and azure[i][1] != 0:
            azure_wrong.append(azure[i][1])
            if azure[i][1] > highest_confidence_azure:
                highest_confidence_azure = azure[i][1]

    google_mean = 0.0
    azure_mean = 0.0
    if len(google_wrong) > 0:
        google_mean = mean(google_wrong)
    if len(azure_wrong) > 0:
        azure_mean = mean(azure_wrong)

    return google_mean, azure_mean, highest_confidence_google, highest_confidence_azure


def confidence_true(google, azure, original):
    google_correct = []
    azure_correct = []
    lowest_confidence_google = 1.0
    lowest_confidence_azure = 1.0

    for i in range(len(original)):
        if google[i][0] == original[i]:
            google_correct.append(google[i][1])
            if google[i][1] < lowest_confidence_google:
                lowest_confidence_google = google[i][1]

        if azure[i][0] == original[i]:
            azure_correct.append(azure[i][1])
            if azure[i][1] < lowest_confidence_azure:
                lowest_confidence_azure = azure[i][1]

    google_mean = 0.0
    azure_mean = 0.0
    if len(google_correct) > 0:
        google_mean = mean(google_correct)
    if len(azure_correct) > 0:
        azure_mean = mean(azure_correct)

    return google_mean, azure_mean, lowest_confidence_google, lowest_confidence_azure

def csv_export(data):
    f = open('report.csv', 'w', encoding='ASCII', newline='')
    writer = csv.writer(f, delimiter=';')
    header = ['ki typ', 'anz. richtig erkannt', 'proz. richtig erkannt', 'mittelwert konfidenz von falsch erkannt',
              'hoechste konfidenz von falsch erkannt', 'mittelwert konfidenz von richtig erkannt',
              'niedrigste konfidenz von richtig erkannt']

    writer.writerow(header)
    writer.writerows(data)
    f.close()

if __name__ == '__main__':
    google = [['4', 0.7300000190734863], ['17', 0.9900000095367432], ['-1', 0.0], ['15', 0.9800000190734863],
              ['5', 0.9900000095367432], ['13', 0.9599999785423279], ['11', 0.9800000190734863],
              ['1', 0.9900000095367432], ['3', 0.9900000095367432], ['-1', 0.0], ['12', 0.9900000095367432],
              ['16', 0.9900000095367432], ['2', 0.9900000095367432], ['18', 0.9900000095367432],
              ['4', 0.9900000095367432], ['14', 0.9700000286102295], ['6', 0.9800000190734863],
              ['8', 0.9700000286102295], ['10', 0.9399999976158142], ['35', 0.9900000095367432],
              ['37', 0.9900000095367432], ['72', 0.9900000095367432]]

    # azure = [['9', 0.938], ['17', 0.414], ['-1', 0.0], ['15', 0.821], ['5', 0.878], ['73', 0.414], ['11', 0.844],
    #          ['1', 0.627], ['3', 0.821], ['4', 0.878], ['12', 0.531], ['16', 0.785], ['2', 0.495], ['18', 0.878],
    #          ['4', 0.414], ['14', 0.676], ['-1', 0.0], ['8', 0.821], ['10', 0.531], ['35', 0.495], ['37', 0.495],
    #          ['72', 0.878]]

    # original = ['9', '17', '7', '15', '5', '13', '11', '1', '3', '4', '12', '16', '2', '18',
    #             '4', '14', '6', '8', '10', '35', '37', '72']

    scorecards = [['5', '3', '4', '4', '5', '4', '4', '5', '5', '38', '3', '3', '6', '3', '4', '4', '5', '4', '5', '37', '-1', '75'],
                ['9', '17', '7', '15', '5', '13', '11', '1', '3', '4', '12', '16', '2', '18', '4', '14', '6', '8', '10', '35', '37', '72'],
                ['5', '3', '4', '4', '5', '4', '4', '5', '5', '38', '3', '3', '6', '3', '4', '4', '5', '4', '5', '37', '-1', '75'],
                ['5', '3', '4', '4', '5', '4', '4', '5', '5', '38', '3', '3', '6', '3', '4', '4', '5', '4', '5', '37', '-1', '75'],
                ['9', '17', '7', '15', '5', '13', '11', '1', '3', '4', '12', '16', '2', '18', '4', '14', '6', '8', '10', '35', '37', '72'],
                ['5', '3', '4', '4', '5', '4', '4', '5', '5', '38', '3', '3', '6', '3', '4', '4', '5', '4', '5', '37', '-1', '75'],
                ['9', '17', '7', '15', '5', '13', '11', '1', '3', '4', '12', '16', '2', '18', '4', '14', '6', '8', '10', '35', '37', '72'],
                ['9', '17', '7', '15', '5', '13', '11', '1', '3', '4', '12', '16', '2', '18', '4', '14', '6', '8', '10', '35', '37', '72'],
                ['9', '17', '7', '15', '5', '13', '11', '1', '3', '4', '12', '16', '2', '18', '4', '14', '6', '8', '10', '35', '37', '72'],
                ['5', '3', '4', '4', '5', '4', '4', '5', '5', '38', '3', '3', '6', '3', '4', '4', '5', '4', '5', '37', '-1', '75'],
                ['9', '17', '7', '15', '5', '13', '11', '1', '3', '4', '12', '16', '2', '18', '4', '14', '6', '8', '10', '35', '37', '72'],
                ['9', '17', '7', '15', '5', '13', '11', '1', '3', '4', '12', '16', '2', '18', '4', '14', '6', '8', '10', '35', '37', '72'],
                ['6', '4', '5', '6', '1', '5', '3', '8', '4', '48', '4', '5', '6', '3', '4', '3', '1', '4', '3', '39', '-1', '87'],
                ['6', '4', '5', '6', '1', '5', '3', '8', '4', '48', '4', '5', '6', '3', '4', '3', '1', '4', '3', '39', '-1', '87'],
                ['6', '4', '5', '6', '1', '5', '3', '8', '4', '48', '4', '5', '6', '3', '4', '3', '1', '4', '3', '39', '-1', '87']]

    data = []
    i = 0
    for original in scorecards:
        i += 1
        print(f'Analyzing Scorecard {i}')
        # url = f'https://wiprojekt-ki.azurewebsites.net/analyze?img=scorecard{i}.jpg&service=google'
        # google_response = requests.get(url)
        # google = eval(google_response.text.split()[0])

        url = f'https://wiprojekt-ki.azurewebsites.net/analyze?img=scorecard{i}.jpg&service=azure'
        azure_response = requests.get(url)
        azure = eval(azure_response.text.split()[0])

        correct_google, correct_azure = number_correct(google, azure, original)
        # print(f'Anzahl richtig erkannter Zahlen von {len(original)}: \nGoogle: {correct_google}\nAzure: {correct_azure}\n')

        google_percentage, azure_percentage = percentage_correct(google, azure, original)
        # print(f'Prozent richtig erkannt:\nGoogle: {google_percentage:.2%}\nAzure: {azure_percentage:.2%}\n')

        # wrong_recognized_google, wrong_recognized_azure = wrong_recognized(google, azure, original)
        # str_wrong_google = str(wrong_recognized_google).replace("'", "")[1:-1:1]
        # str_wrong_azure = str(wrong_recognized_azure).replace("'", "")[1:-1:1]
        # print(f'Falsch erkannte Zahlen (original, erkannt):\nGoogle: {str_wrong_google}\nAzure: {str_wrong_azure}\n')

        google_mean_false, azure_mean_false, highest_confidence_google, highest_confidence_azure = confidence_false(google, azure,
                                                                                                        original)
        # print(f'Mittelwert der Konfidenz von Falsch erkannten Zahlen:\nGoogle: {google_mean_false:.3}\nAzure: {azure_mean_false:.3}\n')
        # print(f'Höchste Konfidenz von Falsch erkannten Zahlen:\nGoogle: {highest_confidence_google:.3}\nAzure: {highest_confidence_azure:.3}\n')

        google_mean_true, azure_mean_true, lowest_confidence_google, lowest_confidence_azure = confidence_true(google, azure, original)
        # print(f'Mittelwert der Konfidenz von Richtig erkannten Zahlen:\nGoogle: {google_mean_true:.3}\nAzure: {azure_mean_true:.3}\n')
        # print(f'Niedrigste Konfidenz von Richtig erkannten Zahlen:\nGoogle: {lowest_confidence_google:.3}\nAzure: {lowest_confidence_azure:.3}')

        data_google = ['google', correct_google, f'{google_percentage:.3}'.replace(".", ","),
                       f'{google_mean_false:.3}'.replace(".", ","), f'{highest_confidence_google:.3}'.replace(".", ","),
                       f'{google_mean_true:.3}'.replace(".", ","), f'{lowest_confidence_google:.3}'.replace(".", ",")]
        data_azure = ['azure', correct_azure, f'{azure_percentage:.3}'.replace(".", ","), f'{azure_mean_false:.3}'.replace(".", ","),
                      f'{highest_confidence_azure:.3}'.replace(".", ","), f'{azure_mean_true:.3}'.replace(".", ","),
                      f'{lowest_confidence_azure:.3}'.replace(".", ",")]

        data.append(data_google)
        data.append(data_azure)

    csv_export(data)