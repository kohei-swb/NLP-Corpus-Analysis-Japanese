import requests

# create list of stop words

    
def get_stopwords_list():
    url = "http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"
    r = requests.get(url)
    tmp = r.text.split('\r\n')
    stopwords = []
    for i in range(len(tmp)):
        if len(tmp[i]) < 1:
            continue
        stopwords.append(tmp[i])
    return stopwords

def remove_from_list(list_stoppingWords, text):
    text_list = text.split()
    filtered_words = [word for word in text_list if word not in list_stoppingWords]
    
    return ''.join(filtered_words)

def removing_stop_words(segment_file_path, removed_stopwords_file_path):
    with open(segment_file_path, "r", encoding="utf-8") as file:
        text = file.read()
    
    stopwords = get_stopwords_list()
    removed_stopwords_text = remove_from_list(stopwords, text)
        
        
    with open(removed_stopwords_file_path, "w", encoding="utf-8") as file:
        file.write(removed_stopwords_text)
        


segment_file_path = 'Path_of_Segmented_text'
stopwords_file_path = 'Path_of_Removed_stopWords_text'

removing_stop_words(segment_file_path, stopwords_file_path)

print(f"Removed stop words text has been saved to {stopwords_file_path}")


