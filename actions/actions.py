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

        name_slot = tracker.get_slot("name")
        type_slot = tracker.get_slot("type")

        print(name_slot.lower())
        print(type_slot.lower())


        with open('./assets/foo.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            message = "no message"
            for row in reader:
                if(row['NAME'].lower() == name_slot.lower()):
                    # print(row['Age'])
                    if(type_slot.find("army number") !=-1):
                        print(row['ARMY NO'])
                        message = "The army number of {} is {} ".format(name_slot, row['ARMY NO'])

                    elif(type_slot.find("details")!=-1):
                        message = "The Details of {} are as below \n name:{} \n Army no:{} \n Rank: {} \n Mobile no: {} ".format(name_slot, name_slot,row['ARMY NO'],row['RANK'],row['MOB NO'])

                        print(message)
                    elif(type_slot.find("rank")!=-1):
                        print(row['RANK'])
                        message = "The Rank of {} is {} ".format(name_slot, row['RANK'])
                    elif(type_slot.find("mobile")!=-1 or type_slot.find("mobile number")!=-1):
                        print(row['MOB NO'])
                        message = "The Mobile number of {} is {} ".format(name_slot, row['MOB NO'])

                    dispatcher.utter_message(
                        text="Well, {}".format(message))

        return [SlotSet("name", None),SlotSet("type", None)]


