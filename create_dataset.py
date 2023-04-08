import os
os.environ['PANDAS_NO_USE_ARCHIVES'] = 'True'
import pandas as pd

# set the path to the news article and summary folders
news_folder_path = r"C:\Users\roaas\Documents\roaa_workspace\text-summarization\Data\News Articles"
summary_folder_path = r"C:\Users\roaas\Documents\roaa_workspace\text-summarization\Data\Summaries"

# initialize empty lists to store the data
text_list = []
summary_list = []

# loop through the news article folders and extract the text files
for folder_name in os.listdir(news_folder_path):
    if os.path.isdir(os.path.join(news_folder_path, folder_name)):  # check if the current path is a directory
        folder_path = os.path.join(news_folder_path, folder_name)
        for file_name in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file_name)):  # check if the current path is a file
                with open(os.path.join(folder_path, file_name), "r") as f:
                    text = f.read()
                    text_list.append(text)

                    # get the corresponding summary file
                    summary_file_path = os.path.join(summary_folder_path, folder_name, file_name)
                    if os.path.isfile(summary_file_path):
                        with open(summary_file_path, "r") as f:
                            summary = f.read()
                            summary_list.append(summary)

# create a pandas DataFrame with the text and summary data
df = pd.DataFrame({"Text": text_list, "Summary": summary_list})

# write the DataFrame to a CSV file
df.to_csv("Dataset.csv", index=False)
