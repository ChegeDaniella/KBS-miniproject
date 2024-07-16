import sqlite3

# Connect to the database
conn = sqlite3.connect('hardware_knowledge_base.db')
cursor = conn.cursor()

# Function to get knowledge
def get_knowledge(question):
    cursor.execute("SELECT answer FROM knowledge WHERE question LIKE ?", ('%' + question + '%',))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return "I'm not sure about that. Please check your device's manual or contact support."

def get_response(user_input):
    response = get_knowledge(user_input)
    return response

def main():
    print("Welcome to the Hardware Help Chatbot!")
    print("Type your question below (type 'exit' to quit):")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
