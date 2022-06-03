def lower(text):
    return text.lower()

def remove_hashtags(text):
    clean_text = re.sub(r"#[A-Za-z0-9_]+", "", text)
    return clean_text
