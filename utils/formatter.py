import re

def format_test_case_output(text):
    text = re.sub(r'(Test Case\s*\d+:)', r'<br><b>\1</b>', text)
    text = re.sub(r'(\n-)', r'<br>&bull;', text)
    text = re.sub(r'(\n\d+\.)', r'<br>\1', text)
    return text.replace('\n', '<br>')
