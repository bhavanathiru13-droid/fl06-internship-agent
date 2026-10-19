
from pathlib import Path

def main():
    print("=" * 55)
    print("     INTERNSHIP ASSIGNMENT ASSISTANT")
    print("=" * 55)

    assignment_file = Path("assignment.txt")

    if not assignment_file.exists():
        print("\nERROR: assignment.txt was not found.")
        print("Create assignment.txt in the project folder.")
        return

    assignment = assignment_file.read_text(encoding="utf-8")

    print("\n1. ASSIGNMENT DETAILS")
    print("-" * 55)
    print(assignment)

    print("\n2. REQUIRED DELIVERABLE CHECKLIST")
    print("-" * 55)

    deliverables = [
        "Read assignment information from a local file",
        "Display the assignment details",
        "Identify the next action for the user",
        "Handle a missing assignment file safely",
        "Test the agent and record the results"
    ]

    for number, item in enumerate(deliverables, start=1):
        print(f"[ ] {number}. {item}")

    print("\n3. RECOMMENDED NEXT ACTION")
    print("-" * 55)
    print("Review the official FL-07 requirements.")
    print("Complete each deliverable and verify it before marking it done.")

    print("\nAgent run completed successfully.")

if __name__ == "__main__":
    main()
