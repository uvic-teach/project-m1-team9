# Mr ED Textual Use Cases

## Patient

### UC-P1

**Description**: Have the patient log into the Mr ED system so other actions can be performed within the system.

**Actors**:
- Patient

**Assumptions**: Patient has a computer with internet connection and a valid email address

**Steps**:

1. Patient Inputs legal name
2. Patient inputs health care number
3. Patient Inputs valid password
4. Patient is logged in to Mr ED system 


**Variations**: If Patient does not currently have a MISTER ED account the steps will change to:

1. Patient inputs legal name
2. Patient inputs health care number
3. Patient creates valid password
4. Patient confirms password
5. Patient confirms they are not a robot 
6. Patient is logged-in to Mr ED system 

**Non-functional**:

- **Intuitive**: must be simple for non tech savvy users to easily log in 
- **Forgot password**: must have function to send a replacement password to email. 

**Issues**: 

- Site security
- Hide plain password text 
- Patient not having a PHN


---

### UC-P2

**Description**: Take Virtual Triage 

**Actors**:

- Patient 

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

### UC-P3

**Description**: The patient is able to view ED queue loads

**Actors**:
- Patient 

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

### UC-P4

**Description**: Patient enters queue to be notified of ED arrival time

**Actors**:

- Emergency department (ED)
- Patient

**Assumptions**: 

- Patient is logged into their account with correct contact information
- Patient has completed triage

**Steps**: 
1. Users triage results are used to prioritize their appointment time
2. Appointment time is updated as ED volume fluctuates
    1. User is notified if appointment time changes
3. Closer to their appointment time, the user is sent finalized arrival time and location details for their appointment

**Variations**: 

**Non-functional**:

- Notification system must be fast
Emails, phone notifications must arrive seconds after being dispatched
- Arrival time and location must be easy for the user to understand and act on
    - Integrate with GPS apps (i.e., Google/Apple maps)
    - Integrate with calendar apps (i.e., Google/Microsoft/Apple calendar)


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

### UC-N2

**Description**: View ED current loads

**Actors**:

- Nurse

**Assumptions**: 

- Nurse has an authorized account in the Mr ED system

**Steps**: 

1. The nurse selects the option on the Mr ED platform that allows them to see current loads in the ED

**Variations**: 

**Non-functional**:

**Issues**: 

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

### UC-D2

**Description**: 

**Actors**:

**Assumptions**: Software system

**Steps**: Intention of the use case.

**Variations**: 

**Non-functional**:

**Issues**: 

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

### UC-T2

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

### UC-T3

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

### UC-T4

**Description**: 

**Actors**:

**Assumptions**: Software system

**Steps**: Intention of the use case.

**Variations**: 

**Non-functional**:

**Issues**: 
