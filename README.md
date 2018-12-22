# python_chatterbot
This project aims to show examples of how to create and use the ChatterBot library


### Installation

#### From PyPi
To install the last version of ChatterBot using pip run the following command in your terminal:

```bash
$> pip install chatterbot
```

### Checking ChatterBot version
If you already have ChatterBot installed and you want to check what version you have installed run the following command in your terminal:

```bash
$> python -m chatterbot --version
```

## Creating a simple chatbot
To understand how the chatterbot library works, take a look at the simple code example:

```python
from chatterbot import ChatBot

#This is a chatterbot object with a name parameter 
bot = ChatBot('bot_name');

#Getting a response from bot
response = bot.get_response("Hello bot!");
print(response)
```

### Analysis
More information, visit the [chatterbot docs](https://chatterbot.readthedocs.io/en/stable/index.html).
