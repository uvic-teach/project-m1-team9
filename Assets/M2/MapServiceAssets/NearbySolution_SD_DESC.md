## SD-5: Nearby ED Location

### Description:
The Nearby ED location sequence Diagram shows the sequence that occurs when a patient wants to use the feature to quickly find a hospital or other form of care nearest them. 

### Participants:
- Patient: THe patient is the user that is trying to locate a health service near them.
- MR ED System: The MR ed system is the interface that the patient interacts with.
- Map Service: The map sevice is an equivalent to google maps that has data on coordinates of health services.
- ED: A Emergency Department that can provide care to patients
- GP clinic: a clinic that provide care to patients

### Messages:
1. Open MR ED System: user opens up the mr ed system so they can interact with the interface
2. Input Desired Locations: User while within The MrED system inputs the desired Health locations that they would like to use.
3. Look for Desired Location: System goes to map service to grab information on the available locations based on user input.
4. Return Suitable Location: map service finds and returns locations that work based on users input.
5. System shows users locations and care options: Interface shows user a list of the options of care and location.
6. Patient Chooses Available care and location option: Pick one of the options that was presented.
7. MR ED Notifies chosen destination: System interacts with the chosen location to update the locations queue, etc. 

### X fragment

