import os
import requests

from langchain_core.messages import HumanMessage #framework that enables building AI agents
from langchain.tools import tool # Allows us to define tools that the agent can use
from langchain_openai import ChatOpenAI #Allows us to use OpenAI's language models
from langgraph.prebuilt import create_react_agent #Allows us to create a React agent
from dotenv import load_dotenv #enables loanding environment variables from a .env file

load_dotenv() # Load environment variables from .env file

print(os.getenv("weather_api_key"))

@tool
def get_weather(location: str) -> str:
    """
    Get the current weather for the specified location.
    
    Args:
        location (str): The name of the location to get the weather for.
    
    Returns:
        str: A string describing the current weather in the specified location.
    """
    location = location.strip()
    if not location:
        return "Please provide a valid location."

    # Load the API key from the environment variable
    API_KEY = os.getenv("weather_api_key")
    if not API_KEY:
        return "Wouldn't you like to know weatherboy (I'm not telling you)"

    print("Researching...")  # Display a message to let the user know the program is working

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": API_KEY, "units": "metric"}

    for attempt in range(2):  # Retry up to 2 times
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()

            if "main" in data and "weather" in data:
                temp = data["main"].get("temp", "N/A")
                description = data["weather"][0].get("description", "N/A")
                return f"The current temperature in {location} is {temp}°C with {description}."
            else:
                return "Wouldn't you like to know weatherboy (I'm not telling you)"
        except requests.exceptions.RequestException:
            if attempt == 0:  # First attempt failed
                print("Double checking to give you the perfect weather report...")
            else:  # Second attempt failed
                return "Wouldn't you like to know weatherboy (I'm not telling you)"

    return "Wouldn't you like to know weatherboy (I'm not telling you)"


def main():
    model = ChatOpenAI(temperature=1.0)  # Initialize the OpenAI model with a temperature of 1.0 for more interesting responses

    tools = [get_weather]  # Define the tools that the agent can use, in this case, the get_weather function
    agent_executor = create_react_agent(model, tools)  # Using agent framework from langgraph

    print("Hello there! I am Big John, your AI Weatherman. What can I do to help you today my guy?")

    while True:
        user_input = input("\nYou: ").strip()  # Get user input and strip any leading/trailing whitespace

        if user_input.lower() == "exit":  # Check if the user wants to exit the loop
            print("See Ya! Have a Big Johnerific day!")
            break

        print("\nBig John: ", end="")  # Print the response from Big John without a newline
        final_response = False  # Track if the response is final

        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}  # Send user input as a HumanMessage to the agent executor
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:  # Check if the chunk contains agent messages
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")  # Print the content of the message without a newline
                    if "Wouldn't you like to know weatherboy" in message.content or "The current temperature" in message.content:
                        final_response = True

        print()

        if final_response:  # Stop further processing if the response is final
            break

if __name__ == "__main__":
    main()  # Call the main function to start the program



