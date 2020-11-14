from pymongo import MongoClient 
import re
from Connection import Connection
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
stop_words=set(stopwords.words('english'))
lemma=WordNetLemmatizer()

#data cleaning using NLP after removing the missing data using mongo Shell
class Data_Cleaning :
    def __init__(self,dbName,collectionName):
        self.connection=Connection(dbName,collectionName)
    
    def clean(self,review_text):
    review_text=re.sub(r'http\S+','',review_text)#remove urls
    review_text=re.sub('[^a-zA-Z]',' ',review_text)#remove non alpha letters
    review_text=str(review_text).lower()#transform all letters to lowercases
    review_text=word_tokenize(review_text)
    review_word=[item for item in review_text if item not in stop_words]#remove the stopwords
    review_text=[lemma.lemmatize(word=w,pos='v') for w in review_text]
    review_text=[i for i in review_text if len(i) > 2]#remove the words having less than 3 letters
    review_text =' '.join(review_text)#from list to string
    return review_text

    def content_cleaning(self):
        exclude_data = {'_id': False, 'attackers': False, 'items': False}
        raw_data = listself.connection.find({}, projection=exclude_data))
        df =  pd.DataFrame(raw_data)
        df['clean_content']=df['content'].apply(self.clean)
        urls=df['topicUrl'] #the topic Urls
        j=0 #iterator for the topicUrls
        for i in df['clean_content']:
            collection.update_one({"topicUrl": urls[j]}, {"$set": {"clean_content": i}})
            j=j+1
            
    def comments_cleaning(self):
        exclude_data = {'_id': False, 'attackers': False, 'items': False}
        raw_data = list(self.connection.find({"comments":{'$ne':None}}, projection=exclude_data))
        df =  pd.DataFrame(raw_data)
        urls=df['topicUrl'] #projection on topicUrl
        url1=urls[0]
        k=0
        for i in df['comments']:
            url1=urls[k]
            myquery = {'topicUrl':url1} 
            clean_comments = [self.clean(x) for x in i]
            for j in clean_comments:
                newvalues = {"$push":{'clean_comments':j}}
                collection.update_one(myquery, newvalues)
            k=k+1



    
    

    