
from document_reader import read_document

text = read_document("documents/sample.txt")

budget = 0
preferred_fuel = ""
preferred_maintenance = ""
minimum_mileage = 0

for line in text.split("\n"):
    if "Maximum Budget:" in line:
        budget_text = line.split("Rs.")[1]
        budget = int(budget_text.replace(",", "").strip()) / 100000

    if "Preferred Fuel:" in line:
        preferred_fuel = line.split(":")[1].strip()

    if "Preferred Maintenance:" in line:
        preferred_maintenance = line.split(":")[1].strip()

    if "Minimum Mileage:" in line:
        minimum_mileage = int(line.split(":")[1].strip())

print("Customer Budget:", budget, "lakh")
print("Preferred Fuel:", preferred_fuel)
print("Preferred Maintenance:", preferred_maintenance)
print("Minimum Mileage:", minimum_mileage)


def read_cars():
    file = open("documents/cars.txt", "r", encoding="utf-8")
    car_text = file.read()
    file.close()

    car_records = car_text.split("\n\n")
    cars = []

    for record in car_records:
        car = {}

        for line in record.split("\n"):
            if line.startswith("Car ") and ":" in line:
                car["name"] = line.split(":", 1)[1].strip()

            elif line.startswith("Price:"):
                price_text = line.split("Rs.")[1]
                car["price"] = float(
                    price_text.split("lakh")[0].strip()
                )

            elif line.startswith("Fuel Type:"):
                car["fuel"] = line.split(":", 1)[1].strip()

            elif line.startswith("Mileage:"):
                mileage_text = line.split(":")[1].strip()
                car["mileage"] = float(mileage_text.split()[0])

            elif line.startswith("Maintenance:"):
                car["maintenance"] = line.split(":", 1)[1].strip()

            elif line.startswith("Safety:"):
                car["safety"] = line.split(":", 1)[1].strip()

        if "name" in car and "price" in car:
            if "fuel" in car and "mileage" in car:
                if "maintenance" in car and "safety" in car:
                    cars.append(car)

    return cars


cars = read_cars()

recommended_cars = []

for car in cars:
    score = 0

    if car["price"] <= budget:
        score = score + 1

        if car["fuel"].lower() == preferred_fuel.lower():
            score = score + 1

        if car["maintenance"].lower() == preferred_maintenance.lower():
            score = score + 1

        if car["mileage"] >= minimum_mileage:
            score = score + 1

    if score >= 3:
        car["score"] = score
        recommended_cars.append(car)


recommended_cars.sort(
    key=lambda car: (car["score"], car["mileage"]),
    reverse=True
)

print("\nRecommended Cars:")

if len(recommended_cars) == 0:
    print("No suitable cars found.")

for car in recommended_cars:
    print("\nCar:", car["name"])
    print("Price: Rs.", car["price"], "lakh")
    print("Fuel:", car["fuel"])
    print("Mileage:", car["mileage"])
    print("Maintenance:", car["maintenance"])
    print("Safety:", car["safety"])
    print("Score:", car["score"])
    print("--------------------")




file = open("documents/cars.txt", "r", encoding="utf-8")
car_text = file.read()
file.close()


query = input("\nAsk a question about cars: ").lower()


car_records = car_text.split("\n\n")

print("\nRelevant Car Information:")

found = False

for record in car_records:
    score = 0

    for word in query.split():
        if word in record.lower():
            score = score + 1

    if score > 0:
        print(record)
        print("--------------------")
        found = True

if found == False:
    print("No matching car information found.")
