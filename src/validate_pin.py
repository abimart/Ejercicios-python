def validate_pin(pin):
    if len(str(pin)) in (4, 6) and str(pin).isdigit():
        return True
    else:
        return False

if __name__ == "__main__":
    validate_pin()