import json
import pandas as pd
import requests

leads = pd.read_excel(r'C:\Users\Trist\Python\testLead.xlsx')

numLeads = len(leads.FirstName)

DEV = True
QA = False
PROD = False
    

for i in range(0, 1):

    firstName = leads.FirstName[i]
    lastName = leads.LastName[i]
    conditions = leads.Conditions[i]
    preg = leads.Preg[i]
    house = leads.Household[i]
    pov = leads.Pov[i]
    state = leads.State[i]
    zipcode = leads.Zipcode[i]
    phone = leads.Phone[i]
    age = leads.Age[i]
    email = leads.Email[i]

    if preg == "A":
        preg == "No"
    else:
        preg == "Yes"
     
    if age == "A":
        age = "Younger than 18"
    elif age == "B":
        age = "18 - 26"
    elif age == "C":
        age = "27 - 35"
    elif age == "D":
        age = "36 - 44"
    elif age == "E":
        age = "55 - 64"
    else:
        age = "65 or Older"
        
    if conditions == "A":
        conditions = "None"
    elif conditions == "B":
        conditions = "Cancer"
    elif conditions == "C":
        conditions = "Heart Attack"
    elif conditions == "D":
        conditions = "Stroke"
    elif conditions == "E":
        conditions = "Diabetes"
    elif conditions == "F":
        conditions = "AIDS/HIV"
    else:
        conditions = "Pulmonary Disease"


    house = int(house)
    phone = str(phone)
    zipcode = str(zipcode)
    state = str(state)
    age = str(age)
    conditions = str(conditions)
    pov = str(pov)
    firstName = str(firstName)
    lastName = str(lastName)
    preg = str(preg)
    email = str(email)
    true = True
    
    lead = {

      "event_id": "01DHM05XWS5SC06JT36PG2AV2W",
      "event_type": "form_response",
      "form_response": {
      
        "form_id": "N5fUMO",
        "token": "ld3hufmuzjg7j9fmlldekprq0d9mp3yp",
        "landed_at": "2019-08-06T17:37:58Z",
        "submitted_at": "2019-08-06T17:38:40Z",
        "hidden": {
          "keyword": ""
        },
        "calculated": {
          "score": 3
        },
        "definition": {
          "id": "N5fUMO",
          "title": "Perfect Health Plans (PROD)",
          "fields": [
           {
              "id": "a7GOltLW1i5K",
              "title": "What is your <strong>First Name?</strong>",
              "type": "short_text",
              "ref": "6f54a006-d0e7-4a2a-b739-f7a519beb639",
              "properties": {}
            },
            {
              "id": "x6xWTLetSswI",
              "title": "{{answer_134241467}}, have you or anyone on this policy ever had any of these conditions in the <strong>past</strong> <strong>5 years?</strong>",
              "type": "multiple_choice",
              "allow_multiple_selections": true,
              "ref": "e8c721b1-bcf3-44ca-912b-5797e67b1945",
              "properties": {},
              "choices": [
                {
                  "id": "WLF6EmSGheD6",
                  "label": "None"
                },
                {
                  "id": "jOdPQFqlslBz",
                  "label": "Cancer"
                },
                {
                  "id": "oPvR8oRv7ZeX",
                  "label": "Heart Attack"
                },
                {
                  "id": "LMW4lP8xZmO5",
                  "label": "Stroke"
                },
                {
                  "id": "HNxxg8gS3Xn7",
                  "label": "Diabetes"
                },
                {
                  "id": "Ap61oYKuUS7m",
                  "label": "AIDS/HIV"
                },
                {
                  "id": "mwXTl3yemGTd",
                  "label": "Pulmonary Disease"
                }
              ]
            },
            {
              "id": "ZnaCtHFgYbvo",
              "title": "Is anyone on this policy pregnant?",
              "type": "multiple_choice",
              "ref": "7b90869d-f02f-41d1-9e12-9fdd0a00bc75",
              "properties": {},
              "choices": [
              {
                  "id": "bh88j7Uby2nk",
                  "label": "No"
                },
                {
                  "id": "gkq0R9BDCsKA",
                  "label": "Yes"
                }
              ]
            },
            {
              "id": "uV9J9Ot5vzi1",
              "title": "How many people are in your household?",
              "type": "opinion_scale",
              "ref": "e83eac02-5d06-4c27-8d1c-3530c37eb6aa",
              "properties": {}
            },
            {
              "id": "MSyyJIC8jOrI",
              "title": "Good news! You could qualify for a subsidy to save thousands. <strong>What is your</strong> <strong>expected annual household income for 2019?</strong>",
              "type": "multiple_choice",
              "ref": "3ed4b9d1-d521-4fb7-97ab-4a6d93706288",
              "properties": {},
              "choices": [
                {
                  "id": "mKa1WPSjBXkt",
                  "label": "Below $20,000"
                },
                {
                  "id": "xVQAUSIWHt4A",
                  "label": "$20,000 - $39,999"
                },
                {
                  "id": "uo5i3PhnUTwq",
                  "label": "$40,000 - $60,999"
                },
                {
                  "id": "IVWLksUer4WC",
                  "label": "$61,000 - $80,999"
                },
                {
                  "id": "Hv9PqfpkZbhR",
                  "label": "$81,000 and Over"
                }
              ]
            },
            {
              "id": "QOwcHuKeGeSS",
              "title": "What <strong>State</strong> do you live in?",
              "type": "dropdown",
              "ref": "1309d5d7-b12c-49e1-bb1e-0852761b5972",
              "properties": {}
            },
            {
              "id": "ZhH0YTumTStR",
              "title": "What is your <strong>Zip Code?</strong>",
              "type": "short_text",
              "ref": "0947bdd1-86ae-4a6f-b8b3-8ca7a4f0a98f",
              "properties": {}
            },
            {
              "id": "LdgTweSqKyhj",
              "title": "Almost done {{answer_134241467}}! What is your <strong>Phone Number?</strong>",
              "type": "short_text",
              "ref": "7f14ecc4-ef41-4a50-b270-8950ac427a05",
              "properties": {}
            },
            {
              "id": "ZT26GCNwLssJ",
              "title": "What is your <strong>Email?</strong>",
              "type": "email",
              "ref": "5d5cf9ca-11c4-4f78-bfdf-c436d11099ce",
              "properties": {}
            },
            {
              "id": "hE2XbrGSTzzI",
              "title": "{{answer_134241467}}, what is your <strong>Last Name?</strong>",
              "type": "short_text",
              "ref": "9b327ea1-953b-4adc-bc2d-ba83300e4b8e",
              "properties": {}
            },
            {
              "id": "C6OJqgupe5KD",
              "title": "Please select your <strong>Age Range:</strong>",
              "type": "multiple_choice",
              "ref": "1fc23abc-f8d9-4757-98cd-f5233a548771",
              "properties": {},
              "choices": [
                          {
                  "id": "RHAYjroJtlas",
                  "label": "Younger than 18"
                },
                {
                  "id": "fXctG94ubWV5",
                  "label": "18 - 26"
                },
                {
                  "id": "qE2rsAqiT1E3",
                  "label": "27 - 35"
                },
                {
                  "id": "HxtoaPXjUf5G",
                  "label": "36 - 44"
                },
                {
                  "id": "d5nOTOq1T4Rn",
                  "label": "45 - 54"
                },
                {
                  "id": "LB0csRzY6bhT",
                  "label": "55 - 64"
                },
                {
                  "id": "j3J7CJBmLRNb",
                  "label": "65 or Older"
                }
              ]
            }
          ]
        },
        "answers": [
          {
            "type": "text",
            "text": firstName,
            "field": {
              "id": "a7GOltLW1i5K",
              "type": "short_text",
              "ref": "6f54a006-d0e7-4a2a-b739-f7a519beb639"
            }
          },
          {
            "type": "choices",
            "choices": {
              "labels": [
                "None"
              ]
            },
            "field": {
              "id": "x6xWTLetSswI",
              "type": "multiple_choice",
              "ref": "e8c721b1-bcf3-44ca-912b-5797e67b1945"
            }
          },
          {
            "type": "choice",
            "choice": {
              "label": preg
            },
            "field": {
              "id": "ZnaCtHFgYbvo",
              "type": "multiple_choice",
              "ref": "7b90869d-f02f-41d1-9e12-9fdd0a00bc75"
            }
          },
          {
            "type": "number",
            "number": house,
            "field": {
              "id": "uV9J9Ot5vzi1",
              "type": "opinion_scale",
              "ref": "e83eac02-5d06-4c27-8d1c-3530c37eb6aa"
            }
          },
          {
            "type": "choice",
            "choice": {
              "label": "$12,000 - $23,999"
            },
            "field": {
              "id": "MSyyJIC8jOrI",
              "type": "multiple_choice",
              "ref": "3ed4b9d1-d521-4fb7-97ab-4a6d93706288"
            }
          },
          {
            "type": "choice",
            "choice": {
              "label": state
            },
            "field": {
              "id": "QOwcHuKeGeSS",
              "type": "dropdown",
              "ref": "1309d5d7-b12c-49e1-bb1e-0852761b5972"
            }
          },
          {
            "type": "text",
            "text": zipcode,
            "field": {
              "id": "ZhH0YTumTStR",
              "type": "short_text",
              "ref": "0947bdd1-86ae-4a6f-b8b3-8ca7a4f0a98f"
            }
          },
          {
            "type": "text",
            "text": phone,
            "field": {
              "id": "LdgTweSqKyhj",
              "type": "short_text",
              "ref": "7f14ecc4-ef41-4a50-b270-8950ac427a05"
            }
          },
          {
            "type": "email",
            "email": email,
            "field": {
              "id": "ZT26GCNwLssJ",
              "type": "email",
              "ref": "5d5cf9ca-11c4-4f78-bfdf-c436d11099ce"
            }
          },
          {
            "type": "text",
            "text": lastName,
            "field": {
              "id": "hE2XbrGSTzzI",
              "type": "short_text",
              "ref": "9b327ea1-953b-4adc-bc2d-ba83300e4b8e"
            }
          },
          {
            "type": "choice",
            "choice": {
              "label": age
            },
            "field": {
              "id": "C6OJqgupe5KD",
              "type": "multiple_choice",
              "ref": "1fc23abc-f8d9-4757-98cd-f5233a548771"
            }
          }
        ]
      }
    }
    # Send to Json
    #
    x = json.dumps(lead)
    
    if DEV:
        r = requests.post('https://rk3kjvh7f8.execute-api.us-east-1.amazonaws.com/dev/v1/send', x)
        print(r)
        print(x)
    if QA:
        r = requests.post('https://rk3kjvh7f8.execute-api.us-east-1.amazonaws.com/qa/v1/send', x)
        print(r)
    if PROD and state == "Alaska": 
        r = requests.post('https://rk3kjvh7f8.execute-api.us-east-1.amazonaws.com/Live1/v1/send',x)
        print(r)
        
    #print(r.text)
    
    #print(json.dumps(lead))
    #print("\n")
    #print("\n")


