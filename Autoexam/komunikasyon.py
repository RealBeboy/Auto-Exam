import requests

#Justine+Roy+P.+Salvador
# Function to generate the URL with answers
def generate_url(base_url, answers):
    query_params = "&".join([f"question{i+1}={answer}" for i, answer in enumerate(answers)])
    return f"{base_url}&{query_params}"

# Main function to submit answers
def submit_answers():

    base_url = "http://122.3.185.245:8081/ROXRUQA/submitprocess.php?grade=11&schoolid=1&name=Justine+Roy+P.+Salvador&subject=Komunikasyon+at+Pananaliksik+Baitang+11.pdf"
    
    # List of answers; customize these answers as needed
    answers = [
    "c",  # 21. batay sa pinag-uusapan
    "d",  # 22. Huwag pakatiwala, sapagkat marami pang maaaring mangyari
    "d",  # 23. kaluwalhatian
    "c",  # 24. Kusang nawawala ang galit o poot sa paglipas ng panahon
    "b",  # 25. upang
    "b",  # 26. sapagkat
    "a",  # 27. Kung gayon
    "d",  # 28. withdrawal slip
    "c",  # 29. faculty room
    "b",  # 30. Etnolek
    "d",  # 31. walwal
    "a",  # 32. dalubwika
    "a",  # 33. Social Media and Internet
    "a",  # 34. Google
    "c",  # 35. Edi wow!
    "a",  # 36. panghihinayang
    "a",  # 37. walang pera
    "b",  # 38. kahawig
    "c",  # 39. Interes ng mananaliksik at napapanahong paksa
    "d",  # 40. Layunin at Kahalagahan ng Pag-aaral
    "c",  # 41. Sakop at Limitasyon ng Pag-aaral
    "d",  # 42. Malaman kung swak (tanggap) o ligwak (di-tanggap) para sa mga mag-aaral sa baitang 11 ng Don Luis Ababa Senior High School ang pagsasalin sa wikang Taglish ng Pinoy New Testament.
    "a",  # 43. Dapat ang layunin ng pananaliksik ay batay sa suliraning inilahad sa bahagi ng Paglalahad ng Suliranin.
    "c",  # 44. Iminumungkahi ng mga mananaliksik na gamitin ang Pinoy NT na may Taglish na pagsasalin upang malinang at tumibay pa ang pananampalataya ng mga kabataang Pilipino.
    "d",  # 45. Social Media Capital of the World
    "a",  # 46. Malikhain ang mg Pilipino na paglikha ng mga salita.
    "d",  # 47. pagsabay sa pag-unlad ng teknolohiya
    "c",  # 48. para maging bukas ang isipan at mapanuri sa mga balita bago humusga at maiwasan ang fake new
    "a",  # 49. ebolusyon ng wika
    "a",  # 50. broadcasting
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
