# Abstractive-Text-Summarizer

Datasets:

Facebook/bart-large-cnn dataset

Python Libraries :
Flask module
Jinja library
Urllib standard library

Language Models: 

API_URL = "https://api-inference.huggingface.co/models/lidiya/bart-large-xsum-samsum"

![image](https://user-images.githubusercontent.com/70998986/198878001-2d36b4c5-79af-4a05-bc6b-4c5eba982c98.png)

The Abstractive Summarizer is made by using the bart data model.

Initially the bart model is worked upon with an input data. The input data is given by the user using the Jinja Library which allows the system to interact with both backend as well as frontend framework.

Once the input is given, the text undergoes various stages of transformations, they are:

1.The text preprocessing is done in which the bag of encoders separate out the words from the text irrespective of the context and relation with the neighbouring sentences.

2.Convolutional Encoder is used to setup a library of words which relate to the original text and support them as to build a new type of neural network which gives importance to sequence information, which somehow retains and leverages the sequence information.

The Attention based processing merges the words with their relating conjunctional words and a meaning is given to the sentence. And finally the summary is generated
