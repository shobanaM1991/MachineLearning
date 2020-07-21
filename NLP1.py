#Natural Language Processing Excercise 1
import nltk
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#nltk.download_shell()  
messages = [line.rstrip() for line in open('SMSSpamCollection')]
#print(len(messages))
#print(messages[50])
for mess_no, message in enumerate(messages[:10]):
    print(mess_no, message)
    print('\n')
messages = pd.read_csv('SMSSpamCollection', sep = '\t', names=['label', 'message'])
#print(messages.groupby('label').describe())
#create a new column in dataframe 'messages ' to count the length of each messages
messages['length'] = messages['message'].apply(len)
#print(messages['length'].describe())
messages['length'].plot.hist(bins = 150)
#print(messages[messages['length'] == 910]['message'].iloc[0])
messages.hist(column = 'length', by = 'label', bins = 60, figsize = (12,4))
#plt.show()
import string
mess = 'Sample message! Notic: it has punctuaion'
nopunc = [c for c in mess if c not in string.punctuation]
#print(nopunc)
from nltk.corpus import stopwords
nopunc = ''.join(nopunc) 
#print(nopunc)
#print(nopunc.split()) 
clean_mess = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

#print(clean_mess) 

def text_process(mess):
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if nopunc.lower() not in stopwords.words('english')]

#print(messages['message'].head().apply(text_process))
from sklearn.feature_extraction.text import CountVectorizer
bow_transformer = CountVectorizer(analyzer=text_process).fit(messages['message'])
#print(len(bow_transformer.vocabulary_))
mess4 = messages['message'][3]
#print(mess4)
bow4 = bow_transformer.transform([mess4])
#print(bow4)
#print(bow4.shape)
#print(bow_transformer.get_feature_names()[9832]) 

message_bow = bow_transformer.transform(messages['message'])
print('shape of Sparse Matrix:', message_bow.shape)
print(message_bow.nnz)  

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
tfidf_transformer.fit(message_bow)
tfidf4 = tfidf_transformer.transform(bow4)
print(tfidf4)
tfidf_transformer.idf_[bow_transformer.vocabulary_['university']]
message_tfidf = tfidf_transformer.transform(message_bow)
from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB()
spam_detect_model.fit(message_tfidf, messages['label'])
spam_detect_model.predict(tfidf4[0])