import pandas as pd
import unicodedata
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


excel_workbook = 'Test.xlsx'
df = pd.read_excel(excel_workbook,sheet_name='Sheet1')

print(df['news_text_content'].head(10))

#Removes all unwanted characters
df['news_text_content'] = df['news_text_content'].str.replace(r'\W'," ", regex=True)
#Removes all accents
df['news_text_content'] = df['news_text_content'].apply(strip_accents)
#Tokenize every word, separte by commas
df['news_text_content'] = df['news_text_content'].apply(word_tokenize)

print(df['news_text_content'].head(10))







