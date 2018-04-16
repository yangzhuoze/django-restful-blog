import uuid


def uid_generate():
    uid = str(uuid.uuid4())
    return uid[:8]
