# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from bs4 import BeautifulSoup
import requests
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import tabula
import csv

tabula.convert_into("./assets/foo.pdf", "./assets/foo.csv", output_format="csv", pages='all')
with open('./assets/foo.csv') as csvfile:
     reader = csv.DictReader(csvfile)

class ActionCurrentTemperature(Action):

    def name(self) -> Text:
        return "action_data_from_pdf"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name_slot = tracker.get_slot("name")
        type_slot = tracker.get_slot("type")

            

        

        for row in reader:
        if(row['Name'] == name_slot):
            print(row['Age'])
            if(type_slot.find("date of birth") or type_slot.find("dob")):

            elif(type_slot.find("details")):

            dispatcher.utter_message(
                text="Well, the current temperature is {}".format(temp))

        return [SlotSet("name", None),SlotSet("type", None)]


