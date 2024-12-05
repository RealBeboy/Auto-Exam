import requests

#Justine+Roy+P.+Salvador
# Function to generate the URL with answers
def generate_url(base_url, answers):
    query_params = "&".join([f"question{i+1}={answer}" for i, answer in enumerate(answers)])
    return f"{base_url}&{query_params}"

# Main function to submit answers
def submit_answers():

    base_url = "http://122.3.185.245:8081/ROXRUQA/submitprocess.php?grade=11&schoolid=1&name=Justine+Roy+P.+Salvador&subject=Grade+12+-+Values+Education+2Q+RUQA+FINAL+QUESTIONS.pdf"
    
    # List of answers; customize these answers as needed
    answers = [
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "a",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "a",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b",
  "b"
]
    
    # Generate the complete URL
    full_url = generate_url(base_url, answers)
    
    # Print the final URL
    print("Generated URL:")
    print(full_url)
    
    # Submit the URL via HTTP GET request
    try:
        response = requests.get(full_url)
        if response.status_code == 200:
            print("Answers submitted successfully!")
        else:
            print(f"Failed to submit answers. HTTP Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    submit_answers()
