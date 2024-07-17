from flask import Flask, render_template, request, jsonify
import pickle
import string
import spacy

app = Flask(__name__)

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

def transform_text(text):
    # Lowercase the text
    text = text.lower()
    
    # Tokenize the text using spaCy
    doc = nlp(text)
    
    # Filter out stopwords and punctuation
    tokens = [token.text for token in doc if not token.is_stop and token.text not in string.punctuation]
    
    # Lemmatize tokens
    lemmatized_tokens = [token.lemma_ for token in nlp(' '.join(tokens))]
    
    # Join the lemmatized tokens into a sentence
    lemmatized_text = ' '.join(lemmatized_tokens)
    
    return lemmatized_text

# Load TF-IDF vectorizer and model
with open('models/vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        input_sms = data['input_sms']

        # Preprocess text
        transformed_sms = transform_text(input_sms)

        # Vectorize text
        vector_input = tfidf.transform([transformed_sms])

        # Predict
        prediction = model.predict(vector_input)[0]

        # Return prediction result as JSON
        return jsonify({'Prediction': 'The Message is Spam !!!!!!!' if prediction == 1 else 'The Message is Not Spam'})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
