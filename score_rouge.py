import csv
from rouge import Rouge

# Load the data from the output CSV file
with open('output.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    summaries = []
    model_summaries = []
    for row in reader:
        summaries.append(row['Summary'])
        model_summaries.append(row['model_summary'])

# Calculate the ROUGE scores
rouge = Rouge()
scores = rouge.get_scores(summaries, model_summaries, avg=True)

# Print the scores
print("ROUGE-1: {:.2f}".format(scores['rouge-1']['f']*100))
print("ROUGE-2: {:.2f}".format(scores['rouge-2']['f']*100))
print("ROUGE-L: {:.2f}".format(scores['rouge-l']['f']*100))

print('ROUGE-1 Precision:', scores['rouge-1']['p'])
print('ROUGE-1 Recall:', scores['rouge-1']['r'])
print('ROUGE-1 F1 Score:', scores['rouge-1']['f'])
print('ROUGE-2 Precision:', scores['rouge-2']['p'])
print('ROUGE-2 Recall:', scores['rouge-2']['r'])
print('ROUGE-2 F1 Score:', scores['rouge-2']['f'])
print('ROUGE-L Precision:', scores['rouge-l']['p'])
print('ROUGE-L Recall:', scores['rouge-l']['r'])
print('ROUGE-L F1 Score:', scores['rouge-l']['f'])
