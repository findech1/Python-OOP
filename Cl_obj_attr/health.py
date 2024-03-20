class HealthWorker:
    def __init__(self, name, nurse, doctor):
        self.name = name
        self.nurse = nurse
        self.doctor = doctor

    def display_info(self):
        pass  # This will be overridden by the subclasses


class Doctor(HealthWorker):
    def display_info(self):
        print(f"{self.name} is a doctor.")


class Nurse(HealthWorker):
    def display_info(self):
        print(f"{self.name} is a nurse.")


class ClinicalOfficer(HealthWorker):
    def display_info(self):
        print(f"{self.name} is a clinical officer.")


# Example usage
doctor = Doctor("Mercy")
nurse = Nurse("John")
clinical_officer = ClinicalOfficer("Alice")

doctor.display_info()  # Output: Mercy is a doctor.
nurse.display_info()   # Output: John is a nurse.
clinical_officer.display_info()  # Output: Alice is a clinical officer.