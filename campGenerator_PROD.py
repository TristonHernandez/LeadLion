import json
import pandas as pd
import requests

camps = pd.read_excel(r'C:\Users\Trist\Python\testCampPROD.xlsx')

numCamps = len(camps.FirstName)

DEV = False
QA = False
PROD = True

true = True

for i in range(0, numCamps):

    firstName = str(camps.FirstName[i])
    lastName = str(camps.LastName[i])
    campName = str(camps.CampName[i])
    states = str(camps.States[i])
    budget = str(camps.Budget[i])
    email = str(camps.Email[i])
    phone = str(camps.Phone[i])
    crm = str(camps.CRM[i])
    crmorsms = str(camps.CRMorSMS[i])


    camp = {

        "event_id": "01DHVND4KEDNNNE3AQ4RG2E3JR",
        "event_type": "form_response",
        "form_response": {
            "form_id": "xZ5x8a",
            "token": "ig759dr919j8mq08cej2ig75wb86p3yw",
            "landed_at": "2019-08-09T17:03:53Z",
            "submitted_at": "2019-08-09T17:04:17Z",
            "hidden": {
              "uid": "xxxxx"
            },
            "definition": {
                "id": "xZ5x8a",
                "title": "LL-EX-PROD-CAMPAIGN (Dev)",
                "fields": [
                    {
                        "id": "ZdnHJubc879C",
                        "title": "What is your <strong>First</strong> Name?",
                        "type": "short_text",
                        "ref": "0d6c692a-27cb-4fb0-86c9-50f854a0e0d0",
                        "properties": {}
                    },
                    {
                      "id": "JtwQTxPH7VyX",
                      "title": "What is your <strong>Last</strong> Name?",
                      "type": "short_text",
                      "ref": "b76b612d-341d-4a16-8d2f-fb5428bdb054",
                      "properties": {}
                    },
                    {
                      "id": "GEa7zD6xdNSE",
                      "title": "What is the name of <strong>Campaign</strong>?",
                      "type": "short_text",
                      "ref": "5a792c23-b51e-4e99-ac5a-44f1e9493677",
                      "properties": {}
                    },
                    {
                      "id": "vqdqfHL1At09",
                      "title": "{{answer_137946325}}, select <strong>ALL</strong> of the states you sell in:",
                      "type": "multiple_choice",
                      "allow_multiple_selections": true,
                      "ref": "ba7d3dc7-032b-47e9-9c7c-f72f8d2c6731",
                      "properties": {},
                      "choices": [
                        {
                          "id": "dyxWRmMx2i5w",
                          "label": "Alabama"
                        },  
                        {
                          "id": "G4hEq3LLeaIn",
                          "label": "Alaska"
                        },
                        {
                          "id": "pI1uqAMJk9Vv",
                          "label": "Arizona"
                        },
                        {
                          "id": "wJvyBzBjisXD",
                          "label": "Arkansas"
                        },
                        {
                          "id": "cngtZ8tTa9zm",
                          "label": "California"
                        },
                        {
                          "id": "nyEYNyuGmqVc",
                          "label": "Colorado"
                        },
                        {
                          "id": "kZRBLe1fSP6r",
                          "label": "Connecticut"
                        },
                        {
                          "id": "m5lKRLI4QeaK",
                          "label": "Delaware"
                        },
                        {
                          "id": "V0Fwoppza1d8",
                          "label": "Dist. of Columbia"
                        },
                        {
                          "id": "etAiXGS1r6NY",
                          "label": "Florida"
                        },
                        {
                          "id": "veQ8BiY4AVtr",
                          "label": "Georgia"
                        },
                        {
                          "id": "IppxQrAmvYJj",
                          "label": "Hawaii"
                        },
                        {
                          "id": "jpZS2leALh2r",
                          "label": "Idaho"
                        },
                        {
                          "id": "ruaUleIV0D7v",
                          "label": "Illinois"
                        },
                        {
                          "id": "jYGXM8xSVzo0",
                          "label": "Indiana"
                        },
                        {
                          "id": "RvnkZ0g0mNx5",
                          "label": "Iowa"
                        },
                        {
                          "id": "dQA2aOTfmm9X",
                          "label": "Kansas"
                        },
                        {
                          "id": "OBzcnxCkdGiA",
                          "label": "Kentucky"
                        },
                        {
                          "id": "O1ZxW7x9nwPL",
                          "label": "Louisiana"
                        },
                        {
                          "id": "VCCI2gxdaC7u",
                          "label": "Maine"
                        },
                        {
                          "id": "SFNyF96GJgTp",
                          "label": "Maryland"
                        },
                        {
                          "id": "Nk7ZJgAWm6lz",
                          "label": "Massachusetts"
                        },
                        {
                          "id": "vtCUpAGue2LK",
                          "label": "Michigan"
                        },
                        {
                          "id": "r2eEBU79nEgq",
                          "label": "Minnesota"
                        },
                        {
                          "id": "gaFuWqiNf8cC",
                          "label": "Mississippi"
                        },
                        {
                          "id": "elmbI7RHJIsa",
                          "label": "Missouri"
                        },
                        {
                          "id": "XoEKweHiy66f",
                          "label": "Montana"
                        },
                        {
                          "id": "LlTgYwdqnWa0",
                          "label": "Nebraska"
                        },
                        {
                          "id": "UBGfzKqvrgIy",
                          "label": "Nevada"
                        },
                        {
                          "id": "ffEqy3P204rx",
                          "label": "New Hampshire"
                        },
                        {
                          "id": "gIVA556AoCOw",
                          "label": "New Jersey"
                        },
                        {
                          "id": "frpFWWa0TQde",
                          "label": "New Mexico"
                        },
                        {
                          "id": "IpE56D5nHZcw",
                          "label": "New York"
                        },
                        {
                          "id": "jjclYEBFLIbD",
                          "label": "North Carolina"
                        },
                        {
                          "id": "HijthUkV8uhR",
                          "label": "North Dakota"
                        },
                        {
                          "id": "z0brDFoQ3BJt",
                          "label": "Ohio"
                        },
                        {
                          "id": "SMGKpWjZtgFC",
                          "label": "Oklahoma"
                        },
                        {
                          "id": "nRWpZ0polqNQ",
                          "label": "Oregon"
                        },
                        {
                          "id": "ux2mLRzysaIM",
                          "label": "Pennsylvania"
                        },
                        {
                          "id": "bkkUJMGm0TIF",
                          "label": "Rhode Island"
                        },
                        {
                          "id": "BCduPmi7JZYu",
                          "label": "South Carolina"
                        },
                        {
                          "id": "VjvLWxJ13828",
                          "label": "South Dakota"
                        },
                        {
                          "id": "sdxrLLxWYq1X",
                          "label": "Tennessee"
                        },
                        {
                          "id": "Uag2QjiBvzTy",
                          "label": "Texas"
                        },
                        {
                          "id": "DpSdX4Ze9tCY",
                          "label": "Utah"
                        },
                        {
                          "id": "whAdFt4C8SDm",
                          "label": "Vermont"
                        },
                        {
                          "id": "PD1pmQWO044b",
                          "label": "Virginia"
                        },
                        {
                          "id": "uuERECJOIf0i",
                          "label": "Washington"
                        },
                        {
                          "id": "bJBG0NlcW23l",
                          "label": "West Virginia"
                        },
                        {
                          "id": "d7hik4CppMpC",
                          "label": "Wisconsin"
                        },
                        {
                          "id": "BjEelEtQPOg0",
                          "label": "Wyoming"
                        }
                    ]
                },
                {
                  "id": "yiLLfGYKn7bO",
                  "title": "<strong>Exclusive Leads:</strong><br>1. Real Time Delivery <br>2. No Pre-Existing Conditions <br>3. Poverty Level of 200 percent or greater<br>4. Not Pregnant   <br><br>Lead Parameters <br>-First Name-Last Name-Income-Household<br>-Phone Number-Email-State-Zip-Age Range-Keyword<br>",
                  "type": "multiple_choice",
                  "ref": "3bef3e1f-ab57-4923-92b6-23d95530d558",
                  "properties": {},
                  "choices": [
                    {
                      "id": "LDaTtrCyhPrZ",
                      "label": "I Accept"
                    }
                  ]
                },
                {
                  "id": "cZUC87tZVmoB",
                  "title": "Select your exclusive lead budget:",
                  "type": "multiple_choice",
                  "ref": "89631f07-7b3b-483a-b488-d26e30f9d205",
                  "properties": {},
                  "choices": [
                    {
                      "id": "kBcBCf5nwgsS",
                      "label": "$100"
                    },
                    {
                      "id": "xy4xksj0q7V2",
                      "label": "$200"
                    },
                    {
                      "id": "nwj4Sx0nPsAR",
                      "label": "$300"
                    },
                    {
                      "id": "tAV4zfw1FUbg",
                      "label": "$500"
                    },
                    {
                      "id": "v4CooH4YDUcb",
                      "label": "$750"
                    },
                    {
                      "id": "jeRgsppMBsNb",
                      "label": "$1,000"
                    },
                    {
                      "id": "QpXgFDAHrHaV",
                      "label": "$1,500"
                    },
                    {
                      "id": "kq8RPfP7jevt",
                      "label": "$2,000"
                    },
                    {
                      "id": "ExYdSrffpiFL",
                      "label": "$3,000"
                    },
                    {
                      "id": "SLojqmSaU3D5",
                      "label": "$4,000"
                    },
                    {
                      "id": "rwzlysScDeRj",
                      "label": "$5,000"
                    },
                    {
                      "id": "p5eXD7uwnzee",
                      "label": "$7,500"
                    },
                    {
                      "id": "In9wtF4KBgqO",
                      "label": "$10,000"
                    }
                  ]
                },
                {
                  "id": "pIYaBqUFm0jD",
                  "title": "<strong>Email</strong> of agent receiving leads:",
                  "type": "short_text",
                  "ref": "e11eab3a47e3a777",
                  "properties": {}
                },
                {
                  "id": "rzoseRPMf7Gk",
                  "title": "<strong>Email</strong> for <strong>receipt</strong>:",
                  "type": "email",
                  "ref": "bbed68c8-c9d9-4141-8750-181459d61767",
                  "properties": {}
                },
                {
                  "id": "oOf5GPgaDabS",
                  "title": "<strong>Phone Number</strong> of agent receiving leads",
                  "type": "phone_number",
                  "ref": "85f68952-527b-4c63-b0cf-2abfaa4707fc",
                  "properties": {}
                },
                {
                  "id": "oeZTMt90dIZZ",
                  "title": "Please choose how you would like to receive your leads:",
                  "type": "multiple_choice",
                  "allow_multiple_selections": true,
                  "ref": "7c79f1e5-1a89-4953-bc75-0fbb8d49e4b0",
                  "properties": {},
                  "choices": [
                    {
                      "id": "w8xTYvnL0zi8",
                      "label": "CRM"
                    },
                    {
                      "id": "KlZUN8PXxAQz",
                      "label": "SMS (text)"
                    }
                  ]
                },
                {
                  "id": "NiVevU1TiMUO",
                  "title": "Please provide CRM Webhook from your Admin associated with The Lead Lion:",
                  "type": "short_text",
                  "ref": "810bf3f7-2111-4e70-88b2-da418d3e03e7",
                  "properties": {}
                }
              ]
            },
            "answers": [
              {
                "type": "text",
                "text": firstName,
                "field": {
                  "id": "ZdnHJubc879C",
                  "type": "short_text",
                  "ref": "0d6c692a-27cb-4fb0-86c9-50f854a0e0d0"
                }
              },
              {
                "type": "text",
                "text": lastName,
                "field": {
                  "id": "JtwQTxPH7VyX",
                  "type": "short_text",
                  "ref": "b76b612d-341d-4a16-8d2f-fb5428bdb054"
                }
              },
              {
                "type": "text",
                "text": campName,
                "field": {
                  "id": "GEa7zD6xdNSE",
                  "type": "short_text",
                  "ref": "5a792c23-b51e-4e99-ac5a-44f1e9493677"
                }
              },
                    {
                "type": "choices",
                "choices": {
                  "labels": [
                    states
                  ]
                },
                "field": {
                  "id": "vqdqfHL1At09",
                  "type": "multiple_choice",
                  "ref": "ba7d3dc7-032b-47e9-9c7c-f72f8d2c6731"
                }
              },
              {
                "type": "choice",
                "choice": {
                  "label": "I Accept"
                },
                "field": {
                  "id": "yiLLfGYKn7bO",
                  "type": "multiple_choice",
                  "ref": "3bef3e1f-ab57-4923-92b6-23d95530d558"
                }
              },
              {
                "type": "choice",
                "choice": {
                  "label": budget
                },
                "field": {
                  "id": "cZUC87tZVmoB",
                  "type": "multiple_choice",
                  "ref": "89631f07-7b3b-483a-b488-d26e30f9d205"
                }
              },
              {
                "type": "text",
                "text": email,
                "field": {
                  "id": "pIYaBqUFm0jD",
                  "type": "short_text",
                  "ref": "e11eab3a47e3a777"
                }
              },
              {
                "type": "email",
                "email": email,
                "field": {
                  "id": "rzoseRPMf7Gk",
                  "type": "email",
                  "ref": "bbed68c8-c9d9-4141-8750-181459d61767"
                }
              },
              {
                "type": "phone_number",
                "phone_number": phone,
                "field": {
                  "id": "oOf5GPgaDabS",
                  "type": "phone_number",
                  "ref": "85f68952-527b-4c63-b0cf-2abfaa4707fc"
                }
              },
              {
                "type": "choices",
                "choices": {
                  "labels": [
                    "CRM",
                    "SMS (text)"
                  ]
                },
                "field": {
                  "id": "oeZTMt90dIZZ",
                  "type": "multiple_choice",
                  "ref": "7c79f1e5-1a89-4953-bc75-0fbb8d49e4b0"
                }
              },
              {
                "type": "text",
                "text": crm,
                "field": {
                  "id": "NiVevU1TiMUO",
                  "type": "short_text",
                  "ref": "810bf3f7-2111-4e70-88b2-da418d3e03e7"
                }
              }
            ]
        }
    }
    
    x = json.dumps(camp)
   # Send to API gateways here --------
    
