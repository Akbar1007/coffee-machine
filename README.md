# Coffee Machine Simulator

A Python-based simulation of a coffee vending machine. This project demonstrates object-oriented programming concepts and interactive user interfaces in Python.

## Features
- **Menu System**: Choose from a selection of coffee options, including latte, espresso, cappuccino, and americano.
- **Resource Management**: Tracks available water, milk, and coffee resources.
- **Payment Processing**: Simulates coin-based payments and calculates change.
- **Interactive Commands**: Allows users to view resources, make coffee, or turn off the machine.

## Project Structure
- **`coffee_maker.py`**: Handles resource management and coffee preparation.
- **`menu.py`**: Defines the menu and drink items.
- **`money_machine.py`**: Manages payment processing.
- **`main.py`**: The main script that ties everything together for user interaction.

## How to Run
1. Clone the repository:
   git clone https://github.com/Akbar1007/coffee-machine
2. Navigate to the project directory:
   cd coffee-machine-simulator
3. Run the main script:
   python main.py

## Usage
- **Available Commands**:
  - Type the name of a drink (e.g., `latte`) to order.
  - Type `report` to view the current resources and profits.
  - Type `off` to turn off the machine.

- **Coin Input**:
  - Enter the number of each type of coin when prompted.

## Example Output
Welcome to coffee machine.
What would you like? (latte/espresso/cappuccino/americano/): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is your latte ☕️. Enjoy!


## Requirements
- Python 3.x

Happy coding! ☕️
