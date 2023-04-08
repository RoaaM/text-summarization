import pandas as pd
import re
import networkx as nx
from collections import Counter
from math import sqrt


def calculate_similarity(sentence1, sentence2):
    # Pre-processing: convert to lowercase, remove punctuation and stop words
    sentence1 = re.sub(r'[^\w\s]', '', sentence1.lower())
    sentence2 = re.sub(r'[^\w\s]', '', sentence2.lower())
    stop_words = {'a', 'an', 'the', 'of', 'to', 'in', 'for', 'on', 'that', 'this', 'it', 'with', 'and', 'or', 'as', 'at', 'by'}
    words1 = [word for word in sentence1.split() if word not in stop_words]
    words2 = [word for word in sentence2.split() if word not in stop_words]

    # Calculate the cosine similarity between the two sentences
    word_count1 = Counter(words1)
    word_count2 = Counter(words2)
    common_words = set(words1).intersection(set(words2))
    dot_product = sum([word_count1[word] * word_count2[word] for word in common_words])
    magnitude1 = sqrt(sum([count ** 2 for count in word_count1.values()]))
    magnitude2 = sqrt(sum([count ** 2 for count in word_count2.values()]))
    similarity = dot_product / (magnitude1 * magnitude2) if magnitude1 > 0 and magnitude2 > 0 else 0.0

    return similarity

# define a function to create the hypergraph from a text
def create_hypergraph(text):
    # split the text into sentences
    sentences = text.split(". ")

    # create a graph to represent the text
    graph = nx.Graph()

    # add nodes to the graph for each sentence in the text
    for sentence in sentences:
        graph.add_node(sentence)

    # add hyperedges to the graph to connect related nodes
    for sentence1 in sentences:
        for sentence2 in sentences:
            # calculate the similarity between the two sentences
            similarity = calculate_similarity(sentence1, sentence2)

            # if the similarity is above a certain threshold, add a hyperedge between the two nodes
            if similarity > 0.5:
                graph.add_edge(sentence1, sentence2)

    return graph

# define a function to generate a summary from a hypergraph
def generate_summary(graph):
    # apply a graph-based summarization algorithm to generate a summary
    # here, we use the PageRank algorithm to rank the sentences based on their importance in the graph
    scores = nx.pagerank(graph)

    # sort the sentences by their scores in descending order
    ranked_sentences = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # select the top 3 sentences as the summary
    summary_sentences = [sentence[0] for sentence in ranked_sentences[:3]]

    # convert the summary back into text format
    summary = ". ".join(summary_sentences) + "."

    return summary

# define a function to read the data from a CSV file and generate model summaries
def generate_model_summaries(filename):
    # read the data from the CSV file
    data = pd.read_csv(filename)

    # create an empty list to store the model summaries
    model_summaries = []

    # iterate over each row in the data
    for index, row in data.iterrows():
        # extract the text and human summary from the row
        text = row['Text']
        human_summary = row['Summary']

        # create a hypergraph from the text
        graph = create_hypergraph(text)

        # generate a summary from the hypergraph
        model_summary = generate_summary(graph)

        # append the model summary to the list
        model_summaries.append(model_summary)

    # add the list of model summaries as a new column in the data
    data['model_summary'] = model_summaries

    # write the updated data to a new CSV file
    data.to_csv('output.csv', index=False)


generate_model_summaries(r'C:\Users\roaas\Documents\roaa_workspace\text-summarization\Dataset.csv')
