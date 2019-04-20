import hexchat
import re
import os

__module_name__ = "RatsignalSysCopy"
__module_version__ = "0.1"
__module_description__ = "HexChat script that automatically copies system name to clipboard for each incoming ratsignal."


# Set this to true to print debugging messages
enableLogging = False


# Regex for matching reported system name in ratsignal
# Seems like MechaSqueak's ratsignal formatting is pretty consistent, so we
# wont worry too much about making it flexible
# Example:
#   RATSIGNAL - CMDR CommanderName - Reported System: Ceramix (86.82 LY from Sol) - Platform: PC - O2: OK - Language: English (en-US) (Case #6) (PC_SIGNAL)
# For some reason the system name has the control char \x02 on either side in the source string from HexChat
# Subgroup 1 holds system name
reg = re.compile("Reported\\sSystem:\\s\x02?([ 0-9a-zA-Z-]*?)\x02?\\s\\(.*?\\)\\s-\\sPlatform")


def printDebug(text):
    if enableLogging:
        print(text)
    return


def getSystemName(messageText):
    # Find matches input string
    match = reg.search(messageText)
    # Pull out subgroup 1
    if match is not None:
        try:
            systemStr = match.group(1).strip()
            if len(systemStr) > 0:
                printDebug("RatsignalSysCopy: Found system string: " + systemStr)
                return systemStr
            else:
                printDebug("RatsignalSysCopy: Empty system string.")
        except IndexError:
            printDebug("RatsignalSysCopy: Invalid group index.")
    else:
        printDebug("RatsignalSysCopy: Could not find reported system in ratsignal string.")
    return None


def copyStringToClipboard(strToCopy):
    if len(strToCopy) > 0:
        command = "echo | set /p=" + strToCopy + "| clip"
        os.system(command)


def alertTextCallback(word, word_eol, userdata):
    # The 'Channel Msg Highlight' events hold all the event text in index 1
    if len(word) >= 2:
        sysName = getSystemName(word[1])
        if sysName is not None:
            copyStringToClipboard(sysName)
    else:
        printDebug("RatsignalSysCopy: Unexpected number of words in event \"Channel Msg Hilight\"")
    return hexchat.EAT_NONE


printDebug("RatsignalSysCopy loaded!")

# Register callback for 'Channel Msg Hilight' print events.
# Ratsignal will be one of these events as long as its configured for highlighting in hexchat
hexchat.hook_print("Channel Msg Hilight", alertTextCallback)

