import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPEN_API_KEY")

# Initialize the OpenAI client with the API key
openai.api_key = api_key

def generate_unique_pairs_prompt(numbers: str, target: str) -> str:
    """
    Sends a prompt to GPT-4 asking it to generate a Python function
    that finds all unique pairs whose sum equals the target.
    """
    # System message to explain the task
    system_message = (
        "Write a Python function that finds all unique pairs of numbers "
        "from the provided list whose sum equals the target. "
        "Each pair should appear only once (e.g., treat (2, 3) and (3, 2) as the same). "
        "Optimize for time and space complexity."
    )
    
    # User message containing the input array and target sum
    user_message = f"Array: {numbers}\nTarget: {target}"

    # Make the API call to OpenAI to generate the code
    response = openai.Completion.create(
        model="gpt-4",  # or gpt-3.5-turbo depending on the model
        prompt=system_message + "\n" + user_message,
        temperature=0  # To ensure deterministic output
    )

    # Extract and return the generated code from the response
    return response.choices[0].text.strip()

def main():
    # Prompt the user to enter a space-separated list of integers
    raw_numbers = input("Enter a list of integers (space-separated): ").strip()
    # Convert the string input into a list of integers
    numbers = list(map(int, raw_numbers.split()))
    
    # Prompt the user to enter the target sum
    target = input("Enter the target sum: ").strip()

    print("\nGenerating function from GPT-4...\n")
    
    # Generate Python code using GPT-4
    result = generate_unique_pairs_prompt(numbers, target)
    
    # Print the generated code
    print("💡 Generated Python Code:\n")
    print(result)

# Ensure the script runs only when executed directly (not when imported)
if __name__ == "__main__":
    main()
