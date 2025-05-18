import hashlib
import uuid

def tokenize(data):
    return hashlib.sha256((data + str(uuid.uuid4())).encode()).hexdigest()

if __name__ == "__main__":
    sensitive_info = input("Enter sensitive data: ")
    token = tokenize(sensitive_info)
    print("Tokenized:", token)
