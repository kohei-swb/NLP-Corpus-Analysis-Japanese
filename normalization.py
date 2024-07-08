import re
import unicodedata
import neologdn

# Function to normalize text
def normalize_text(text):
    text = re.sub(r'<.*?>', '', text)  # Remove XML/HTML tags
    text = re.sub(r'\s+', ' ', text).strip()  # Replace multiple spaces with a single space and trim
    text = neologdn.normalize(text)  # Additional normalization with neologdn
    text = normalize_unicode(text)  # Unicode normalization
    text = normalize_number(text)  # Normalize numbers
    text = lower_text(text)  # Convert to lowercase
    return text

def normalize_unicode(text, form='NFKC'):
    return unicodedata.normalize(form, text)

def normalize_number(text):
    # Replace consecutive digits with '0'
    return re.sub(r'\d+', '0', text)

def lower_text(text):
    return text.lower()

def normalize_text_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    normalized_text = normalize_text(text)
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(normalized_text)
        


input_file_path = 'Path_of_Extracted_text'
output_file_path = 'Path_of_Normalized_text'

normalize_text_file(input_file_path, output_file_path)

print(f"Normalized text has been saved to {output_file_path}")
