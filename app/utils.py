import re

def validate_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def find_matches(user, all_users):
    return [
        potential_match
        for potential_match in all_users
        if user.gender != potential_match.gender and
           user.city == potential_match.city and
           set(user.interests.split(",")).intersection(set(potential_match.interests.split(",")))
    ]
