# Cleaning the data

def cleaning_data(text):
   cleaned_text = remove_urls(remove_user_mentions(remove_hashtags(lower(text))))
   return cleaned_text