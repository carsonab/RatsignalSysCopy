# RatsignalSysCopy

A ratting utility for automatically copying the system name to your clipboard for every incoming RatSignal.
Works with HexChat, Python 3, and Windows.

This will overwrite whatever is in your clipboard each time a new RatSignal comes in.

## Requirements

HexChat
- https://hexchat.github.io/
Python 3
- https://www.python.org/downloads/

## Installation

To install simply copy RatsignalSysCopy.py to your HexChat addons folder and restart HexChat.
Do **not** copy hexchat.py or test.py, they are for testing only :)
By default location of the HexChat addons folder is: `C:\Users\YourUserName\AppData\Roaming\HexChat\addons`
- Replace YourUserName with your windows user name

To function, ratsignals must be configured as highlighted text in HexChat. To configure:
- Select Settings > Preferences
- Select Alerts (under the Chatting category)
- Next to "Extra words to highlight" enter "Ratsignal" (without the quotes)

To check that RatsignalSysCopy is running, in HexChat type `/py list` into chat input and
make sure RatsignalSysCopy is listed.
