# Random-Meeting-ID

This is a Python-based utility for generating unique and secure meeting IDs, inspired by Google's meeting ID format. The system is designed to be a core component of a larger video conferencing application, providing a reliable way to create meeting identifiers and manage access.

---

## Features

### Unique ID Generation
Generates unique meeting IDs based on a configurable pattern (e.g., `portion1-portion2-portion3`). Each portion consists of a random string of lowercase letters.

### Collision Prevention
To prevent ID collisions and enhance security, the system includes a quarantine mechanism. Recently used meeting IDs are automatically put into a "quarantine list" for a one-week period, ensuring that they are not immediately reused.

### Access Control
The application can be integrated with a database to manage a list of active meeting pins. It also allows for the pre-authorization of specific guests, enabling them to bypass the waiting room and join meetings automatically.

---

## Technical Details

The core logic is contained within a few simple, yet effective functions:

* `generate_portion(portion_size)`: Creates a random string of lowercase letters of a specified length.
* `generate_meeting_id(pattern)`: Combines three portions of specific lengths to form a complete, hyphenated meeting ID string.

The planned database integration will handle the following data:

* **Active Meeting Pins:** A list of all currently active meeting IDs.
* **Quarantined IDs:** A list of recently used meeting IDs, along with their quarantine expiration dates.
* **Authorized Guests:** A list of users allowed to join specific meetings without explicit host approval.

---

## Future Development

* Implement the **database connection** and management logic.
* Create a **quarantine service** to manage ID expiration and removal from the quarantine list.
* Develop a full **API** for creating, validating, and managing meeting IDs and guest access.
* Edge Case Handling **Limit Hit** Generate a Different pattern if there is no space for the current pattern format

This README provides an overview of the current functionality and future vision for the Meeting ID Generator. For more details on implementation, refer to the function docstrings within the code.
