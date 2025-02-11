import requests
import pandas as pd

def generate_recent_contests(weekly_latest=None, biweekly_latest=None):
    contests = []
    if weekly_latest is not None:
        for i in range(weekly_latest, weekly_latest - 20, -1):
            contests.append(f"weekly-contest-{i}")
    if biweekly_latest is not None:
        for i in range(biweekly_latest, biweekly_latest - 10, -1):
            contests.append(f"biweekly-contest-{i}")
    
    return contests

def fetch_contest_questions(contest_slug):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    query = {
        "query": """
        query getContestQuestions($titleSlug: String!) {
          contest(titleSlug: $titleSlug) {
            title
            questions {
              title
              questionId
              credit
            }
          }
        }
        """,
        "variables": {"titleSlug": contest_slug}
    }
    
    response = requests.post(url, json=query, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch data for contest: {contest_slug}.")
        return []
    
    data = response.json().get("data", {}).get("contest", {})
    return data.get("questions", [])

def extract_questions(weekly_latest=None, biweekly_latest=None, mark=None):
    contests = generate_recent_contests(weekly_latest, biweekly_latest)
    selected_questions = []
    
    for contest_slug in contests:
        questions = fetch_contest_questions(contest_slug)
        for question in questions:
            if question.get("credit", 0) == mark:
                selected_questions.append({
                    "Contest": contest_slug,
                    "Question": question["title"],
                    "Question ID": question["questionId"]
                })
    
    return selected_questions

def save_to_excel(weekly_latest=None, biweekly_latest=None, mark=None):
    questions = extract_questions(weekly_latest, biweekly_latest, mark)
    if not questions:
        print(f"No {mark}-point questions found.")
        return
    
    filename = f"leetcode_{mark}_mark_questions.xlsx"
    df = pd.DataFrame(questions)
    df.to_excel(filename, index=False)
    print(f"Saved to {filename}")

if __name__ == "__main__":
    weekly_input = input("Enter the latest Weekly Contest number: ").strip()
    biweekly_input = input("Enter the latest Biweekly Contest number: ").strip()
    mark_input = input("Enter the mark of the questions to extract: ").strip()
    
    weekly_latest = int(weekly_input) if weekly_input.isdigit() else None
    biweekly_latest = int(biweekly_input) if biweekly_input.isdigit() else None
    mark = int(mark_input) if mark_input.isdigit() else None
    
    if (weekly_latest is None and biweekly_latest is None) or mark is None:
        print("No contest numbers or mark provided. Exiting.")
    else:
        save_to_excel(weekly_latest, biweekly_latest, mark)