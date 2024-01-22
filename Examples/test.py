import sys 
import os 

### Needed for correct importing w/o install ####
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
#################################################

from payload_generator import Payload_Generator

template = '{[0,6]}0A{R[0,1,"B"]}FF{R[1,2,">H"]}0E{[0,4]}DD'
payloads = Payload_Generator(template)

for pl in payloads:
    print(pl)
