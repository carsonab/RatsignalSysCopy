
# Test RatSignalSysCopy

import RatsignalSysCopy

# Turn on debug logging to see whats going on
RatsignalSysCopy.enableLogging = True

# Simulated input from HexChat for ratsignal
# For whatever reason, when coming from HexChat the control char \x02
# is on either side of the system name, so need to handle that
testInput = ["unused",
             "RATSIGNAL - CMDR Commanader_Name - Reported System: Pleiades Sector AB-C D12-345 (85.60 LY from Maia) - Platform: PC - O2: OK - Language: English (en-US) (Case #9) (PC_SIGNAL)"]
RatsignalSysCopy.alertTextCallback(testInput, None, None)
