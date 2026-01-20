# Project 9
## Blind Auction Program

A simple command-line blind auction application where multiple users can submit bids without seeing others' offers.

## Features

- Sequential bid collection from multiple participants
- Input validation for yes/no responses
- Screen clearing between bids to maintain privacy
- Automatic winner determination based on highest bid

## Requirements
```bash
pip install art
```

## Usage

Run the program:
```bash
python auction.py
```

Follow the prompts:
1. Enter your name
2. Enter your bid amount (numbers only)
3. Indicate if there are more bidders
4. Screen clears automatically for the next bidder
5. Winner is announced when all bids are collected

## How It Works

The program uses a dictionary to store bidder names and amounts, then uses Python's `max()` function with a key parameter to identify the highest bid. Screen clearing (100 newlines) ensures each bidder's amount remains confidential during the auction process.

## Example Output
```
What is your name?: alice
What is your bid?: $150
Are there any other bidders? Type 'yes' or 'no'. yes

What is your name?: bob
What is your bid?: $200
Are there any other bidders? Type 'yes' or 'no'. no

The user with the winning bid is: bob with a bid of 200
```

## What I Learned

- **Dictionary manipulation**: Using dictionaries to store key-value pairs (bidder names and amounts)
- **Input validation**: Implementing loops to ensure users provide valid responses
- **The `max()` function**: Using the `key` parameter to find dictionary keys with maximum values
- **Control flow**: Managing program state with boolean flags and conditional logic
- **User experience**: Creating privacy in a shared terminal environment through screen clearing
- **String methods**: Using `.lower()` for case-insensitive input handling
