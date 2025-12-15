class Patient:
    def __init__(self, name, urgent=False):
        self.name = name
        self.urgent = urgent
        self.next = None

class HospitalQueue:
    def __init__(self):
        self.head = None

    def add_patient(self, name, urgent=False):
        new_patient = Patient(name, urgent)

        if self.head is None or urgent:
            new_patient.next = self.head
            self.head = new_patient
            return

        current = self.head
        while current.next and not current.next.urgent:
            current = current.next

        new_patient.next = current.next
        current.next = new_patient

    def serve_patient(self):
        if self.head is None:
            print("Черга порожня")
            return
        served = self.head
        self.head = self.head.next
        print("Прийнято пацієнта:", served.name)

    def show_queue(self):
        current = self.head
        print("Черга пацієнтів:")
        while current:
            status = "Терміново" if current.urgent else "Звичайний"
            print(f"{current.name} ({status})")
            current = current.next

def main():
    queue = HospitalQueue()

    queue.add_patient("Іван")
    queue.add_patient("Марія")
    queue.add_patient("Олег", urgent=True)
    queue.add_patient("Анна")

    queue.show_queue()
    queue.serve_patient()
    queue.show_queue()

if __name__ == "__main__":
    main()
