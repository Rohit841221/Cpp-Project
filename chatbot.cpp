#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

// Function to convert string to lowercase for easy matching
string toLowerCase(string str) {
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    return str;
}

// Function to get chatbot response
string getResponse(string userInput) {
    string input = toLowerCase(userInput);  // convert input to lowercase

    if (input == "hi" || input == "hello") {
        return "Hello! How can I help you?";
    } 
    else if (input == "how are you") {
        return "I'm just a bot, but I'm doing great! What about you?";
    }
    else if (input == "what is your name") {
        return "I am ChatBot, your virtual assistant.";
    }
    else if (input == "bye" || input == "exit") {
        return "Goodbye! Have a great day.";
    }
    else if (input.find("name") != string::npos) {
        return "I'm ChatBot, your friend!";
    }
    else if (input.find("time") != string::npos) {
        return " Sorry I don't have a watch, but you can check your system clock!";
    }
    else {
        return "Sorry, I didn't understand that.";
    }
}

int main() {
    string userInput;
    cout << "Welcome to Simple ChatBot! Type 'bye' to exit.\n\n";

    while (true) {
        cout << "You: ";
        getline(cin, userInput);

        // Exit condition
        if (toLowerCase(userInput) == "bye" || toLowerCase(userInput) == "exit") {
            cout << "Bot: " << getResponse(userInput) << endl;
            break;
        }

        // Bot response
        cout << "Bot: " << getResponse(userInput) << endl;
    }

    return 0;
}