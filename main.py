#!/usr/bin/env python3
import base64
import hashlib
import os
import secrets
import string

from dotenv import load_dotenv

load_dotenv()


def generate_salt(length=16):
    """Generate a random salt."""
    return secrets.token_bytes(length)


def generate_password(master_secret: str, salt: bytes, length=24):
    """
    Generate a password using the master secret and salt.
    """

    derived_key = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=master_secret.encode(),
        salt=salt,
        iterations=600_000,
        dklen=length,
    )
    password = base64.urlsafe_b64encode(derived_key).decode("utf-8")
    return password[:length]


if __name__ == "__main__":
    master_password = os.environ.get("MASTER_SECRET")

    if not master_password:
        raise ValueError("MASTER_SECRET environment variable is not set.")

    salt = generate_salt()

    password = generate_password(master_password, salt)

    print("Salt: ", salt.hex())
    print("Generated Password: ", password)
