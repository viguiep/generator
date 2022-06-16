# Story generator in Streamlit with form

import streamlit as st
import random



# ******************************************
# VARIABLES
# ******************************************
from utils.data import generate_fields, generate_descriptions, generate_suggestions

MY_FIELDS = generate_fields()
MY_DESCRIPTIONS = generate_descriptions()
MY_SUGGESTIONS = generate_suggestions()


# ******************************************
# BEGINNING
# ******************************************
st.title('Story generator (Fairytale)')

with open('story.txt') as f:
    SENTENCES = f.readlines()

if st.button('GENERATE STORY'):
    # CAVEAT: no replacement name can be part of another one... (since it would be replaced too)
    animal_lowercase = st.session_state['animal_lowercase']
    hero_gender = st.session_state['hero_gender']
    if animal_lowercase: # SHOULD BE COMPULSORY TO HAVE AN ANIMAL => ADAPT THE CODE
        st.session_state['animal_plural'] = animal_lowercase + 's' # IMPROVE WITH THE INFLECT LIBRARY
        st.session_state['animal_capitalized'] = animal_lowercase.capitalize()
    if hero_gender == 'male':
        hero_boy_or_girl = 'boy'
        hero_he_or_she_lowercase = 'he'
        hero_he_or_she_capitalized = 'He'
        hero_his_or_her_lowercase = 'his'
        hero_his_or_her_capitalized = 'His'
        HERO_HIM_OR_HER_LOWERCASE = 'him'
        HERO_HIM_OR_HER_CAPITALIZED = 'Him'
    elif hero_gender == 'female':
        hero_boy_or_girl = 'girl'
        hero_he_or_she_lowercase = 'she'
        hero_he_or_she_capitalized = 'She'
        hero_his_or_her_lowercase = 'her'
        hero_his_or_her_capitalized = 'Her'
        HERO_HIM_OR_HER_LOWERCASE = 'her'
        HERO_HIM_OR_HER_CAPITALIZED = 'Her'
    REPLACEMENTS = {
        'HERO_FIRSTNAME': st.session_state['hero_firstname'],
        'HERO_LASTNAME': st.session_state['hero_lastname'],
        'HERO_BOY_OR_GIRL': hero_boy_or_girl,
        'HERO_HE_OR_SHE_LOWERCASE' : hero_he_or_she_lowercase,
        'HERO_HE_OR_SHE_CAPITALIZED': hero_he_or_she_capitalized,
        'HERO_HIS_OR_HER_LOWERCASE' : hero_his_or_her_lowercase,
        'HERO_HIS_OR_HER_CAPITALIZED': hero_his_or_her_capitalized,
        'FRIEND_FIRSTNAME': st.session_state['friend_firstname'],
        'FRIEND_LASTNAME': st.session_state['friend_lastname'],
        'FRIEND_RELATIONSHIP': st.session_state['friend_relationship'],
        'HERO_ADJ': st.session_state['hero_adj'],
        'FAVORITE_TOY': st.session_state['favorite_toy'],
        'ANIMAL_LOWERCASE': st.session_state['animal_lowercase'],
        'ANIMAL_PLURAL': st.session_state['animal_plural'],
        'ANIMAL_CAPITALIZED': st.session_state['animal_capitalized'],
        'ANIMAL_ADJ_NOT_SIZE': st.session_state['animal_adj_not_size'],
        'FOREST': st.session_state['forest'],
        'COLOR': st.session_state['color'],
        'CLOTHING': st.session_state['clothing'],
        'VERY_HEALTHY_FOOD': st.session_state['very_healthy_food'],
        'UNHEALTHY_FOOD_1': st.session_state['unhealthy_food_1'],
        'UNHEALTHY_FOOD_2': st.session_state['unhealthy_food_2'],
        'UNHEALTHY_FOOD_3': st.session_state['unhealthy_food_3'],
    }

    for sentence in SENTENCES:
        new_sentence = sentence
        for key, value in REPLACEMENTS.items():
            new_sentence = new_sentence.replace(key, value)

        st.write(new_sentence)

# ******************************************
# SIDEBAR
# ******************************************


MY_VALUES = dict()


for my_field in MY_FIELDS:
    if my_field not in st.session_state:
        st.session_state[my_field] = ''
    MY_VALUES[my_field] = st.session_state[my_field]

def get_info(my_field):
    my_description = MY_DESCRIPTIONS[my_field]
    col_1, col_2 = st.columns([1,1])
    with col_1:
        st.write('')
        st.write('')
        st.write(my_description)
    with col_2:
        my_value = st.text_input('', key=my_field, value=st.session_state[my_field])



st.sidebar.title('Informations')

MY_SUGGESTED_FIELDS = ['hero_adj', 'animal_lowercase', 'animal_adj_not_size', 'forest', 'favorite_toy', 'color', 'clothing',
          'very_healthy_food', 'unhealthy_food_1', 'unhealthy_food_2', 'unhealthy_food_3', 'unhealthy_food_4', 'unhealthy_food_5']

with st.sidebar:

    if st.button('SUGGEST FIELDS'):
        my_suggestions = MY_SUGGESTIONS['hero']
        my_value_suggested = random.choice(my_suggestions)
        st.session_state['hero_firstname'] = my_value_suggested[0]
        st.session_state['hero_lastname'] = my_value_suggested[1]
        st.session_state['hero_gender'] = my_value_suggested[2]
        my_suggestions = MY_SUGGESTIONS['sidekick']
        my_value_suggested = random.choice(my_suggestions)
        st.session_state['friend_firstname'] = my_value_suggested[0]
        st.session_state['friend_lastname'] = my_value_suggested[1]
        st.session_state['friend_gender'] = my_value_suggested[2]
        st.session_state['friend_relationship'] = my_value_suggested[3]
        for my_field in MY_SUGGESTED_FIELDS:
            st.session_state[my_field] =random.choice(MY_SUGGESTIONS[my_field])

    st.subheader('The hero')
    THE_HERO = ['hero_firstname', 'hero_lastname', 'hero_gender', 'hero_adj', 'favorite_toy']
    for my_field in THE_HERO:
        get_info(my_field)

    st.subheader('The villain')
    THE_VILLAIN = ['animal_lowercase', 'animal_adj_not_size', 'color', 'clothing']
    for my_field in THE_VILLAIN:
        get_info(my_field)
    st.subheader('The sidekick')

    THE_SIDEKICK = ['friend_firstname', 'friend_lastname', 'friend_gender', 'friend_relationship']
    for my_field in THE_SIDEKICK:
        get_info(my_field)

    st.subheader('Other info')
    THE_OTHER_INFO = ['forest', 'very_healthy_food', 'unhealthy_food_1', 'unhealthy_food_2','unhealthy_food_3']
    for my_field in THE_OTHER_INFO:
        get_info(my_field)
