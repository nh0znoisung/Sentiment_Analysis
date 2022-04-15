from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from tkinter import *

# Ref:
# https://www.geeksforgeeks.org/sentiment-detector-gui-using-tkinter-python/
# https://coderspacket.com/sentiment-analysis-gui-using-vadersentiment-in-python

def detect_sentiment():
    sentence = file_label.get("1.0", "end")
    sentence = sentence.strip()
    # print(sentence.strip())

    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence)
 
    str_neg = str(sentiment_dict['neg']*100) + "%"
    str_neu = str(sentiment_dict['neu']*100) + "%"
    str_pos = str(sentiment_dict['pos']*100) + "%"

    senti_label.configure(text="\n\nPositive Sentiment: "+ str_pos+
                            "\n\nNeutral Sentiment: " + str_neu +
                            "\n\nNegative Sentiment: "+ str_neg +"\n\n")
     
    # decide sentiment as positive, negative and neutral
    compound = sentiment_dict['compound']
    if(compound>=0.05):
        overall_label.configure(text="Overall Sentiment is Positive",bg="#28a745",fg="yellow")
    elif(compound<=-0.05):
        overall_label.configure(text="Overall Sentiment is Negative",bg="#dc3545", fg="white")
    else:
        overall_label.configure(text="Overall Sentiment is Neutral",bg="#ffc107",fg="#212529")
 

bg_col = "#f2f2f2"


# sentence was rated as: 100% Negative
 
if __name__ == "__main__" :
    gui = Tk()
    gui.config(background = bg_col)
    gui.title("Sentiment Detector")
    gui.geometry("400x450")
    gui.resizable(width=False, height=False)


    file_label_frame = LabelFrame(gui, text="Enter Your Sentence:", bg = "white", bd=5, width=200, height=50)
    file_label_frame.pack(side=TOP)
    file_label = Text(file_label_frame, font="Times", width=220, height=6, bg="white")
    file_label.pack()



    Label(gui,text="\n", font=("Arial", 11), bg = bg_col).pack()

    sentiment_btn = Button(gui,text="Sentiment Analyzer", bg="red", fg='white', command = detect_sentiment , font=("Arial", 13))
    sentiment_btn.pack()

    senti_label = Label(gui,text="\n\nPositive Sentiment: None"+
                            "\n\n Neutral Sentiment: None"+
                            "\n\nNegative Sentiment: None", font=("Arial", 11), bg = bg_col)

    senti_label.pack()

    overall_label = Label(gui,text="\nOverall Sentiment: None", font=("Arial", 16))
    overall_label.pack()

    gui.mainloop()
    