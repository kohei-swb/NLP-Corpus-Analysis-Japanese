import re
import xml.etree.ElementTree as ET
import os

def extract_and_save_body_sentences(input_file_path, output_dir):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all <doc>...</doc> blocks
    doc_blocks = re.findall(r'<doc.*?>.*?</doc>', data, re.DOTALL)
    
    for doc in doc_blocks:
        # Parse the <doc> block
        root = ET.fromstring(doc)
        
        # Get the id attribute
        doc_id = root.get('id')
        
        # Extract the body text (everything except the <doc> tag and its attributes)
        body_text = root.text
        
        if doc_id and body_text:
            # Create a filename based on the id attribute
            output_file_path = os.path.join(output_dir, f'doc_{doc_id}.txt')
            
            # Write the body sentences to the output file
            with open(output_file_path, 'w', encoding='utf-8') as file:
                sentences = body_text.split('\n')
                for sentence in sentences:
                    stripped_sentence = sentence.strip()
                    if stripped_sentence:
                        file.write(stripped_sentence + '\n')
            
            print(f"Extracted sentences from doc id {doc_id} have been saved to {output_file_path}")

input_file_path = '/Users/kohei/Documents/Precision_task/extracted_sentences/AA/wiki_00'
output_dir = '/Users/kohei/Documents/Precision_task/list_of_titles'

extract_and_save_body_sentences(input_file_path, output_dir)
