# Sentiment Analysis - NLP Model

In this section all the scripts, datasets and models related to the NLP model can be found.

We implement the workflow for both a local Unix machine and with a Google Colab Virtual Machine (VM). If you are interested in working with a Google Colab VM you can follow [this jupyter notebook](https://github.com/enriquemondragon/MySafetyNet/blob/main/model/dataprep_train_test.ipynb).

If you wish to run it locally you can create a virtual environment and install the requirements:
```
    $ python3 -m venv snet_venv
    $ source snet_venv/bin/activate
    $ pip install -r requirements_modelmaker.txt

```
We trained our model using the [Tweet Sentiment Extraction dataset](https://www.kaggle.com/competitions/tweet-sentiment-extraction/data?select=train.csv), which consists of twitter posts labeled as positive, neutral or negative. We took only the text column, as well as the sentiment one, changing the values to numbers from 0 to 1.
The preprocessed step can be done with the script:
```
    $ python3 preprocess.py --input path/to/the/dataset --output output/path/

```

Model training, quantization and conversion can be done using the script:
```
    $ python3 training.py --train train/data \
    --valid valid/data --test test/data --model {NLP_model} \
    --epochs {N} --output output/path/ 

```
