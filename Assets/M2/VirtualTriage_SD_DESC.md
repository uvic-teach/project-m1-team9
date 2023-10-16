## SD-3: Virtual Triage

### Description:
This is a sequence diagram for virtual triage covering the main usecases.

### Participants:
- Patient                      P  : Person seeking treatment.
- MisterEd Virtual Triage      VT : Virtual triage service we provide
- Notification System          NS : Sends notifications and keeps tract of the ED queue
- Map Service                  MS : Map microservice that shows the locations of health services
- BC Health Database           HDB: Stores patient data and medical history
- Emergency Department         ED : Emergency department at the hospital, has a queue
- Non-Emergency Health Options NE : Any external health resource to treat patients (Clinic, OTC medication)

### Messages:
P   ->  VT  : Patients starts virtual triage through MisterED

VT -->> P   : Virtual triage sends the survey questions to the patient

P   ->> VT  : Survey questions answered

VT  ->  HDB : Virtual triage requires medical history to accurately assess patient condition/risk

HDB -->>VT  : Medical history returned by the BC health database to help with triage

VT  ->  VT  : Process information, determines if the ED is required at all, and if so, if the triage is safe to do virtually

alt ED Required Case 1

    alt ED Required: Can be virtually triaged Case 1.1
    
        VT -->> P  : ED recommended to patient
        
        VT -> ED   : ED notified of patient and their triage result
        
    else ED Required: Cannot be virtually triaged Case 1.2
    
        VT -->> P  : In person triage recommended
        
        P ->    ED : Patient visits ED in person
        
        ED -->> P  : Patient is triaged in person
        
    ED ->> NS  : Patient added to queue based on triage result
    
else Can be virtually triaged: Non-Emergency Result Case 2

    VT -->> P  : Non-emergency recommended
    
    P  -> MS   : Checks map for treatment options nearby. This could be many things
    
    MS -->> P  : Non-Emergency health options displayed on map
    
    P  -> NE   : Emergency not required, other options used
    
    NE -> P    : Patient treated. This means that the diagram ends for the patient here in this case, and they stop interacting with our system.
    
NS ->>  P      : Patient told they are on the queue and will be notified

I was thinking of adding that the patient would be asked if they wanted a notification or ot wait but I figured if we're assuming they're using the MisterED system they would want to wait at home instead of at the ED.

loop forever

    ED ->>  NS     : Update queue
    
    if patient is soon in queue
    
        NS ->>  P      : Notification sent
        
        break
        
P   ->  ED     : Patient goes to ED

ED -->> P      : Patient treated

#### Notes:
1. Integration of the maps service is not finalized or thought out too well, as well as viewing current ed loads
2. Didn't display the case where the patient chooses to not deal with the MisterED notification system, misses the notification, or chooses to not receive notifications and just wait at the ED.
3. Could explore in more detail what the triage process would look like but would need to contact health professionals for input.
