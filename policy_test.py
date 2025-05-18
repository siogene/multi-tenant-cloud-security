import requests

def test_abac(role):
    response = requests.get(f"http://localhost:5000/access?role={role}")
    print("Response:", response.json())

if __name__ == "__main__":
    test_abac("admin")
    test_abac("guest")
