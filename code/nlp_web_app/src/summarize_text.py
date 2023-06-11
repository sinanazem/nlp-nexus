from transformers import pipeline


def summarize_BART(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", truncation=True)
    summarize_list_of_dict = summarizer(text, max_length=1000, min_length=30, do_sample=False)
    return summarize_list_of_dict[0]['summary_text']