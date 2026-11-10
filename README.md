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