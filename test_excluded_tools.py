import pytest

@pytest.mark.parametrize("excluded", [
    [],
    ["Knife"],
    ["Scissors"],
    ["Knife", "Scissors"]
])
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded

@pytest.mark.xfail(
    reason="Defect 1: Excluding all tools returns 500 instead of 400",
    strict=True
)
def test_all_tools_excluded_returns_error(api, auth):
    body = {
        "excludedTools": ["Knife", "Pizza cutter", "Scissors"]
    }
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 400
    assert "error" in res.json()