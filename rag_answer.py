
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def generate_answer(query, car_text):
    query_words = query.lower().split()
    car_records = car_text.split("\n\n")

    relevant_records = []

    for record in car_records:
        score = 0

        for word in query_words:
            if len(word) > 2 and word in record.lower():
                score = score + 1

        if score > 0:
            relevant_records.append(record)

    if len(relevant_records) == 0:
        return "Sorry, no relevant car information found."

    context = "\n\n".join(relevant_records)

    prompt = """
    You are a helpful car buying assistant.

    Answer the customer's question using only the car information below.
    If the information is not available, say so.
    Do not invent car specifications.

    Car Information:
    """ + context + """

    Customer Question:
    """ + query

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    file = open("documents/cars.txt", "r", encoding="utf-8")
    car_text = file.read()
    file.close()

    query = input("Ask a question about cars: ")

    answer = generate_answer(query, car_text)

    print("\nAnswer:")
    print(answer)
