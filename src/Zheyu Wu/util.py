import pandas as pd
import numpy as np
import re



us_state_abbrev = {
    'alabama': 'al',
    'alaska': 'ak',
    'arizona': 'az',
    'arkansas': 'ar',
    'california': 'ca',
    'colorado': 'co',
    'connecticut': 'ct',
    'delaware': 'de',
    'florida': 'fl',
    'georgia': 'ga',
    'hawaii': 'hi',
    'idaho': 'id',
    'Illinois': 'il',
    'indiana': 'in',
    'iowa': 'ia',
    'kansas': 'ks',
    'kentucky': 'ky',
    'louisiana': 'la',
    'maine': 'me',
    'maryland': 'md',
    'massachusetts': 'ma',
    'michigan': 'mi',
    'minnesota': 'mn',
    'mississippi': 'ms',
    'missouri': 'mo',
    'montana': 'mt',
    'nebraska': 'ne',
    'nevada': 'nv',
    'new hampshire': 'nh',
    'new jersey': 'nj',
    'new mexico': 'nm',
    'new york': 'ny',
    'north carolina': 'nc',
    'north dakota': 'nd',
    'ohio': 'oh',
    'oklahoma': 'ok',
    'oregon': 'or',
    'pennsylvania': 'pa',
    'rhode island': 'ri',
    'south carolina': 'sc',
    'south dakota': 'sd',
    'tennessee': 'tn',
    'texas': 'tx',
    'utah': 'ut',
    'vermont': 'vt',
    'virginia': 'va',
    'washington': 'wa',
    'west virginia': 'wv',
    'wisconsin': 'wi',
    'wyoming': 'wy',
}

abbrev_to_states = {}
for key in us_state_abbrev.keys():
    abbrev_to_states[us_state_abbrev[key]] = key


# extract country and region from location
def parse_location(data):
    
    abbrev_to_states = {}
    for key in us_state_abbrev.keys():
        abbrev_to_states[us_state_abbrev[key]] = key
        
    country = []
    region = []
    j = 0
    for location in data['location']:
        j = j+1
        if location == 'Not available' or location == ' ':
            country.append('')
            #print(location)
            region.append('')
        else:
            location=location.replace('.','')
            location = location.lower()
            if ',' not in location:
                splitted_string = location.split()
                location = ' '.join(splitted_string[:-1])+','+splitted_string[-1]
            location_list = re.split(';| -|,|[|]|/',location)
            location_list = [i.strip() for i in location_list if i] 
            if 'chicago' in location_list and len(location_list)<2:
                location_list.append(abbrev_to_states['il'])
            if "boston" in location_list and len(location_list)>2:
                location_list.append(abbrev_to_states['ma'])
            #print(location_list)
            if location_list[-1] in abbrev_to_states or location_list[-1] in us_state_abbrev:
                country.append('usa')
                try:
                    region.append(abbrev_to_states[location_list[-1]])
                except:
                    region.append(location_list[-1])
            elif len(location_list)>=2 and (location_list[-2] in abbrev_to_states or location_list[-2] in us_state_abbrev):
                country.append('usa')
                try:
                    region.append(abbrev_to_states[location_list[-2]])
                except:
                    region.append(location_list[-2])
            
            else:
                if location_list[-1] == 'miami':
                    country.append('usa')
                    region.append('miami')
                elif location_list[-1] == 'brooklyn':
                    country.append('usa')
                    region.append('brooklyn')
                elif location_list[-1] == 'illinois':
                    country.append('usa')
                    region.append('illinois')
                elif location_list[-1] == 'carolina':
                    country.append('usa')
                    region.append('north carolina')
                elif location_list[-1] == 'boston':
                    country.append('usa')
                    region.append('boston')
                elif location_list[-1]=='states':
                    country.append('usa')
                    region.append('')
                elif location_list[-1]=='york':
                    country.append('usa')
                    region.append('new york')
                elif 'usa' in location_list[-1] or 'us' == location_list[-1]:
                    country.append('usa')
                    region.append(location_list[-1][:location_list[-1].find('U')])
                elif 'jersey' in location_list[-1]:
                    country.append('usa')
                    region.append('new jersey')
                elif 'lousiana' in location_list[-1]:
                    # misspell
                    country.append('usa')
                    region.append('louisiana')
                elif 'engla' == location_list[-1]:
                    country.append('england')
                    region.append(location_list[-2])
                elif 'massachusettes' in location_list[-1]:
                    country.append('usa')
                    region.append('massachusetts')
                elif "angels" in location_list[-1] or "barbara" in location_list[-1]:
                    country.append('usa')
                    region.append('california')
                elif "seattle" in location_list[-1]:
                    country.append('usa')
                    region.append('washington')
                elif 'katy' in location_list[-1]:
                    country.append('usa')
                    region.append('texas')
                elif location_list[-1] in us_state_abbrev:
                    country.append('usa')
                    region.append(location_list[-1])
                else:
                    country.append(location_list[-1])
                    if len(location_list) >= 2:
                        region.append(location_list[-2])
                    else:
                        region.append('')
    return country,region