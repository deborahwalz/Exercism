class PhoneNumber:
    """Clean up user-entered phone numbers so that they can be sent SMS messages"""

    def __init__(self, number):
        self.number = self.clean_validate(number)
        self.area_code = self.number[:3]      

    def clean_validate(self, number):
        number = (number.lstrip("+1")
            .replace(" ", "")
            .replace("-", "")
            .replace("(", "")
            .replace(")", "")
            .replace(".", "")
        )
        if (len(number) != 10) or (number[0] in ["0", "1"]) or (number[3] in ["0", "1"]):
            raise ValueError("Number not valid!")
        return number

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"

