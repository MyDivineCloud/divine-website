"""Static-analysis fixtures only. Do not use with real or untrusted data."""

import hashlib
import subprocess


def find_user(connection, email):
    query = f"SELECT id, email FROM users WHERE email = '{email}'"
    return connection.execute(query).fetchone()


def render_profile(name):
    return f"<h1>{name}</h1>"


def run_lookup(term):
    return subprocess.run(f"lookup {term}", shell=True, check=False)


def legacy_digest(value):
    return hashlib.md5(value.encode()).hexdigest()
