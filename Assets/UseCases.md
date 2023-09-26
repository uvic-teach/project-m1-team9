# Mr ED Textual Use Cases

## Patient

### UC-1: Sign into Mister Ed

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
  
---

### UC-1a: Register to Mister Ed

**Use Case Extension**: UC-1a extends UC-1

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

### UC-2: Take Virtual Triage 

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

- The patient cannot be safely triaged virtually so they are given a triage location to travel to and are triaged in person.

**Non-functional**:

- **Performance & Scalability**: This use-case should be able to be completed quickly and should not be slowed by technical issues.
- **Usability**: The questionnaire must be simple enough for any user to be able to complete it.
- **Reliability**: This use-case must be reliable as incorrectly triaging a person could have serious consequences on their health. 

**Issues**:

- The patient’s triage information must remain private

---

### UC-3: View Current ED Load

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

### UC-4: Real Triage

**Description**: The patient is told to receive triage in-person at a specificed location

**Actors**:

- Patient (Primary actor)
- Emergency department (ED)

**Assumptions**: 

- The patient was unable to virtually complete triage

**Steps**: 

1. An appropriate in-person location for triage is determined.
2. The patient is given the location of their in-person triage and told to see a ED staff member at this location.

**Issues**: 

- How far in advance of their appointment is the user given appointment time and location

## Nurse 
### UC-N1

**Description**: Assign treatment option to patient

**Actors**:

- Nurse
- Patient

**Assumptions**:

- Patient has completed an in person triage

**Steps**:

1. Nurse assess patient details
2. Nurse directs patient to treatment options


**Variations**: 

**Non-functional**:

**Issues**: 

---

### UC-5

**Description**: Register to Mr ED

**Actors**:

- Patient, BC health database

**Assumptions**: 

- Patient does not have an authorized account in the Mr ED system
- Mr ED system has access to BC health Database

**Steps**: 

1. Patient fills in Username
2. Patient fills in health info
   2.1 patient gives health number
   2.2 number is checked against database
3. Patient gives password
4. patient confirms password

**Variations**: 
patient puts in wrong health number - returns an error
**Non-functional**:

**Issues**: 
cyber security

## Mister ED Database
### UC-D1

**Description**: Manage appointments

**Actors**:

- Mr ED Database
- Patient

**Assumptions**:

- Mr ED database can communicate to send and receive information from the provinces health database. Mr ED system has complete access to the database.

**Steps**:

1. From the Mr ED database first must view priorities of all the current patients 
2. Then must ensure that from the database


**Variations**: 

**Non-functional**:

**Issues**: 

---

### UC-6 extends UC-3 

**description**: notify patient of ED vist

**change**: want to alert patient that they should now arrive to the ER room so they can be helpped

**Steps**: 
1. recieve the patient that needs to be notified to com into the ER
2. send a notification to patient for patient to confirm they are coming
3. wait for patient to confirm
4. They confim that they are coming

**Variations**: 

**Non-functional**:

**Issues**: 
cyber security

## Treatment Assignment
### UC-T1

**Description**: Patient is recommended to go to clinic/GP

**Actors**:

- Patient
- Primary care clinic

**Assumptions**: Software system

**Steps**: 

1. The patient is contacted with a recommendation to go to a primary care clinic 

---

### UC-7

**Description**: Patient is recommended to take an over the counter (OTC) medicatio

**Actors**:

- Patient

**Assumptions**: Software system

**Steps**:

- The patient is contacted with a recommendation to take an OTC medication

**Variations**: 

**Non-functional**:

**Issues**: 

---

### UC-8

**Description**: Patient is recommended to contact a medical hotline

**Actors**:

- Patient

**Assumptions**: Software system

**Steps**:

- The patient is contacted with a recommendation to phone a medical hotline

**Variations**: 

**Non-functional**:

**Issues**: 

---

### UC-9

**Description**: 

**Actors**:

**Assumptions**: Software system

**Steps**: Intention of the use case.

**Variations**: 

**Non-functional**:

**Issues**: 
