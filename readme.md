# Habit Tracker

A Python project that uses the Pixela API to track daily habits and activities. This script allows you to log activities, update your progress, and delete entries, making it easy to maintain a visual record of your habits over time.
> **Note**: This project is for learning purposes only.
## Features

- **User Account Creation**: Sets up a new Pixela user account (run once).
- **Graph Creation**: Creates a graph for tracking a specific habit (e.g., cycling distance in kilometers).
- **Daily Logging**: Adds a new entry (or "pixel") to the graph with user-provided data.
- **Update Entry**: Updates the entry for a particular day.
- **Delete Entry**: Deletes the entry for a particular day.

## Prerequisites

- Python 3
- `requests` library (install via `pip install requests`)

## Setup

1. Clone this repository.
2. Install the `requests` library if not already installed:
   ```bash
   pip install requests
   ```

3. Replace the placeholders in the script with your Pixela `USERNAME`, `TOKEN`, and `GRAPH_ID`:
   ```python
   USERNAME = "your_username"
   TOKEN = "your_token"
   GRAPH_ID = "your_graph_id"
   ```
## Example 
[Demo](https://pixe.la/v1/users/madhavanr/graphs/graph1.html)
## Usage

1. **Create a User** (optional if you already have an account): Uncomment the user creation section in the script to create a new Pixela account.
2. **Create a Graph**: Uncomment the graph creation section to set up a graph for your habit.
3. **Log Your Habit**: Run the script, and enter the amount (e.g., kilometers cycled) when prompted.
4. **Update/Delete an Entry**: Uncomment the relevant sections to update or delete entries as needed.
