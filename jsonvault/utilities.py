import secrets


def generate_key(nbytes=40):
    return secrets.token_urlsafe(nbytes)


if __name__ == '__main__':
    # token_urlsafe encoded in base64-- so an average of 1.3* the size.
    foo = generate_key()
    print(foo, len(foo))