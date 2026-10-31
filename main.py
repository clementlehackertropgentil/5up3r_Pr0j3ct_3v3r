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
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


if __name__ == "__main__":
    master_password = os.environ.get("MASTER_SECRET")

    if not master_password:
        raise ValueError("MASTER_SECRET environment variable is not set.")
