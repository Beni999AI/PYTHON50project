# Aviation data and vacation planning program using API requests

#### Video demo: 

#### Description: 
Welcome to Flight Tracker & Deal Finder! This is a powerful command-line interface (CLI) application designed for aviation enthusiasts, frequent flyers, and anyone looking for the best flight deals. It provides a simple, interactive menu to track live flights in real-time and search for affordable routes. You can also save flight information for later viewing, which is presented in a clean, tabular format.

This tool leverages the AviationStack API for comprehensive, real-time flight data and offers a user-friendly experience powered by the questionary library.

✨ Features
This application comes packed with several key features to enhance your flight tracking and booking experience:

✈️ Live Flight Tracking: Track any flight in real-time using its IATA or ICAO number. Get up-to-the-minute details including:

Airline Name

Departure & Arrival Airports

Scheduled vs. Actual Departure/Arrival Times

Current Flight Status (e.g., scheduled, en-route, landed)

💸 Route & Deal Search: Find the best flight deals for your desired routes by providing the following information:

Departure & Arrival Airports

Outbound and Return date

And receive the following information:

Best Available price

Name of the Airline

Flight Duration

And more...

📚 Save & View Flights: Save the details of any tracked flight directly to a local database. You can easily retrieve and view this information later in a beautifully formatted table using the tabulate library.

🤖 Interactive CLI: A user-friendly, emoji-enhanced menu system built with questionary makes navigating the application's features a breeze.

✅ Simple & Clean: The codebase is straightforward and easy to understand, making it a great project for learning or contribution.

# How it works?

The program operates on a continuous loop, presenting a command-line menu built with the questionary library. When a user selects an option:

Search for routes: It prompts the user for input such as the deparature airport's ID and the destination airport's ID. The outbound date and the returning date. Based on those pieces of information it makes an API request to Serpapi. From the recieved Json the program prints out an easily understandable output with price, duration and so much more...

Flight Tracking: It prompts for a flight IATA/ICAO code. This code is then embedded into a URL for the AviationStack API. The requests library sends an HTTP GET request to this URL. The program parses the returned JSON data to extract and display live flight details like status, times, and locations.

Saving Data: If the user chooses to save, the extracted flight details are passed to a save function which stores the information in a local database (managed by the functions in db.py).

Viewing Data: To view saved flights, the program retrieves the data from the database and uses the tabulate library to format and print it in a clean, human-readable grid in the terminal.

Essentially, it's a state-driven CLI that acts as a front-end to the AviationStack API, with added functionality for local data persistence and presentation.



# installation

Prerequisites

Make sure you have Python 3.6 or higher installed on your system. You will also need an API key from AviationStack and Serpapi to fetch flight data and prices.

Before using the app, install the required libraries:
```shell
pip install -r requirements.txt
```

## Usage

To run the app:
```shell
python project.py
```
Follow the on-screen instructions that are easily understandable and it's a breeze to use such a delightful program.

