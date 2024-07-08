import MeCab

def morphological_analysis(text):
    mecab = MeCab.Tagger('-Owakati -d /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd')
    processed = mecab.parse(text)
    return processed

def segment_text_file(input_file_path, output_file_path):
    with open(input_file_path, "r", encoding="utf-8") as file:
        text = file.read()
        
    segmented_text = morphological_analysis(text)
    
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(segmented_text)

input_file_path = 'Path_of_Normalized_text'
output_file_path = 'Path_of_Segmented_text'

segment_text_file(input_file_path, output_file_path)

print(f"Segmented text has been saved to {output_file_path}")
