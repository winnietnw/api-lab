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