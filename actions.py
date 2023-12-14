import csv
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


file_path  = r"D:\RASA\user_data.xlsx"
class ActionHesitantSmallTalk(Action):
    def name(self) -> Text:
        return "action_hesitant_small_talk"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_hesitant_small_talk")
        return []

class ActionProvideDetails(Action):
    def name(self) -> Text:
        return "action_provide_details"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_provide_details")
        return []

class ActionExtractName(Action):
    def name(self) -> Text:
        return "action_extract_name"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        dispatcher.utter_message(text=f"The name extracted is: {name}")

        # Save data to CSV file
        csv_file_path = file_path
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, "", "", "", ""])

        return []

class ActionExtractPhoneNumber(Action):
    def name(self) -> Text:
        return "action_extract_phone_number"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        phone_number = tracker.get_slot("phone_number")
        dispatcher.utter_message(text=f"The phone number extracted is: {phone_number}")

        # Save data to CSV file
        csv_file_path = file_path 
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["", phone_number, "", "", ""])

        return []

# Similar classes for other extraction actions (email, address, date_of_birth, education)...

class ActionExtractEmail(Action):
    def name(self) -> Text:
        return "action_extract_email"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        email = tracker.get_slot("email")
        dispatcher.utter_message(text=f"The email extracted is: {email}")

        # Save data to CSV file
        csv_file_path = file_path 
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["", "", "", email, ""])

        return []

# Similar classes for other extraction actions (address, date_of_birth, education)...

class ActionExtractAddress(Action):
    def name(self) -> Text:
        return "action_extract_address"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        address = tracker.get_slot("address")
        dispatcher.utter_message(text=f"The address extracted is: {address}")

        # Save data to CSV file
        csv_file_path = file_path 
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["", "", address, "", ""])

        return []

class ActionExtractDateOfBirth(Action):
    def name(self) -> Text:
        return "action_extract_date_of_birth"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        date_of_birth = tracker.get_slot("date_of_birth")
        dispatcher.utter_message(text=f"The date of birth extracted is: {date_of_birth}")

        # Save data to CSV file
        csv_file_path = file_path 
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["", "", "", "", date_of_birth])

        return []

class ActionExtractEducation(Action):
    def name(self) -> Text:
        return "action_extract_education"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        education = tracker.get_slot("education")
        dispatcher.utter_message(text=f"The education extracted is: {education}")

        # Save data to CSV file
        csv_file_path = file_path 
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["", "", "", "", education])

        return []


