# NLP-Corpus-Analysis-Japanese

1. **Download language corpora from** [Wikipedia Dump](https://dumps.wikimedia.org/jawiki/)
2. **Installign Mecab**
- For MacOS, install Homebrew first, then:
   ```bash
   brew install mecab
   brew install mecab-ipadic
   ```
- Check the installation place of neologd library
  ```bash
  echo `mecab-config --dicdir`"/mecab-ipadic-neologd"
  ```
  output:  
  /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd  
- Example usage
  ```bash
  echo ”推し活” | mecab -d /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd
  echo ”推し活” | mecab
  ```
 You will notice the difference and accuracy of these outputs  

3. **Extract sentences from XML file using** [Wikipedia Dump Extractor](https://github.com/attardi/wikiextractor)
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

5. Normalization the extracted sentences
  - Remove XML tags
  - Unicode normalization
  - Replace multiple spaces with a single space
  - Normalize with the neologdn library
  - Replace numbers with 0
  - Covert all letters to lowercase  
  Reference:
  [Normalization_codes](https://github.com/Hironsan/natural-language-preprocessings/blob/master/preprocessings/ja/normalization.py)

5. Remove stop words by segmenting text into words
6. Perform morphological analysis on the text file and output the appearance rate of each word

