import MeCab

def macab_appearances(text):
    mecab = MeCab.Tagger('-d /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd')
    # mecab = MeCab.Tagger()

    noun_count = {}
    node = mecab.parseToNode(text)
    total_nouns = 0
    while node:
        word = node.surface
        hinshi = node.feature.split(",")[0]
        if word in noun_count.keys() and hinshi == "名詞":
            noun_freq = noun_count[word]
            noun_count[word] = noun_freq + 1
            total_nouns += 1
        elif hinshi == "名詞":
            noun_count[word] = 1
            total_nouns += 1
        else:
            pass
        node = node.next
        
    noun_percentage = {noun: (count / total_nouns) * 100 for noun, count in noun_count.items()}
    sorted_noun_percentage = sorted(noun_percentage.items(), key=lambda x: x[1], reverse=True)
    
    # Convert the sorted list of tuples into a string
    result_str = ', '.join([f"{noun}: {percentage:.2f}%" for noun, percentage in sorted_noun_percentage])
    return result_str

def get_noun_appearances(input_file_path, output_file_path):
    with open(input_file_path, "r", encoding="utf-8") as file:
        text = file.read()
    
    result = macab_appearances(text)
    
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(result)

input_file_path = 'Path_of_Removed_stopWords_text'
output_file_path = 'Path_of_Result_text'

get_noun_appearances(input_file_path, output_file_path)

print(f'Appearance result has been saved to {output_file_path}')    