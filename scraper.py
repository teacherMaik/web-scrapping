import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd
import re


def clean_text(text):
    if not text:
        return None
    # Strip leading/trailing whitespace and replace multiple whitespace chars with single space
    return ' '.join(text.split())

def clean_rule_text(rule):
    rule = rule.strip()

    # Remove spaces before punctuation like ., :, ,
    rule = re.sub(r'\s+([.,:])', r'\1', rule)

    # Ensure exactly one space after punctuation (except when it's the end)
    rule = re.sub(r'([.,:])(?!\s|$)', r'\1 ', rule)

    # Collapse multiple spaces into one
    rule = re.sub(r'\s{2,}', ' ', rule)

    return rule

# Wizards search urls for all lands
url_params = ['?page=0', '?page=1', '?page=2', '?page=3', '?page=4', '?page=5', '?page=6', '?page=7', '?page=8', '?page=9', '?page=10', '?page=11', '?page=0']

url_1 = 'https://gatherer.wizards.com/Pages/Search/Default.aspx?page=1&type=+[Land]'
response = requests.get(url_1)

soup_1 = BeautifulSoup(response.text, 'html.parser')
# print(soup_1)

card_rows = soup_1.find_all('tr', class_ = 'cardItem')

cards = []
colors = ['blue', 'white', 'red', 'black', 'green', 'colorless']
basics = ['mountain', 'island', 'swamp', 'forest', 'plains']

# for row in card_rows:

for i in range(12):

    row = card_rows[i]
    card = {}

    link = None
    link_tag = row.find('a')
    if link_tag:
        link = link_tag['href']

        link_img = link_tag.find('img')
        card_name = link_img['alt']
        card['name'] = card_name
    
    card_info_tag = row.find('td', class_= 'middleCol')
    if card_info_tag:

        type_tag = card_info_tag.find('span', class_ = 'typeLine')
        if type_tag:
            card_type = type_tag.string
            cleaned_card_type = clean_text(card_type)
            card['types'] = cleaned_card_type

        rules_div = card_info_tag.find('div', class_ = 'rulesText')
        if rules_div:
            rules_tags = rules_div.find_all('p')

            mana_pool = []
            card_rules = []
            for rules_tag in rules_tags:

                rules_tag_parts = []
                for child in rules_tag.descendants:

                    if isinstance(child, Tag) and child.name == 'img' and child.has_attr('alt'):

                        rules_tag_parts.append(child['alt'])
                    elif isinstance(child, NavigableString):

                        rules_tag_parts.append(child.strip())

                full_rule = ' '.join(part for part in rules_tag_parts if part).replace('  ', ' ')
                cleaned_full_rule = clean_rule_text(full_rule)
                card_rules.append(cleaned_full_rule)

                lower_rule = full_rule.lower()
                if 'add' in lower_rule or 'search your library for' in lower_rule:
                    
                    for color in colors:
                        if color in lower_rule:
                            mana_pool.append(color)

                    for basic in basics:
                        if basic in lower_rule:
                            if basic == 'mountain':
                                mana_pool.append('red')
                            elif basic == 'swamp':
                                mana_pool.append('black')
                            elif basic == 'island':
                                mana_pool.append('blue')
                            elif basic == 'forest':
                                mana_pool.append('green')
                            elif basic == 'plains':
                                mana_pool.append('white')

            
            card['mana-pool'] = mana_pool
            card['rules'] = card_rules

    sets_div = row.find('td', class_ = 'rightCol')
    if sets_div:
        current_set_tag = sets_div.find('div', class_ = 'rightCol')
        current_set_img = current_set_tag.find('img')
        card['recent-set'] = current_set_img['alt']

        other_sets_tag = sets_div.find('div', class_ = 'otherSetSection')
        if other_sets_tag:
            other_sets_imgs = other_sets_tag.find_all('img')
            other_sets = []
            for img in other_sets_imgs:

                other_sets.append(img['alt'])

            card['other-sets'] = other_sets

    card['link'] = link
    print(card)
    cards.append(card)

# print(cards)