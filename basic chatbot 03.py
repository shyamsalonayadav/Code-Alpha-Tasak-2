import random

def get_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm good, thanks!", "Doing well, how about you?", "I'm a chatbot, so I don't have feelings, but thanks for asking!"],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "default": ["I'm not sure how to respond to that.", "Could you please rephrase that?", "I didn't understand."]
    }

    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the input matches any predefined responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # If no match is found, return a default response
    return random.choice(responses["default"])

# Simple loop to keep the chatbot running
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)