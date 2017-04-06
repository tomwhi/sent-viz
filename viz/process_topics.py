import wikipedia
from skipthoughts.skipthoughts import *
from nltk.tokenize import sent_tokenize
from sklearn.manifold import TSNE
import numpy as np
import pandas as pd
import begin

def paragraph2df(paragraph, paragraph_idx):
    sentences = sent_tokenize(paragraph)

    sentence_idxs = range(len(sentences))
    paragraph_idxs = [paragraph_idx]*len(sentences)
    return pd.DataFrame({"sentence": sentences, "sentence_idx": sentence_idxs, "paragraph_idx": paragraph_idxs})


def get_wiki_df(topic):
    wiki_data = wikipedia.page(topic)
    paragraphs = wiki_data.content.split("\n")
    paragraph_dfs = []
    for paragraph_idx in range(len(paragraphs)):
        paragraph = paragraphs[paragraph_idx]
        df = paragraph2df(paragraph, paragraph_idx)
        paragraph_dfs.append(df)

    wiki_df = pd.concat(paragraph_dfs)
    wiki_df["topic"] = [topic]*len(wiki_df)
    return wiki_df


def get_wiki_dfs(topics):
    wiki_dfs = []
    for topic in topics:
        try:
            wiki_df = get_wiki_df(topic)
            wiki_dfs.append(wiki_df)
        except Exception, e:
            pass

    return wiki_dfs


@begin.start(auto_convert=True)
def process(topics_str="New York,Chicago", output="tSNE_results_2components.txt"):
    topics = topics_str.split(",")
    combined_wiki_df = pd.concat(get_wiki_dfs(topics))

    model = load_model()
    encoder = Encoder(model)
    sentence_vecs = encoder.encode(combined_wiki_df["sentence"])

    model = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    combined_fit = model.fit_transform(sentence_vecs)

    combined_wiki_df["comp1"] = combined_fit[:,0]
    combined_wiki_df["comp2"] = combined_fit[:,1]

    combined_wiki_df.to_csv(output, sep="\t", index=False)
