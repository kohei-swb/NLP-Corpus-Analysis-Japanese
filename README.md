# NLP-Corpus-Analysis-Japanese

1. **Download language corpora from** [Wikipedia Dump](https://dumps.wikimedia.org/jawiki/)
2. **Install Mecab**
- For MacOS, install Homebrew first, then:
   ```bash
   brew install mecab
   brew install mecab-ipadic
   ```
- Check the installation location of the neologd library
  ```bash
  echo `mecab-config --dicdir`"/mecab-ipadic-neologd"
  ```
  output example:  
  /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd  
- Example usage
  ```bash
  echo ”恋ダンスを踊った。” | mecab -d /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd
  ```
  output:  
    ”	記号,括弧閉,*,*,*,*,”,”,”
    恋ダンス	名詞,固有名詞,一般,*,*,*,恋ダンス,コイダンス,コイダンス
    を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
    踊っ	動詞,自立,*,*,五段・ラ行,連用タ接続,踊る,オドッ,オドッ
    た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
    。	記号,句点,*,*,*,*,。,。,。
    ”	記号,括弧閉,*,*,*,*,”,”,” 
  ```bash
  echo ”恋ダンスを踊った。” | mecab
  ```
  output:  
    ”	記号,括弧閉,*,*,*,*,”,”,”
    恋	名詞,一般,*,*,*,*,恋,コイ,コイ
    ダンス	名詞,サ変接続,*,*,*,*,ダンス,ダンス,ダンス
    を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
    踊っ	動詞,自立,*,*,五段・ラ行,連用タ接続,踊る,オドッ,オドッ
    た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
    。	記号,句点,*,*,*,*,。,。,。
    ”	記号,括弧閉,*,*,*,*,”,”,”

From the above example, "恋ダンス" should be recognized as one word, but without library, it is recognized as two words.
  
 You will notice the difference and accuracy of these outputs  

3. **Extract sentences from XML file using** 
[Wikipedia Dump Extractor](https://github.com/attardi/wikiextractor)
   - install wikiextractor
    ```bash
    pip install wikiextractor
    ```

  - Extract sentences from XML file by wikiextractor
    ```bash
    python -m wikiextractor.WikiExtractor <Wikipedia dump file> -o <extracted template file>
    ```
    Example: 
    ```bash
    python -m wikiextractor.WikiExtractor /Users/UserName/Documents/jawiki-20240220-pages-articles-multistream.xml -o extracted_sentences
    ```
4. Extract and Save body sentences of each topic to files
[list_topics.py](https://github.com/hei8san/NLP-Corpus-Analysis-Japanese/blob/main/list_topics.py)

    **Be sure to alter:**
    - [line 39] input_file_path =
    <Path_of_Extracted_template_file>  
    - [line 40] output_file_path = <Path_of_Output_Directory>

5. **Normalize the extracted sentences**
    [normalization.py](https://github.com/hei8san/NLP-Corpus-Analysis-Japanese/blob/main/normalization.py)

    **Be sure to alter:**
    - [line 36] input_file_path = <Path_of_Extracted_text>
    - [line 37] output_file_path = <Path_of_Normalized_text>
  
    **This python script does:** 
    - Remove XML tags
    - Unicode normalization
    - Replace multiple spaces with a single space
    - Normalize with the neologdn library
    - Replace numbers with 0
    - Convert all letters to lowercase

        Reference:
        [Normalization_codes](https://github.com/Hironsan/natural-language-preprocessings/blob/master/preprocessings/ja/normalization.py)

6. Segment text into words
  [segmentation.py](https://github.com/hei8san/NLP-Corpus-Analysis-Japanese/blob/main/segmentation.py)
    **Be sure to alter:**
    - [line 17] input_file_path = <Path_of_Normalized_text>
    - [line 18] output_file_path = <Path_of_Segmented_text>

7. Remove stop words from segmented text
[remove_stopwords.py](https://github.com/hei8san/NLP-Corpus-Analysis-Japanese/blob/main/remove_stopwords.py)
    **Be sure to alter:**
    - [line 17] input_file_path = <Path_of_Segmented_text>
    - [line 18] output_file_path = <Path_of_Removed_stopWords_text>


8. Perform morphological analysis on the text file and output the appearance rate of each word  
[morphological_analysis.py](https://github.com/hei8san/NLP-Corpus-Analysis-Japanese/blob/main/morphological_analysis.py)
    **Be sure to alter:**
    - [line 40] input_file_path = <Path_of_Removed_stopWords_text>
    - [line 41] output_file_path = <Path_of_Result_text>
