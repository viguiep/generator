# Story generator in Streamlit with form

import streamlit as st
import random


# ******************************************
# VARIABLES
# ******************************************
MY_FIELDS = ['hero_firstname', 'hero_lastname', 'hero_gender', 'hero_adj',
          'animal', 'animal_adj_not_size', 'nb_animals', 'friend_firstname', 'friend_lastname', 'friend_gender', 'friend_relationship',
          'forest', 'toy', 'color', 'clothing',
          'healthy_food', 'unhealthy_food_1', 'unhealthy_food_2', 'unhealthy_food_3', 'unhealthy_food_4', 'unhealthy_food_5']

MY_DESCRIPTIONS = { 'hero_firstname' : 'First name',
                    'hero_lastname' : 'Last name',
                    'hero_gender' : 'Gender',
                    'hero_adj' : 'An adjective to describe your hero (e.g. little, brave)',
                    'animal' : 'A type of animal (e.g. bear, pig)',
                    'animal_adj_not_size' : "An adjective (not relating to size) describing the animal(s) (e.g. hairy, scary)",
                    'nb_animals' : 'How many of the animals above will be in the story',
                    'friend_firstname' : 'First name',
                    'friend_lastname' : 'Last name',
                    'friend_gender' : 'Gender',
                    'friend_relationship' : 'Relationship',
                    'forest' : 'The name of a forest or park nearby (e.g. Sherwood Forest)',
                    'toy' : "The hero's favourite cuddly toy (e.g. Mr Teddy)",
                    'color' : 'A color (e.g. red, green)',
                    'clothing' : 'An item of clothing, singular (e.g. skirt, dungarees)',
                    'healthy_food' : 'A type of healthy vegetable, plural (e.g. carrots, cabbages)',
                    'unhealthy_food_1' : 'Unhealthy food 1',
                    'unhealthy_food_2' : 'Unhealthy food 2',
                    'unhealthy_food_3' : 'Unhealthy food 3',
                    'unhealthy_food_4' : 'Unhealthy food 4',
                    'unhealthy_food_5' : 'Unhealthy food 5'}


# ******************************************
# BEGINNING
# ******************************************
st.title('Story generator (Fairytale)')

"""
Principle:
- enter the data with a FORM
- you can generate all the data (changing the default value)
- then the full app is run
"""

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
    col_1, col_2 = st.columns([3,1])
    with col_1:
        st.write('')
        st.write('')
        st.write(my_description)
    with col_2:
        my_value = st.text_input('', key=my_field, value=st.session_state[my_field])

if st.button('SUGGEST FIELDS'):
    st.session_state['hero_firstname'] = 'Pascal'
    st.session_state['hero_lastname'] = 'Viguié'

st.subheader('The hero')
get_info('hero_firstname')
get_info('hero_lastname')
get_info('hero_gender')
get_info('hero_adj')
get_info('toy')
get_info('color')
get_info('clothing')
st.subheader('The villain')
get_info('animal')
get_info('animal_adj_not_size')
get_info('nb_animals')
st.subheader('The sidekick')
get_info('friend_firstname')
get_info('friend_lastname')
get_info('friend_gender')
get_info('friend_relationship')
st.subheader('Other info')
get_info('forest')
get_info('healthy_food')
get_info('unhealthy_food_1')
get_info('unhealthy_food_2')
get_info('unhealthy_food_3')
get_info('unhealthy_food_4')
get_info('unhealthy_food_5')


st.sidebar.title('Informations')

with st.sidebar:
    st.write('COUCOU')
