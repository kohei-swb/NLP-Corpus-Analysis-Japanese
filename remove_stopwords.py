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
        
    # Manually adding stop words
    additional_stopWords = ["いくつか", "0", "00", "000", "0パーセント", "0件", "0度", "0ユーロ", "0km", "0分", "0倍", "0ドル", "0メートル", "0mm", "0点", "00000", "の", "ら", "ころ", "および", "ap", "hp", "ド", "か月", "にも", "した", "では", "(", ")", "同国", "0回", "彼ら", "との", "しない", "ドニ", "hp", "ap", "eu", "世紀", "年", "月", "日", "時", "分", "秒", "メートル", "キロメートル", "センチメートル", "グラム", "キログラム", "リットル", "これ", "それ", "あれ", "ここ", "そこ", "あそこ", "どこ", "だれ", "何", "する", "いる", "ある", "なる", "こと", "もの"]
    
    for i in range(len(additional_stopWords)):
        stopwords.append(additional_stopWords[i])

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


