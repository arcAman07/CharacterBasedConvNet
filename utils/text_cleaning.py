def lower(text):
    return text.lower()

def remove_hashtags(text):
    clean_text = re.sub(r"#[A-Za-z0-9_]+", "", text)
    return clean_text

def remove_user_mentions(text):
    clean_text = re.sub(r"@[A-Za-z0-9_]+", "", text)
    return clean_text

def remove_urls(text):
    clean_text = re.sub(r"^https?:\/\/.*[\r\n]*", "", text, flags=re.MULTILINE)
    return clean_text