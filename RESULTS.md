# api-lab

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Short Carbonara
- Step 0.12, results of the three runs without a session (optional): 2 passed, 1 failed (401 Unauthorized).
- Step 0.16, blocks of "how many of the three tools are excluded":
  - 0 tools: PASSED
  - 1 tool: PASSED
  - 2 tools: PASSED
  - 3 tools: Defect found (HTTP 500)

## Defect report
- Title: Excluding all three pizza tools returns HTTP 500
- Request: POST /api/pizza with all three tools excluded.
- Expected result: HTTP 400 with a JSON error message.
- Actual result: HTTP 500 with an empty response body.
- Severity: Not specified in the lab instructions.

## Part A: Input Domain Model
| Characteristic | Blocks | Values in the tests | Test |
|---|---|---|---|
| C1 Value of stars | Below 1 | 0 | test_stars_out_of_range[0] |
| C1 Value of stars | 1 to 5 (base) | 3 | test_base_choice_is_saved |
| C1 Value of stars | Above 5 | 6 | test_stars_out_of_range[6] |
| C2 Type of stars | Whole number (base) | 3 | test_base_choice_is_saved |
| C2 Type of stars | Decimal | 3.5 | test_stars_decimal |
| C2 Type of stars | Text | "3" | test_stars_text |
| C2 Type of stars | Missing | No field | test_stars_missing |
| C3 Pizza | Exists (base) | Existing pizza | test_base_choice_is_saved |
| C3 Pizza | Does not exist | 999999999 | test_pizza_does_not_exist |
| C4 Token | Own token (base) | From auth | test_base_choice_is_saved |
| C4 Token | None | No header | test_rating_without_token |
| C4 Token | Wrong length | Token abc | test_rating_with_wrong_token |

- Step A4, status codes when the other user reads, changes and deletes:
  - Read: 404
  - Change: 400
  - Delete: 400

## Part B
1. API tests can find network problems and integration problems between the application and the real server, which unit tests with stubs cannot detect. Unit tests with stubs are still useful because they run faster, are easier to control, and can test individual functions without depending on the real server.
2. Every test creates its own user with a new name to avoid conflicts with other tests and to keep test data independent. Using the public token would mean sharing the same account and data. In Project 2, I will apply the same idea by creating separate test users and test data for each test instead of sharing one account.
3. A session allows multiple requests to share cookies and maintain information between requests. This makes the tests more consistent and avoids creating a new connection for every request. In Step 0.12, two runs passed and one run failed with 401 Unauthorized.
4. The block where all three tools are excluded revealed the defect. A 500 error with an empty body is worse because the client does not receive a useful error message to explain what went wrong. The test stays as xfail to document the known defect and detect when the server fixes it.
5. Base choice coverage needs 9 tests:
   - C1: 3 blocks
   - C2: 4 blocks
   - C3: 2 blocks
   - C4: 3 blocks
   Total = 1 + (3-1) + (4-1) + (2-1) + (3-1) = 9 tests.
   All combinations coverage needs 72 tests:
   3 x 4 x 2 x 3 = 72 tests.
6. The status codes in Step A4 were:
   - Read: 404
   - Change: 400
   - Delete: 400    
   I expected the API to refuse all three requests with a 4xx status code. All three responses were within the expected range, so this is not a defect.
7. The request with a made-up token returned 401 Unauthorized with the error message "authentication failed". This is the expected result because the API correctly rejects an invalid token. This is not a defect.
8. An API test can check status codes, response data, and whether the API behaves correctly. A test through the web pages can check visual appearance, layout, and whether the user interface works correctly.