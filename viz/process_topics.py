import wikipedia
import codecs
import logging
from skipthoughts.skipthoughts import *
from nltk.tokenize import sent_tokenize
from sklearn.manifold import TSNE
import bhtsne
import matplotlib.pyplot as plt
import numpy as np

def plot_2d(data2d):
    plt.figure(figsize=(6,6))
    plt.scatter(data2d[:,0], data2d[:,1], s=1)
    plt.show()

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
            logging.info("Failed to retrieve topic:")
            pass

    return wiki_dfs


@begin.start(auto_convert=True)
def process(topics_str="New York,Chicago", output="tSNE_results_2components.txt"):
    topics = topics_str.split(",")
    combined_wiki_df = pd.concat(get_wiki_dfs(topics))

    logging.basicConfig(level=logging.DEBUG)

    model = load_model()
    encoder = Encoder(model)
    sentence_vecs = encoder.encode(combined_wiki_df["sentence"])

    pd.DataFrame(sentence_vecs).to_csv("SentenceVectors.txt", sep="\t")

    model = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    combined_fit = model.fit_transform(sentence_vecs)

    p = 30
    t = 0.5
    data2d = bhtsne.tsne(sentence_vecs.astype("float64"), perplexity=p, theta=t)
    #plot_2d(data2d)

    combined_wiki_df["comp1"] = data2d[:,0]
    combined_wiki_df["comp2"] = data2d[:,1]
    combined_wiki_df["comp1_sklearn"] = combined_fit[:,0]
    combined_wiki_df["comp2_sklearn"] = combined_fit[:,1]

    outfile = codecs.open(output, 'w', encoding="utf_8")
    print >> outfile, "topic\tparagraph_idx\tsentence_idx\tcomp1\tcomp2\tcomp1_sklearn\tcomp2_sklearn\tsentence"
    for idx in range(len(combined_wiki_df)):
        topic = combined_wiki_df.iloc[idx,3]
        sentence = combined_wiki_df.iloc[idx,1]
        sentence_idx = combined_wiki_df.iloc[idx,2]
        paragraph_idx = combined_wiki_df.iloc[idx,0]
        comp1 = combined_wiki_df.iloc[idx,4]
        comp2 = combined_wiki_df.iloc[idx,5]
        comp1_sklearn = combined_wiki_df.iloc[idx,6]
        comp2_sklearn = combined_wiki_df.iloc[idx,7]
        try:
            print >> outfile, "%s\t%d\t%d\t%1.3f\t%1.3f\t%1.3f\t%1.3f\t%s" % \
            (topic, paragraph_idx, sentence_idx, comp1, comp2, comp1_sklearn, comp2_sklearn, sentence.replace("\t", " ").replace("'",""))
        except Exception, e:
            pdb.set_trace()
            dummy = 1
