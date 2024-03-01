# from django.shortcuts import render

# # Create your views here.

import re

def count_characters(input_string):
    # Define a regular expression pattern to match any character
    pattern = re.compile(r'.')

    # Use the findall method to find all matches in the input string
    matches = pattern.findall(input_string)

    # Count the number of matches (characters) found
    character_count = len(matches)

    return character_count

# Example usage
input_string =r"""Displayed consistency in the production support and enhancement role for 7 critical supply chain apps for Kroger. 
-Ensured 100% business continuity via seamless implementation of Web Server Migration across 16 divisions. 
-Played key role in supporting modernization between 2 apps for forecast and order processing by working on 3 test cases across 8 period and guided new team members. 
-Prevented Buyers from under-ordering by Shipment sync across 2 different applications for 14 items. 
-Added RTA account reports in teams folder for 50+ locations and supported user issues in accessing the reports. 
-Disaster recovery testing for 2 applications that benefits to handle the application when servers goes down. 
-Handled 40+ job abends to ensure order processing and sending missing data, 30+ user requests providing the necessary updates and resolution.
-Helped in reducing 10+ abends by enhancing the existing process.
-As part of upskilling underwent hands on bootcamp on AWS dataengineer."""
#-For legacy migration, worked on phase mapping exercise for 150 components and migrating 12 vendors to modern apps in 2 phases.

result = count_characters(input_string)
print(f"The number of characters in the string is: {result}")

print(len(input_string))