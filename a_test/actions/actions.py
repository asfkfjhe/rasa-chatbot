# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

user_data = {
    "123": {"name": "Supriya", "balance": 1000, "transactions": ["Spent 1000 at bigmart"]},
    "456": {"name": "Alice Smith", "balance": 500, "transactions": ["Spent 300 at ason"]}
}

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSupplyInfo(Action):

    def name(self) -> Text:
        return "action_supply_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        print(entities)

        
        name = "Unknown"

        for e in entities:
            if e['entity'] == 'name':
                name = e['value']
                break  # If 'name' is found, no need to keep looping

        dispatcher.utter_message(response="utter_supply_info", name=name)

        return []
    

class ActionSupplyAccount(Action):

    def name(self) -> Text:
        return "action_supply_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        print(entities)

        acc_number = "Unknown"
        for e in entities:
            if e['entity'] == 'acc_number':
                acc_number = e['value']
                break


        if acc_number in user_data:
            user_info = user_data[acc_number]
            dispatcher.utter_message(response="utter_balance", acc_number=acc_number, balance=user_info['balance'])
        else:
            dispatcher.utter_message(text=f"Sorry, no information found for account number {acc_number}.")
        


        return []
    
class ActionShowHistory(Action):

    def name(self) -> Text:
        return "action_show_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        print(entities)

        if acc_number in user_data:
            user_info = user_data[acc_number]
            dispatcher.utter_message(response="utter_balance", history=user_info['transactions'])
        else:
            dispatcher.utter_message(text=f"Sorry, no information found for account number {acc_number}.")
        


        return []
    

class ActionGoodBye(Action):

    def name(self) -> Text:
        return "action_supply_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        print(entities)

        
        name = "Unknown"

        for e in entities:
            if e['entity'] == 'name':
                name = e['value']
                break  # If 'name' is found, no need to keep looping

        dispatcher.utter_message(response="utter_supply_info", name=name)

        return []