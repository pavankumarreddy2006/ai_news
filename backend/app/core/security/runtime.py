from fastapi import Header, HTTPException


def validate_internal_api_key(x_internal_key: str | None = Header(default=None)) -> str | None:
    if x_internal_key == "":
        raise HTTPException(status_code=401, detail="Invalid internal key.")
    return x_internal_key

