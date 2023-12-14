# GetThatData

# Ai assistant for extracting data

This project is a conversational chatbot developed using Rasa, designed to initiate and guide users through providing personal information. The chatbot employs custom actions to extract details such as name, email, phone number, address, date of birth, and education.


## Requirements

Ensure you have the following software installed:

- [Rasa](https://rasa.com/docs/rasa/installation)
- Python 3.x


## Files and Directories
data/: Contains training data for Rasa.
actions/: Contains custom action code.
endpoints.yml: Configuration file for action server endpoint.
config.yml: Rasa configuration file.
domain.yml: Contains the domain configuration.
stories/: Contains user stories for training.
README.md: You are here!

## Installation

1. Clone the repository:
https://github.com/maittreyy/GetThatData.git)https://github.com/maittreyy/GetThatData.git

Steps:

1) Navigate to the project directory:
  cd your-chatbot-repo
  Start Virtual environment

2) Installation
  pip install -r requirements.txt

3) Starting rasa.
  `rasa init`

(Please change the codes manually for the following files by copying from my repo, as I was unable to do it in github:
  Domain.yml, Stories.yml, Rules.yml etc
## Running the Chatbot

1. **Train the Rasa model:**
   - Execute the command: `rasa train`

2. **Start the Rasa server:**
   - Execute the command: `rasa run --endpoints endpoints.yml`

3. **Start the Rasa Action server:**
   - Open a new terminal.
   - Execute the command: `rasa run actions`

4. **Interact with the chatbot:**
   - Open another terminal.
   - Run Rasa shell: `rasa shell`
    

