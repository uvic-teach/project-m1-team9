# MisterED Textual Use Cases

### UC-1: View Current ED Load

**Description**: The patient is able to view ED queue loads

**Actors**:
- Patient (Primary actor)

**Assumptions**:
- The patient has successfully signed-in to their MISTER ED account.

**Steps**:
1. The patient selects the option that brings them to the screen that shows them local ED queues.

**Variations**: 

**Non-functional**:

- **Reliability**: The display for the queue loads must be accurate.

**Issues**: 

- The number of other patients in the queue must not indicate any personal information about the other patients.
- The queue load is not an accurate representation of ED wait times

---

### UC-2: Locate Nearby Solution 

**Description**: 

**Actors**:

- Patient (Primary actor)
- Map service
- Emergency Department

**Assumptions**: 
- Patient knows what they want to find for health care.
- If the patient wants to go to an ED, they know which one to go to.

**Steps**:
1. Open the MisterEd system.
2. Filter by location and type of care desired.
3. Find location, directions, and contact information of desired medical service. 

**Variations**:
- Patient doesn't find what they're looking for.

**Non-functional**:
- needs to scalable to large datasets of maps.
- Needs to be accurate and have up to date information on services and locations.

**Issues**:
- runtime

### UC-2a: View Current ED Load

**Use Case Extension**: UC-1 extends UC-2

**Description**: User can see ED loads of ED's on the map.

**Actors**:

- Patient (Primary actor)
- Emergency Department

**Assumptions**: 
- Patient is planning on going to an ED but is concerned about capacity or wait time.

**Steps**:
1. Open the MisterEd system.
2. Filter by location and ED's.
3. Find ED's near the patient.
4. Check current ED load on the map of the ED's nearby.

**Variations**: 
- Patient decides on other medical treatment if ED isn't strongly recommended.
- Patient changes which ED they're going to visit based on current ED load.
- Patient goes to ED after seeing that they're not at a high capacity despite not being recommended to.

**Non-functional**:
-needs to scalable to large datasets of maps

**Issues**:
- runtime
- Needs to be accurate and have up to date information on services, locations, and current ED load.

### UC-2b: Take Virtual Triage

**Description**: 

**Actors**:

- Patient (Primary actor)
- Emergency Department

**Assumptions**: 
- Patient is registered and signed into the MisterEd system.
- Patient is unsure of what sort of medical treatment they require.
- Patient is able to be safely virtually triaged and recommended an accurate course of action.

**Steps**:
1. The patient answers the questions on the triage questionnaire using drop-down menus for answers (multiple choice).
2. The inputs are used to automatically determine the next steps for the patient.
3. The results are given to the patient.
4. From the type of care recommended, the maps locates the closest resources to the patient using the map.
5. The patient can now find directions, availiablity, and contact information for various services in their area from the map.

**Variations**: 
- Patient is told to go to one of:
  - Pharmacty (OTC Medication)
  - GP/clinic
  - Medical hotline
  - In person triage
  - Directly placed in the ED queue

**Non-functional**:
- Needs to be consistent and reliable
- Needs to give accurate triage assessments and when unable to, get the patient triaged in person.

**Issues**:
- Accuracy
- Patients not being able to accurately answer technical questions
- Databases not containing enough information on previous health conditions for an accurate triage

---

### UC-3: Take Virtual Triage 

**Description**: The patient takes a virtual triage through Mister Ed

**Actors**:

- Patient (Primary actor)

**Assumptions**:

- The patient is able to competently answer the questions on the triage questionnaire. 
- The patient has successfully signed-in to their MISTER ED account.

**Steps**:

1. The patient answers the questions on the triage questionnaire using drop-down menus for answers (multiple choice).
2. The inputs are used to automatically determine the next steps for the patient.
3. The results are given to the patient.

**Variations**: 
- The patients results are compiled so that its optimal to Locate a nearby health solution.
- Virtual triage is not sufficient, real triage is required.

**Non-functional**:

- **Performance & Scalability**: This use-case should be able to be completed quickly and should not be slowed by technical issues.
- **Usability**: The questionnaire must be simple enough for any user to be able to complete it.
- **Reliability**: This use-case must be reliable as incorrectly triaging a person could have serious consequences on their health. 

**Issues**:

- The patient’s triage information must remain private

### UC-3a: Real Triage 

**Description**: The patient takes a real triage through the ED system

**Actors**:

- Patient
- ED

**Assumptions**:
- The patient is unable to be safely triaged virtually.
- The patient is able to answer questions in the in person triage.
- The ED can observe the condition of the patient.

**Steps**:

1. The patient is told to go to the closest ED for an in person triage.
2. Patient arrives at the ED.
3. Patient is triaged in person.

**Variations**: 

**Non-functional**:

- **Performance & Scalability**: This use-case should be able to be completed quickly and should not be slowed by technical issues
- **Usability**: The instruction to go to the ED should be clear and concise
- **Reliability**: This use-case must be reliable as failing to notify them to get triaged in person could lead to negative health affects 

