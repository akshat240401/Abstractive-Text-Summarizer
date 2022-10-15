#!/usr/local/bin/python
# coding=utf8

import os, sys
from urllib import response
import requests


API_URL = "https://api-inference.huggingface.co/models/lidiya/bart-large-xsum-samsum"
headers = {"Authorization": f"Bearer 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"}


data='''
भारत–भूमि
की महानता उसकी विशाल जनसंख्या अथवा भू–क्षेत्र के कारण नहीं, अपितु उसकी भव्य और अनुकरणीय उदार परम्पराओं के कारण रही है। आचार, विचार, चिन्तन, भाषा और वेशभूषा की विविधताओं को राष्ट्रीयता के सूत्र में पिरोकर भारत ने मानवीय एकता का आदर्श उपस्थित किया है।धर्म के तत्व भारतीय मान्यता के अनुसार धैर्य, क्षमा, आत्मसंयम, चोरी न करना, पवित्र भावना, इन्द्रियों पर नियन्त्रण बुद्धिमत्ता, विद्या, सत्य और क्रोध न करना ये धर्म के दस लक्षण हैं।
'''


def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
	"inputs": data,
	
})
print(output)
