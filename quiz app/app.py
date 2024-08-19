import random

from flask import Flask, render_template, request,redirect
import requests

app = Flask(__name__)

api_1 = {"data_science": "DATA SCIENCE", "deep_learning": "DEEP LEARNING"}
api_2 = {"gen_ai": "GEN AI", "sql": "SQL"}
api_3 = {"knowledge_engineering": "KNOWLEDGE ENGINEERING", "python": "PYTHON"}
api_4 = {"c": "C", "java": "JAVA"}
api_5 = {"machine_learning": "MACHINE LEARNING"}
api_6 = {"javascript": "JAVA SCRIPT", "datastructure": "DATA STRUCTURE"}
api_7 = {"blockchain": "BLOCK CHAIN", "cybersecurity": "CYBER SECURITY"}



@app.route('/', methods=["POST", "GET"])
def home():
    return render_template("home.html")


@app.route('/questions', methods=["POST", "GET"])
def quiz():
    # Handle the category selection
    global response
    global topic
    selected_category = request.form.get('category')
    limit = int(request.form.get('num_questions'))
    print(limit)
    if not selected_category:
        return redirect('/')
    if selected_category in api_1.keys():
        topic = api_1[selected_category]
        response = requests.get(f"https://66c1b30af83fffcb5879f8a7.mockapi.io/data_science/{selected_category}")
    elif selected_category in api_2.keys():
        topic = api_2[selected_category]
        response = requests.get(f"https://66c1c06bf83fffcb587a1c4f.mockapi.io/Data_science/{selected_category}")
    elif selected_category in api_3.keys():
        topic = api_3[selected_category]
        response = requests.get(f"https://66c0af2bba6f27ca9a5756aa.mockapi.io/insightify/{selected_category}")
    elif selected_category in api_4.keys():
        topic = api_4[selected_category]
        response = requests.get(f"https://66c1c31cf83fffcb587a2575.mockapi.io/{selected_category}")
    elif selected_category in api_5.keys():
        topic = api_5[selected_category]
        response = requests.get(f"https://66c1cc9df83fffcb587a3c01.mockapi.io/{selected_category}")
    elif selected_category in api_6.keys():
        topic = api_6[selected_category]
        response = requests.get(f"https://66c1cfc4f83fffcb587a44e3.mockapi.io/insightify/{selected_category}")
    elif selected_category in api_7.keys():
        topic = api_7[selected_category]
        response = requests.get(f"https://66c1e48af83fffcb587a8887.mockapi.io/insightify/{selected_category}")

    else:
        print("NO API FOUND FOR THIS CATEGORY")
    # Fetch the questions based on the category
    list_of_question = response.json()[:limit]
    random.shuffle(list_of_question)
    # Get the current question index
    question_index = int(request.args.get('question', 0))
    if question_index >= len(list_of_question) or question_index < 0:
        question_index = 0

    return render_template(
        'index.html',
        questions=list_of_question,
        current_question_index=question_index,
        total_questions=len(list_of_question),
        title=selected_category,
        topic=topic
    )


if __name__ == '__main__':
    app.run(debug=True)
