Playing with visualisation of skip-thought vectors and LSTM stuff.

# Installation

Run these steps before running `pip install` on the working copy:

```
conda install -y numpy
conda install -y scipy
conda install -y pandas
pip install git+https://github.com/tomwhi/skip-thoughts.git
```

# Running
Example:

```
python /path/to/process_topics.py --topics-str="Tokyo,Kyoto,koala,platypus,Jackie Mclean,Kenny Garrett" --output="SentenceData.txt"
Rscript /path/to/vis_vectors.R SentenceData.txt SentenceViz
```