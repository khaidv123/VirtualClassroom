import time
import uuid
import json
import re


def get_timestamp():
    return int(time.time() * 1000)

def generate_uuid():
    return str(uuid.uuid4())

def clean_response(raw_response):
    """Handling special characters"""
    cleaned = re.sub(r'```(json)?', '', raw_response)
    cleaned = cleaned.replace('\r\n', '\n').replace('\r', '\n')
    cleaned = re.sub(
        r'(?<!\\)\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', 
        r'\\\\', 
        cleaned
    )
    return cleaned.strip()

def parse_json_response(cleaned_response):
    """Process and validate JSON response"""
    try:
        return json.loads(cleaned_response)
    except json.JSONDecodeError:
        start = cleaned_response.find('{')
        end = cleaned_response.rfind('}')
        if start != -1 and end != -1:
            try:
                return json.loads(cleaned_response[start:end+1])
            except:
                pass
        return None

def process_content(content):
    """Convert markdown format to HTML"""
    content = re.sub(r'(\d+\.)\s', r'<span class="list-number">\1</span> ', content)
    content = re.sub(r'•\s', r'<span class="list-bullet">•</span> ', content)
    
    content = re.sub(r'\\sqrt(\w+)', r'\\sqrt{\1}', content)
   
    content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
    
    content = re.sub(r'\$(?! )', '$ ', content)
    content = re.sub(r'(?<! )\$', ' $', content)
    
    content = re.sub(r'\n\s{2,}', lambda m: '\n' + ' ' * (len(m.group(0))//2), content)
    
    bullet_replacements = {'◦': '○', '■': '▪', '‣': '▸'}
    for k, v in bullet_replacements.items():
        content = content.replace(k, v)
    
    return content
    
def parse_output(content):
    cleaned_response = clean_response(content)

    response_data = parse_json_response(cleaned_response)

    bot_response = process_content(response_data.get("spoken_message", ""))
    return bot_response
