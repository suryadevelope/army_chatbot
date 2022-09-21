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


class ActionCurrentTemperature(Action):

    def name(self) -> Text:
        return "action_data_from_pdf"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name_slot = tracker.get_slot("name").lower()
        type_slot = tracker.get_slot("type").lower()

        print(name_slot)
        print(type_slot)


        with open('./assets/foo.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            message = "no message"
            for row in reader:
                if(row['Name'].lower() == name_slot.lower()):
                    # print(row['Age'])
                    if(type_slot.find("date of birth") !=-1 or type_slot.find("dob")!=-1):
                        print(row['Age'])
                        message = "The age of {} is {} years".format(name_slot, row['Age'])

                    elif(type_slot.find("details")!=-1):
                        message = "The Details of {} are as below \n name:{} \n Position{} \n Office: {} \n Salary: {} ".format(name_slot, name_slot,row['Position'],row['Office'],row['Salary'],row['Age'])

                        print(message)

                    dispatcher.utter_message(
                        text="Well, {}".format(message))

        return [SlotSet("name", None),SlotSet("type", None)]


