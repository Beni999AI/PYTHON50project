
import sys
import questionary
import emoji
import requests
import time
from db import get_db, save, view
from tabulate import tabulate


def main():
    while True:
    #making so that i can choose options in a menu
        answer = questionary.select(
            emoji.emojize("Choose one option:red_exclamation_mark:"),
                choices = [
                    emoji.emojize("Search for routes :airplane:"),
                    emoji.emojize("Track a specific plane :airplane_departure:"),
                    emoji.emojize("View the saved ones :books:"),
                    emoji.emojize("Exit the program :cross_mark:")
                ]).ask()

        if (emoji.emojize("Search for routes :airplane:")) == answer:
            routes()
        elif  (emoji.emojize("Track a specific plane :airplane_departure:")) == answer:
            tracking()
        elif (emoji.emojize("View the saved ones :books:")) == answer:
            #if they want to see the saved flights
            db = get_db()
            flight_code = questionary.text("Please, input the flight's IATA/ICAO number: ").ask()
            flight_data = view(db, flight_code)
            if flight_data:
                print("\n🛫 Saved Flight Details:")
                print(tabulate([flight_data], headers="keys", tablefmt="grid"))
            else:
                print("❌ No saved flight data found for that code.")
            time.sleep(2)
            main()


        elif (emoji.emojize("Exit the program :cross_mark:")) == answer:
            quitting()



def quitting():
    #if they press quit then the program exists
    sys.exit((emoji.emojize("See you soon :grinning_face:")))

def tracking():
    #receive the flight number and then receive the API response in connection with that flight
    flight_number = questionary.text("Please, input the flight's IATA/ICAO number: ").ask()
    tracking_details(flight_number)



def tracking_details(flight_code):
    API = 'a92c6540d08fd8a9adc970998bd3aeae'
    code_type = 'iata_code' if len(flight_code) <=  6 else 'icao_code'
    url = f'https://api.aviationstack.com/v1/flights?{code_type}={flight_code}&access_key={API}'
    response = requests.get(url)
    data = response.json()
    if 'data' in data and data['data']:
        flight = data['data'][0]
        print("\n🛫 Live Flight Status:")
        print(f"Airline: {flight['airline']['name']}")
        print(f"Flight: {flight['flight']['iata']} / {flight['flight']['icao']}")
        print(f"From: {flight['departure']['airport']} ({flight['departure']['iata']})")
        print(f"To: {flight['arrival']['airport']} ({flight['arrival']['iata']})")
        print(f"Scheduled Departure: {flight['departure']['scheduled']}")
        print(f"Actual Departure: {flight['departure']['actual']}")
        print(f"Scheduled Arrival: {flight['arrival']['scheduled']}")
        print(f"Actual Arrival: {flight['arrival']['actual']}")
        print(f"Status: {flight['flight_status']}")

        time.sleep(2)
        if questionary.confirm(emoji.emojize("Do you want to save this flight's info? :airplane:")).ask():
            """
            text = f"Airline: {flight['airline']['name']}@Flight: {flight['flight']['iata']} / {flight['flight']['icao']}@From: {flight['departure']['airport']} ({flight['departure']['iata']})@To: {flight['arrival']['airport']} ({flight['arrival']['iata']})@Scheduled Departure: {flight['departure']['scheduled']}@Actual Departure: {flight['departure']['actual']}@Scheduled Arrival: {flight['arrival']['scheduled']}@Actual Arrival: {flight['arrival']['actual']}@Status: {flight['flight_status']}"

            try:
                with open("live_flight_data.txt", "a") as f:
                    f.write(f"Time of saving: {time.ctime()}@{text}")
            except (FileNotFoundError, PermissionError):
                print("Something went wrong. After 5 seconds you will be redirected to the main menu!")
                time.sleep(5)
                main()
                """
            db = get_db()
            save(db, flight['flight']['iata'], flight['airline']['name'], flight['departure']['airport'], flight['arrival']['airport'], flight['departure']['scheduled'], flight['arrival']['scheduled'], flight['flight_status'])
            print("✅ Flight information saved successfully!")
            time.sleep(2)
            main()

        else:
            if questionary.confirm(emoji.emojize("Do you want to go back to the main menu? ⛔️")):
                main()
            else:
                time.sleep(60)
                main()

    else:
        print("❌ No live flight data found for that code.")


def routes():
    menu = questionary.select(
    (emoji.emojize("Choose one option:red_exclamation_mark:")),
        choices = [
            (emoji.emojize("Search specific destinations :airplane:")),
            (emoji.emojize("Go back :cross_mark:")),
            (emoji.emojize("Exit the program :cross_mark:"))
        ],).ask()
    #they are able to search for the best deals available
    if menu == (emoji.emojize("Search specific destinations :airplane:")):
        print("JO")

    #if they want to go back to the main menu
    elif menu == (emoji.emojize("Go back :cross_mark:")):
        main()

    #exits th program if they choose to
    else:
        quitting()





if __name__ == "__main__":
    main()
