# Email/SMS Spam Classifier (Binary Classification Problem)

# Overview

This project is a web-based application designed to classify Email/SMS messages as **SPAM** or **NOT SPAM** using machine learning models. The project is deployed on Render and utilizes a voting ensemble model combining Multinomial Naive Bayes and ExtraTreesClassifier, achieving 100% precision and 98.55% accuracy.

# Business Use Case

## Problem Statement:

Email and SMS platforms face a significant challenge in managing and filtering out spam messages. These unsolicited messages not only clutter inboxes but also pose security risks, including phishing attempts and malware distribution. Traditional spam filters often fail to achieve high precision, leading to either false positives (important emails marked as spam) or false negatives (spam emails reaching the inbox).

## Business Use Case:

A corporate email service provider wants to integrate a robust spam classification system to enhance the security and productivity of its users. The system should ensure that legitimate emails are not incorrectly marked as spam, while effectively filtering out all actual spam messages.

## Solution:

The Email/SMS Spam Classifier leverages a voting ensemble model combining Multinomial Naive Bayes and ExtraTreesClassifier to achieve high accuracy and precision. This system can be integrated into the corporate email service to provide reliable spam detection and improve the overall user experience.

## How This System Solves the Problem:

1. **High Precision and Accuracy:** The ensemble model, which combines Multinomial Naive Bayes and ExtraTreesClassifier, achieves 100% precision and 98.55% accuracy. This ensures that the system reliably filters out spam messages while minimizing false positives, thereby maintaining user trust and satisfaction.

2. **Enhanced Security:** By accurately identifying and filtering spam messages, the system helps prevent phishing attempts, malware distribution, and other security threats. This enhances the overall security of the email and SMS platforms.

3. **Improved Productivity:** With effective spam filtering, users spend less time managing unwanted messages and more time on productive tasks. This leads to increased efficiency and a better user experience.

4. **Scalability and Integration:** The system is built using Python and Flask, making it easily deployable on various cloud platforms. It can be integrated into existing email and messaging systems with minimal modifications, ensuring a seamless transition.

5. **User-Friendly Interface:** The web-based application provides a simple interface where users can input SMS messages and receive instant predictions. This makes it easy for users to understand and utilize the spam classification system.

## Implementation in a Corporate Email Service:

1. **Integration:** The corporate email service integrates the spam classifier into its infrastructure. This involves setting up the Flask application and ensuring secure communication between the email server and the classifier.

2. **Real-Time Spam Detection:** The classifier processes incoming emails and SMS messages in real-time, using the pre-trained models to classify each message as either spam or not spam. This ensures that spam messages are filtered out before they reach the user's inbox.

3. **Continuous Monitoring and Updates:** The email service continuously monitors the performance of the spam classifier and updates the model as needed. This ensures that the system remains effective against new types of spam messages.

4. **User Feedback Loop:** Users can provide feedback on the accuracy of the spam classification. This feedback is used to further refine the models, improving their performance over time.

5. **Reporting and Analytics:** The system provides detailed reports and analytics on spam detection rates, false positives, and false negatives. This information helps the email service provider understand the effectiveness of the spam classifier and make data-driven decisions for further improvements.

By implementing the Email/SMS Spam Classifier, the corporate email service can significantly enhance the security and productivity of its users, providing a reliable and efficient solution for spam detection.

# Deployment

The application is deployed on a Cloud Platform `Render`.

You can access the application using the given Deployment Link: Email Spam Classifier


# Features

- Text preprocessing with spaCy
- TF-IDF vectorization of input text
- Multiple machine learning models for spam classification
- Ensemble model for improved accuracy
- JSON-based API for predictions
- User-friendly web interface

# Prerequisites

- Python 3.7 or higher
- Flask
- spaCy and its English model (en_core_web_md)
- scikit-learn
- pickle

# Installation

### Clone the repository:

```
git clone https://github.com/yourusername/spam-classifier.git
cd spam-classifier
```

### Install required packages:

```python
pip install -r requirements.txt
```

### Download and install spaCy English model:

```python
python -m spacy download en_core_web_md
```

### Usage:

1. Start the Flask app:

```python
python app.py
```

2. Access the application at http://0.0.0.0:8000.

# Project Details

### Project Structure:

1. `Dataset`:

   - spam.csv: The dataset used for training and testing the models.
2. `static`:

   - Background image and style.css: Static files for the web application's appearance.
3. `templates`:

   - `index.html`: The main HTML file for the web application's interface.
4. `application.py`: The main Flask application script.
5. `dockerfile`: Docker configuration file for containerizing the application.
6. `requirements.txt`: List of dependencies required for the project.
7. `email_spam_detector.ipynb`: Jupyter notebook for model training and experimentation.

### Functions and Their Purpose:

- `transform_text(text)`: Preprocesses the input text by converting to lowercase, tokenizing, removing stopwords and punctuation, and lemmatizing the tokens.
- `Flask route home()`: Handles GET and POST requests for the home page, processes input SMS, vectorizes it, and returns the prediction.

### Model Training and Experimentation:

The model was first trained using Naive Bayes and then Multinomial Naive Bayes, which achieved 100% precision. Further experimentation involved various models, including:

- **Logistic Regression**
- **SVC**
- **Decision Tree Classifier**
- **K-Nearest Neighbors**
- **Random Forest Classifier**
- **AdaBoost Classifier**
- **Bagging Classifier**
- **ExtraTreesClassifier**
- **Gradient Boosting Classifier**
- **XGBoost Classifier**

Finally, a `Voting Ensemble` was created with `Multinomial Naive Bayes` and `ExtraTreesClassifier`, which improved the model accuracy further while maintaining 100% precision. This extensive experimentation ensures the robustness and reliability of the spam classifier.

## How to Use the Application:

- Open the application in your browser.
- Enter an SMS message in the input field.
- Click the "Predict" button.
- View the prediction result indicating whether the message is **SPAM** or **NOT SPAM**.


# Contributing

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Create a new Pull Request.

# License

This project is licensed under the `MIT` License.