**Issues**:

- Patient doesn't go to the ED
- Patient forgets that they were notified that they should get triaged in person
- Notifications are blocked by the patient

---

### UC-4: Sign into Mister Ed

**Description**: Have the patient log into the Mr ED system so other actions can be performed within the system.

**Actors**:
- Patient (Primary actor)

**Assumptions**: 

- Patient has access to the internet
- Patient has a valid PHN
- Patient has a valid email

**Steps**:

1. Patient Inputs legal name
2. Patient inputs health care number
3. Patient Inputs valid password
4. Patient is logged in to Mr ED system 

**Non-functional**:

- **Intuitive**: must be simple for non tech savvy users to easily log in 
- **Forgot password**: must have function to send a replacement password to email. 

**Issues**: 

- Site security
- Encryption

### UC-4a: Register to Mister Ed

**Use Case Extension**: UC-5 extends UC-4

**Change**: Instead of logging into Mister Ed immediately, the patient must first make an account if they do not already have one

**Steps**:  

1. Patient inputs legal name
2. Patient inputs valid email
3. Patient inputs health care number
4. Patient creates valid password
5. Patient confirms password
6. Patient confirms they are not a robot
7. Patient agrees to terms of consent form
8. Patient is logged-in to Mr ED system 

**Issues**: 
- Site security
- Encryption
  
---


### UC-5: Register to Mister Ed

**Description**: Have the patient register to the MisterED system so that the user can sign into the MisterED system.

**Change**: Instead of logging into Mister Ed immediately, the patient must first make an account if they do not already have one

**Steps**:  

1. Patient fills in Username
2. Patient fills in health info
   2.1 patient inputs BC health number
   2.2 BC health number is checked against BC health database
3. Patient gives password
4. patient confirms password
5. Registration completed.

**Issues**: 
- Site security
- Possiblity of making public citizens medical information
- Encryption
  
---

### UC-6: Notify Patient of ED visit 

**Description**: By end of usecase Patient has been notified to come into ER  

**Actors**
- Patient
- ED

**Assumptions**: 
- Patient is near the top of the queue and can be treated by the ED soon.
- Patient is registered and signed into the Mister Ed system.
- ED knows that the patient is waiting on a notification from them to arrive to the ED and not waiting inside the ED.

**Steps**:
1. recieve the patient that needs to be notified to com into the ER
2. send a notification to patient for patient to confirm they are coming
3. wait for patient to confirm
4. Patient confirms that they are coming to ED

**Variations**: 
Patient does not confirm they are coming to ED through MR ED system,
- Take no Action thorugh system, only perform action if they Show up to ED
**Non-functional**:


**Issues**:
- Site security
- Possiblity of making public citizens medical information
- Encryption

### UC-6a: Notify Patient of ED Visit

**Use Case Extension**: UC-3 extends UC-6

**Actors**:

- Patient (Primary actor)

**Assumptions**:

- The patient is able to competently answer the questions on the triage questionnaire. 
- The patient has successfully signed-in to their MISTER ED account.

**Steps**:

1. The patient answers the questions on the triage questionnaire using drop-down menus for answers (multiple choice).
2. The inputs are used to automatically determine the next steps for the patient.
3. The results are given to the patient.

**Variations**: 

- The patient cannot be safely triaged virtually so they are given a triage location to travel to and are triaged in person.

**Non-functional**:



**Issues**:

- The patient’s information must remain private

---

### UC-7: Real Triage

**Description**: The patient is told to receive triage in-person at a specificed location

**Actors**:

- Patient (Primary actor)
- Emergency department (ED)

**Assumptions**: 

- The patient is able to answer questions in the in person triage.
- The ED can observe the condition of the patient.

**Steps**: 

1. Patient arrives at ED.
2. Patient is triaged in person.
3. Patient identity is verified.

**Issues**: 

---

### UC-7a: 

**Use Case Extension**: UC-6 extends UC-7

**Actors**:

- Patient
- ED

**Assumptions**:

- The patient is able to answer questions in the in person triage.
- The patient does not want to wait a long time in the ED waiting room if avoidable.
- The patient has registered for the MisterEd system and is signed in.

**Steps**:

1. Patient notifies ED that they are registered with MisterEd.
2. ED updates their queue as they treat patients.
3. MisterEd sends notifications to patients to come to the ED when they are close to the top of the queue.

**Variations**: 
The patient will not be seen in a very timely manner then the ED will tell them that through Mr Ed they will be notified of when they should visit the ED. 

**Non-functional**:
- Reliable: If this notification doesn't go out, people will miss their spot or chance to get treated.
- Fault Tolerance: Notifications have to be sent out soon enough that the patient has time to return to keep things moving smoothly.

**Issues**:

- The patient misses the notification
- Patient is not connected to the internet or is out of service area

---
