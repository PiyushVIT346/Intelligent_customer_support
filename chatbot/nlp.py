import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def process_user_message(message, model):
    # Dummy processing - replace with actual model inference
    doc = nlp(message)
    response = "I am not sure how to respond to that."
    if "support" in message.lower():
        response = "How can I assist you with your support request?"
    elif "product" in message.lower():
        response = "Please provide more details about the product."
    return response
