import numpy as np
import argparse
import csv


def generate_data(num_employees=100, seed=42):
    np.random.seed(seed)
    salaries = np.random.randint(30000, 120000, num_employees)
    departments = np.random.choice([0, 1, 2, 3], size=num_employees)
    return salaries, departments


def dept_name(dept_id):
    return {0: "HR", 1: "IT", 2: "Sales", 3: "Finance"}.get(dept_id, "Unknown")


def analyze_overall(salaries):
    print(" Overall Salary Stats")
    print("Average Salary: ${:.2f}".format(np.mean(salaries)))
    print("Max Salary: ${}".format(np.max(salaries)))
    print("Min Salary: ${}".format(np.min(salaries)))


def analyze_by_department(salaries, departments):
    print("\n Department-wise Stats:")
    for dept in range(4):
        dept_salaries = salaries[departments == dept]
        print(
            f"{dept_name(dept)} - Count: {len(dept_salaries)}, "
            f"Avg: ${np.mean(dept_salaries):.2f}, "
            f"Max: ${np.max(dept_salaries)}"
        )


def find_high_earners(salaries, threshold=100000):
    high_earners = np.where(salaries > threshold)[0]
    print(f"\n Employees earning above ${threshold}: {len(high_earners)}")
    return high_earners


def export_to_csv(salaries, departments, filename="salary_details.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Employee ID", "Department", "Salary"])
        for i, (dept, sal) in enumerate(zip(departments, salaries)):
            writer.writerow([i + 1, dept_name(dept), sal])
    print(f"\n Data exported to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Analyze employee salary data.")
    parser.add_argument(
        "--summary", action="store_true", help="Show overall salary summary"
    )
    parser.add_argument(
        "--departments", action="store_true", help="Show department-wise stats"
    )
    parser.add_argument("--high-earners", action="store_true", help="Show high earners")
    parser.add_argument("--export", action="store_true", help="Export data to CSV")
    parser.add_argument(
        "--count", type=int, default=100, help="Number of employees to simulate"
    )

    args = parser.parse_args()
    salaries, departments = generate_data(num_employees=args.count)

    if args.summary:
        analyze_overall(salaries)

    if args.departments:
        analyze_by_department(salaries, departments)

    if args.high_earners:
        find_high_earners(salaries)

    if args.export:
        export_to_csv(salaries, departments)


if __name__ == "__main__":
    main()
