#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
   
    def __init__(self, name=None, breed=None):
        # Validate name
        if not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
            self.name = None
        elif len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            self.name = None
        else:
            self.name = name

        # Validate breed
        if breed and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        elif breed:  # Only set breed if it is valid
            self.breed = breed