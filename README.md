# Poetry DB Tests

This project automates the process of navigating to a Twitch streamer's page and taking a screenshot using Selenium and pytest.

## Prerequisites

- **Python 3.\***
- **requests** library: Installed at step 4 using `pip install -r requirements.txt`
- **pytest**: Installed at step 4 using `pip install -r requirements.txt`

## Setup Instructions

### 1. Clone the Repository

```bash
git clone [repository_url]
cd poetrydb
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment (Linux/MacOS)

```bash
source venv/bin/activate
```

### 3. Activate the Virtual Environment (Windows)

```bash
venv\Scripts\activate
```


### 4. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 5. Run the Test

```bash
pytest test_poetry.py
```

### 5.1 Run the Test (DEBUG Mode)

```bash
pytest --capture=no test_poetry.py
```
## Test Cases Summary

| **Test Case ID** | **Description**                  | **Steps**                                                                                                                                                                                                                                                                                                                                                 | **Expected Result**                                                                                                                                                                                                           |
|------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TC-001**       | Retrieve a poem by title         | 1. Send a GET request to `/title/Ozymandias`<br>2. Check status response = 200<br>3. Verify one or more poems returned<br>4. Verify the poem title is "Ozymandias"<br>5. Verify the author is "Percy Bysshe Shelley"<br>6. Verify there are 14 lines in the "lines" array<br>7. Verify the line count is "14" equal with returned linecount from response | - Status code is **200 OK**<br>- Poem title is **"Ozymandias"**<br>- Author is **"Percy Bysshe Shelley"**<br>- Line count is **"14"**<br>- "lines" array contains **14 lines**                                                |
| **TC-002**       | Retrieve poems by author         | 1. Send a GET request to `/author/Emily Dickinson`<br>2. Check status response = 200<br>3. Verify that at least one poem is returned <br>4. Verify all returned poems are authored by "Emily Dickinson" and retuned lines count equals linecount from result                                                                                              | - Status code is **200 OK**<br>- All poems are authored by **"Emily Dickinson"**<br>- At least **one poem** is returned<br>- linescount equals with number on non empty lines from response                                   |
| **TC-003**       | Handling invalid endpoint        | 1. Send a GET request to `/title/404`<br>2. Verify the status code is **200 OK** (Normally must be **404 Not Found**)<br>3. Verify the response contains an error message indicating an invalid endpoint                                                                                                                                                  | - Status code is **200 OK** (must be 404, i've used 200 because bad api implementation)<br>- Response body contains an **status** equals with **404**<br>- Response body contains **reason** that is equal with **Not found** |

## Validation Methods and Rationale

In the automated tests for the PoetryDB API, several validation methods have been employed to ensure that the API responses meet the expected criteria. Below is a description of the validations used in each test case and the rationale behind choosing these validations.

### **TC-001: Retrieve a Poem by Title**

- **Validation of HTTP Status Code (200 OK):**
  - **Why:** Ensures that the API endpoint is accessible and that the request was successfully processed.
  - **How:** By asserting that `response.status_code == 200`.

- **Validation of Poem Title and Author:**
  - **Why:** Confirms that the API returns the correct poem and that the data integrity is maintained.
  - **How:** By checking that `poem["title"] == "Ozymandias"` and `poem["author"] == "Percy Bysshe Shelley"`.

- **Validation of Line Count:**
  - **Why:** Verifies that the poem content is complete and that no lines are missing.
  - **How:** By asserting that `poem["linecount"] == "14"` and that the length of `poem["lines"]` is 14.

- **Data Structure Validation:**
  - **Why:** Ensures that the response JSON structure matches the expected format.
  - **How:** By accessing the expected keys in the JSON object without errors.

### **TC-002: Retrieve Poems by Author**

- **Validation of HTTP Status Code (200 OK):**
  - **Why:** Confirms that the API request was successful.
  - **How:** By asserting that `response.status_code == 200`.

- **Validation of Author Field in Each Poem:**
  - **Why:** Ensures that all returned poems are authored by the specified author, validating the correctness of the filtering functionality.
  - **How:** By iterating over each poem in the response and asserting that `poem["author"] == "Emily Dickinson"`.

- **Validation of Response Data Quantity:**
  - **Why:** Confirms that the API returns data when expected, indicating that the database contains entries for the author.
  - **How:** By asserting that the length of the poems list is greater than zero.

- **Validation of Line Count:**
  - **Why:** Verifies that the poem content is complete and that no lines are missing.
  - **How:** By asserting that the number of lines in each poem matches the expected line count and ignoring empy lines.

### **TC-003: Handling Invalid Endpoint**

- **Validation of HTTP Status Code (200 OK) (Standard would be 404 in this case, but this is the api :D ):**
  - **Why:** Ensures that the API correctly handles requests to invalid endpoints by returning an appropriate error status code.
  - **How:** By asserting that `response.status_code == 200`. (Normally should be 404, used 200 because of bad api implementation and to be able to test other expected results)

- **Validation of Error Message in Response:**
  - **Why:** Verifies that the API provides meaningful error messages to help users understand the issue.
  - **How:** By checking that the response body contains the expected error message, such as "Not Found" and **404** as status.

### **General Rationale for Validation Choices**

- **HTTP Status Codes:**
  - **Importance:** Validating HTTP status codes is fundamental in API testing to confirm that the server is responding correctly to different types of requests.
  - **Benefit:** Helps in quickly identifying issues related to request handling, authentication, or server errors.

- **Response Content Validation:**
  - **Importance:** Checking the content of the response ensures that the API returns the correct data and that data integrity is maintained.
  - **Benefit:** Validates that the API's filtering and data retrieval functionalities work as intended, providing accurate data to consumers.

- **Error Handling Validation:**
  - **Importance:** Testing how the API handles invalid inputs or endpoints is crucial to ensure robustness and user-friendliness.
  - **Benefit:** Confirms that the API adheres to RESTful principles by providing appropriate status codes and error messages, enhancing the developer experience.

- **Data Structure and Completeness:**
  - **Importance:** Ensuring that the response data structures are as expected (e.g., JSON format with specific keys) helps prevent issues when the API is consumed by clients.
  - **Benefit:** Reduces the risk of runtime errors and ensures seamless integration with client applications.

By performing these validations, we can increase confidence in the reliability and correctness of the API, providing assurance that it behaves as expected under various scenarios.

### Notes

- The API is not perfect, and the tests are designed to handle the current implementation of the API.
- The tests are written to validate the expected behavior of the API, and the expected results are based on the current API responses.
- Other scenarios and edge cases can be added to further enhance the test suite's coverage and robustness. Examples include testing for empty responses, timeouts, and malformed JSON responses, other response types, etc. .