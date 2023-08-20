import tkinter as tk
import nltk                                      # pip install nltk
from textblob import TextBlob                    # pip install textblob
from newspaper import Article                    # pip install newspaper3k

def summarize():    
# nltk.download('punkt')

# url = "https://indianexpress.com/article/technology/science/russia-luna-25-crashes-moon-failure-8900854/"
    url = utext.get('1.0',"end").strip()
    article = Article(url)
    article.download()
    article.parse()

    article.nlp()

    # print(f'Title : {article.title}')
    # print(f'Authors : {article.authors}')
    # print(f'Publication Date : {article.publish_date}')
    # print(f'Summary : {article.summary}')
    
    title.config(state="normal")
    author.config(state="normal")
    publish_date.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")
    
    title.delete('1.0','end')
    title.insert('1.0',article.title)
    
    author.delete('1.0','end')
    author.insert('1.0',article.authors)
    
    publish_date.delete('1.0','end')
    publish_date.insert('1.0',article.publish_date)
    
    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)
    
    analysis = TextBlob(article.text)
    sentiment.delete('1.0','end')
    sentiment.insert('1.0',f'Polarity: {analysis.polarity},Sentiment:{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
    
    #disabled so that user cannot change the content
    title.config(state="disabled")
    author.config(state="disabled")
    publish_date.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")
    

   

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

#title
tlabel = tk.Label(root,text='Title')
tlabel.pack()

title=tk.Text(root,height=1,width=140)
title.config(state='disabled',bg='#bddddd')
title.pack()

#author
alabel = tk.Label(root,text='Author')
alabel.pack()

author=tk.Text(root,height=1,width=140)
author.config(state='disabled',bg='#bddddd')
author.pack()

#Publication Date
plabel = tk.Label(root,text='Publication Date')
plabel.pack()

publish_date=tk.Text(root,height=1,width=140)
publish_date.config(state='disabled',bg='#bddddd')
publish_date.pack()

#Summary
slabel = tk.Label(root,text='Text Summary')
slabel.pack()

summary=tk.Text(root,height=20,width=140)
summary.config(state='disabled',bg='#bddddd')
summary.pack()

#Sentiment 
selabel = tk.Label(root,text='Sentiment')
selabel.pack()

sentiment=tk.Text(root,height=1,width=140)
sentiment.config(state='disabled',bg='#bddddd')
sentiment.pack()

#URL
ulabel = tk.Label(root,text='URL')
ulabel.pack()

utext=tk.Text(root,height=1,width=140)
utext.pack()

btn = tk.Button(root, text="Summarize",command=summarize)
btn.pack()

root.mainloop()
