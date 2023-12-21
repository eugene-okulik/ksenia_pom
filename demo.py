from faker import Faker


def email():
    fake = Faker()
    first_name = fake.first_name_male()
    last_name = fake.last_name()
    return f"{first_name}.{last_name}@{fake.domain_name()}"


print(email())
