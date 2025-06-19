from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

def load_chatbot(model_name="google/flan-t5-base"):
    print("Loading model:", model_name)

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    chatbot = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    return chatbot
