# TO CORRECT
# avoid to have twice an unhealthy food
# suggest & memorize hero & hero friend
# suggest friend relationship with linked to sex
# suggest for all fields
# use streamlit form insted of my repetitions
# use different files (for the data, for the functions...) to clarify the code
# do copies with git
# do the fairytale generation
# push to Streamlit Cloud
# do the other generations (cf. the website story-generator)
# add variety in hero's trip (based on characteristics of hero & villain + on chance + on state evolution of hero/villain and on intent)


import streamlit as st
import random

MY_SUGGESTIONS = dict()
MY_SUGGESTIONS['hero'] = [('Sam', 'Gump', 'male'),
                       ('Bob','Doop', 'male'),
                       ('Jody','Gloop', 'female'),
                       ('Robin','Snozcumber', 'female'),
                       ('Mike', 'Giantbulb', 'male'),
                       ('Alex','Slaughterhouse', 'male'),
                       ('Lee','Lakeman','male'),
                       ('Chloe', 'Bogtrotter', 'female'),
                       ('Catherine','Ramsbottom','female'),
                       ]

MY_SUGGESTIONS['pos_character'] = ['gentle', 'thoughtful', 'modest', 'adorable', 'brave', 'helpful','loving', 'special', 'hopeful', 'optimistic', 'charming','kind', 'grateful', 'gracious', 'delightful', 'patient','generous', 'energetic', 'down to earth', 'admirable', 'friendly','smart', 'considerate','noble', 'articulate', 'caring','intuitive', 'sympathetic','clever', 'daring', 'courageous','hilarious', 'understanding', 'incredible','funny', 'popular', 'virtuous', 'lovable', 'remarkable', 'cute', 'sweet', 'splendid','stable', 'witty', 'admirable', 'giving', 'intelligent', 'brave', 'bold']
MY_SUGGESTIONS['neg_character'] = ['greedy','callous','selfish','spiteful','mean','cowardly','stupid', 'spiteful', 'scheming','wild','tactless','peculiar','creepy','sinister', 'arrogant', 'proud', 'ruthless', 'cold-blooded', 'smelly', 'vile', 'snotty', 'hungry', 'predatory', 'malicious', 'deranged', 'snooty', 'violent', 'cowardly', 'brutal', 'controlling', 'clumsy', 'forgetful', 'thoughtless', 'stingy', 'rude', 'tight-fisted',]
MY_SUGGESTIONS['phys_adj'] = ['pink','feathery','sloppy','slimy','spiky','greasy','ginger','brunette','brown', 'blonde', 'red','tall','short','fat','squat','chubby', 'skinny', 'pointy', 'scrawny', 'wobbly', 'wide', 'vast', 'solid', 'fragile', 'fluffy', 'hairy', 'grubby', 'dirty', 'moist', 'ugly', 'pretty', 'charming', 'handsome', 'beautiful', 'sticky', 'curvaceous', 'curvy', 'ample', 'ruddy',]
MY_SUGGESTIONS['hero_adj']= MY_SUGGESTIONS['pos_character'] + MY_SUGGESTIONS['neg_character'] + MY_SUGGESTIONS['phys_adj']

MY_SUGGESTIONS['animal'] = ['fox','monkey','snake','bear','rat','lizard','owl','badger', 'ostrich','frog']
MY_SUGGESTIONS['animal_adj_not_size'] = ['hairy', 'fluffy', 'scary', 'spiky', 'cruel', 'kind', 'fierce', 'friendly', 'fuzzy','hysterical','naughty','scruffy',]
MY_SUGGESTIONS['forest'] = ['Penrose Woods','Central Park','Sherwook Forest','Kennel Vale',	'Idless Woods','St James\'s Park','Kensington Gardens','Gurglebridge','Hyde Park','Hampstead Heath',
									'New Swamp','Thetford Forest','The Amazon Rainforest','Wyre Forest','Snotchester Forest','Greenwood Forest','Spittleton Woods','Gruesomeside Forest','Grizedale Forest','Dallington Forest','Yuckylake Woods','Stinkville Forest',
									'Greenton Woods', 'Slipperyham Park', 'Bogstaple Woods', 'Awfulpool Forest']
MY_SUGGESTIONS['toy'] = ['Mr Teddy','Miss Piggy','Terrance the Moose','Little Mouse', 'Henry the Hippo','Spike','Daisy','Laura','Rags','Bunny',
                         'George','Blankey','Ted','Hugo','Molly','Dolly','Emma','Piglet','Donkey',]
"""
suggestPerson('friend_firstname','friend_lastname','friend_gender')
suggestChildRelationship('friend_firstname','friend_lastname','friend_gender','friend_relationship')
			if(gender==0){
				var relationships = new Array('brother','father','uncle','grandfather','friend','teacher','papa','grandpa');
			}	else {
				var relationships = new Array('mother','auntie','sister','friend','aunt','grandmother','grandma','gran','teacher');
			}

names['male_firstnames'] = new Array( 'Boris', 'Fred', 'Albert', 'Tom', 'James', 'Matthew', 'Mark', 'Luke', 'John', 'David', 'Harold', 'Bob', 'Jack', 'Mike', 'Raymond', 'Cuthbert', 'Casper', 'Harry', 'Cameron', 'Warwick', 'Steve', 'Steven', 'Simon', 'Jeff', 'Zach', 'Chris', 'Christian', 'Matt', 'Mathias', 'Alex', 'Will', 'William', 'Forest', 'Clarke', 'Gregory', 'Joshua', 'Josh', 'Andy', 'Andrew', 'Dick', 'Rick', 'Richard', 'Rob', 'Robert', 'Mo', 'Hector', 'Reginald', 'Phillip', 'Phil', 'Pete', 'Roger', 'Brad', 'Chad', 'Shane', 'Daniel', 'Dan', 'Tristan', 'Roy', 'Gary', 'Tony', 'Toby', 'Barry', 'Graham', 'Kevin','Tommy','Sandie','Darth','Garth');

names['female_firstnames'] = new Array( 'Annie', 'Mary', 'Sarah', 'Laura', 'Lauren', 'Katy', 'Kate', 'Catherine', 'Naomi', 'Helen', 'Nadine', 'Alice', 'Alison', 'Susan', 'Suzanne', 'Sharon', 'Georgina', 'Sonya', 'Marion', 'Beth', 'Una', 'Sophia', 'Rachel', 'Christiana', 'Maud', 'Mildred', 'Zoe', 'Chantal', 'Charlotte', 'Chloe', 'Flora', 'Annabelle', 'Elizabeth', 'Morwenna', 'Jenna', 'Jenny', 'Gemma', 'Wenna', 'Fairydust', 'Charity', 'Ocean', 'Virginia', 'Hannah', 'Mavis', 'Harriet', 'Kathy', 'Heather', 'Kimberly', 'May', 'Carla', 'Suki', 'Michelle', 'Rhiannon', 'Ruth', 'Polly', 'Sally', 'Molly', 'Dolly', 'Maureen', 'Maud', 'Doris', 'Felicity','Jessica','Stanley' );

names['lastnames'] = new Array( 'Gump', 'Doop', 'Gloop', 'Snozcumber', 'Giantbulb', 'Slaughterhouse', 'Godfrey', 'Smith', 'Jones', 'Bogtrotter', 'Ramsbottom', 'Cockle', 'Hemingway', 'Pigeon', 'Parker', 'Nolan', 'Parkes', 'Butterscotch', 'Barker', 'Trescothik', 'Superhalk', 'Barlow', 'MacDonald', 'Ferguson', 'Donaldson', 'Platt', 'Bishop', 'Blunder', 'Thunder', 'Sparkle', 'Walker', 'Raymond', 'Thornhill', 'Sweet', 'Parker', 'Johnson', 'Randall', 'Zeus', 'England', 'Smart', 'Gobble', 'Clifford', 'Thornton', 'Cox', 'Blast', 'Plumb', 'Wishmonger', 'Fish', 'Blacksmith', 'Thomas', 'Grey', 'Russell', 'Lakeman', 'Ball', 'Chan', 'Chen', 'Wu', 'Khan', 'Meadows', 'Connor', 'Williams', 'Wilson', 'Blackman', 'Jones', 'Humble', 'Noris','Bond','Rabbit','McCallister','DeVito','Malkovich','Olsson','Sparrow','Kowalski',
'Vader','Torrance', 'Greenway','Rockatansky','Pitt','Willis','Jolie');
"""

MY_SUGGESTIONS['color'] = ['red', 'yellow', 'green', 'blue', 'purple', 'pink']
MY_SUGGESTIONS['clothing'] = ['top hat', 'bowler hat', 'dungarees', 'pinafore', 'skirt', 't-shirt', 'jumper', 'waistcoat', 'coat', 'jacket']
MY_SUGGESTIONS['healthy_food'] = ['carrots', 'butternut squashes', 'aubergines', 'courgettes', 'cauliflowers', 'cabbages', 'parsnips', 'sprouts', 'turnips',
                      'sweet potatoes', 'swedes','broccoli florets','pumpkins','peppers','onions','runner beans','sugar snap pea','pods of peas','peas','red cabbages','lettuces','cucumbers',]
MY_SUGGESTIONS['unhealthy_food'] = ['crisps', 'sweets', 'biscuits', 'cakes', 'toffees', 'chocolates','chips', 'doughnuts', 'pancakes','muffins','cupcakes','pizzas','macarons','lollipops','jelly babies','humbugs','fruit gums']


MY_IDs = ['hero_firstname', 'hero_lastname', 'hero_gender', 'hero_adj',
          'animal', 'animal_adj_not_size', 'friend_firstname', 'friend_lastname', 'friend_gender', 'friend_relationship',
          'forest', 'toy', 'color', 'clothing',
          'healthy_food', 'unhealthy_food_1', 'unhealthy_food_2', 'unhealthy_food_3', 'unhealthy_food_4', 'unhealthy_food_5']


# Create a fairy tale
# https://www.plot-generator.org.uk/fairytale/

# FULL WIDTH
# st.set_page_config(layout="wide")

# *******************************
# personalized style
# button
m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: rgb(200, 200, 200);
    }
    </style>""", unsafe_allow_html=True)
# *******************************

my_columns = dict()
my_values = dict()

"""
for my_id in MY_IDs:
    if my_id not in st.session_state:
        st.session_state[my_id] = ''
    my_values[my_id] = st.session_state[my_id]

"""
"""
nb_information = 17 # cf. the keys from 0 to 16
for i in range(nb_information):
    my_value_str = 'my_value_' + str(i) # state variables my_value_0, ..., my_value_16
    if my_value_str not in st.session_state:
        st.session_state[my_value_str] = ''
    my_values[my_value_str] = st.session_state[my_value_str]
"""
nb_information = 17 # cf. the keys from 0 to 16
for i in range(nb_information):
    my_value_str = 'my_value_' + str(i) # state variables my_value_0, ..., my_value_16
    if my_value_str not in st.session_state:
        st.session_state[my_value_str] = ''
    my_values[my_value_str] = st.session_state[my_value_str]

for my_id in MY_IDs:
    if my_id not in st.session_state:
        st.session_state[my_id] = ''
    my_values[my_id] = st.session_state[my_id]

my_values

def get_or_suggest_a_piece_of_information(my_id,
                                          my_description='', # description of the input
                                          my_suggestions=['default'], # choices for the suggestion
                                          my_value = '', # default value of the input
                                          ):
    # my_id = str of a number e.g. "5"
    # type = "input_text", "selectbox"...
    # my_choices = for selectbox
    my_value_str = 'my_value_' + my_id
    col_1, col_2 = st.columns([1,1])
    with col_1:
        placeholder = st.empty()
        placeholder.text_input(my_description, value=my_value, key=my_id)
    with col_2:
        st.write('')
        st.write('')
        click_suggest = st.button('Suggest', key=my_id)
        if click_suggest:
            my_value = random.choice(my_suggestions)
            placeholder.text_input(my_description, value=my_value)
            st.session_state[my_value_str] = my_value

def get_or_suggest_a_person(my_id, my_description, my_value_first_name ='', my_value_last_name='', my_value_gender=0):
    # my_id = str of a number e.g. "5"
    # type = "input_text", "selectbox"...
    # my_choices = for selectbox
    st.write(my_description)
    my_column_1 = my_id + '_1'
    my_column_2 = my_id + '_2'
    my_column_3 = my_id + '_3'
    my_column_4 = my_id + '_4'
    my_columns[my_column_1], my_columns[my_column_2], my_columns[my_column_3], my_columns[my_column_4] = st.columns([1,1,1,1])
    with my_columns[my_column_1]:
        #st.text_input('First name', key=my_column_1)
        placeholder_first_name = st.empty()
        placeholder_first_name.text_input('First name', value=my_value_first_name, key=my_column_1)
    with my_columns[my_column_2]:
        #st.text_input('Last name', key=my_column_2)
        placeholder_last_name = st.empty()
        placeholder_last_name.text_input('Last name', value=my_value_last_name, key=my_column_2)
    with my_columns[my_column_3]:
        result = st.radio('', ('Male', 'Female'), index=my_value_gender, key=my_column_3)
    with my_columns[my_column_4]:
        st.write('')
        st.write('')
        st.button('Suggest', key=my_id)
    return 'Male' if result.index == 0 else 'Female'

def get_or_suggest_selectbox(my_id,
                             my_description='', # description of the input
                             my_suggestions=['default'], # choices for the suggestion
                             my_value = 1, # default value of the input
                             ):
    # my_id = str of a number e.g. "5"
    # type = "input_text", "selectbox"...
    # my_choices = for selectbox
    my_value_str = 'my_value_' + my_id
    my_column_1 = my_id + '_1'
    my_column_2 = my_id + '_2'
    my_columns[my_column_1], my_columns[my_column_2] = st.columns([1,1])
    with my_columns[my_column_1]:
        placeholder = st.empty()
        placeholder.selectbox(my_description, my_suggestions, key=my_id)
    with my_columns[my_column_2]:
        st.write('')
        st.write('')
        click_suggest = st.button('Suggest', key=my_id)
        if click_suggest:
            my_value = random.choice(my_suggestions)
            placeholder.text_input(my_description, value=my_value, key=my_id)
            st.session_state[my_value_str] = my_value


# *******************************
# TITLES & UPPER PART
st.title('Story Generator - Fairytale')
'Please keep your input family friendly.'

# RANDOM FILL
st.subheader('Need a prompt? Go random! ')
if st.button('Fill entire form with random ideas'):
    'FillAll function'
else:
    'Fill the form yourself'


# *******************************
# FORM
st.header('Fill in the form.')

# HERO
st.subheader("The hero (a child)")
# TODO
hero_gender = get_or_suggest_a_person('0', '')
hero_gender
# FIN TODO
get_or_suggest_a_piece_of_information('1', 'An adjective to describe your hero (e.g. little, brave)',
                                      my_suggestions = MY_SUGGESTIONS['hero_adj'],
                                      my_value=my_values['my_value_1'])
get_or_suggest_a_piece_of_information('2', "The hero's favourite cuddly toy (e.g. Mr Teddy)",
                                      my_suggestions = MY_SUGGESTIONS['toy'],
                                      my_value=my_values['my_value_2'])

# VILLAIN (animals)
st.subheader("The villain")
get_or_suggest_a_piece_of_information('3', 'A type of animal (e.g. bear, pig)',
                                      my_suggestions = MY_SUGGESTIONS['animal'],
                                      my_value=my_values['my_value_3'])
# TODO
get_or_suggest_selectbox ('4', 'How many of the animals above will be in the story', my_suggestions=(1,2,3,4,5))
# FIN TODO
get_or_suggest_a_piece_of_information('5', "An adjective (not relating to size) describing the animal(s) (e.g. hairy, scary)",
                                      my_suggestions = MY_SUGGESTIONS['animal_adj_not_size'],
                                      my_value=my_values['my_value_5'])

# ADDITIONAL INFORMATION
st.subheader("Additional information")
# TODO
get_or_suggest_a_person('6', 'A friend or family member of the hero')
get_or_suggest_a_piece_of_information('7', 'His or her relationship to the hero')
# FIN TODO
get_or_suggest_a_piece_of_information('8', 'The name of a forest or park nearby (e.g. Sherwood Forest)',
                                      my_suggestions = MY_SUGGESTIONS['forest'],
                                      my_value=my_values['my_value_8'],)
get_or_suggest_a_piece_of_information('9', 'A colour (e.g. red, green)',
                                      my_suggestions = MY_SUGGESTIONS['color'],
                                      my_value=my_values['my_value_9'],)
get_or_suggest_a_piece_of_information('10', 'An item of clothing, singular (e.g. skirt, dungarees)',
                                      my_suggestions = MY_SUGGESTIONS['clothing'],
                                      my_value=my_values['my_value_10'],)
get_or_suggest_a_piece_of_information('11', 'A type of healthy vegetable, plural (e.g. carrots, cabbages)',
                                      my_suggestions = MY_SUGGESTIONS['healthy_food'],
                                      my_value=my_values['my_value_11'],)
"Five unhealthy foods, plural (e.g. biscuits, crisps)"
# WE SHOULD AVOID TO HAVE TWICE THE SAME UNHEALTHY FOOD
get_or_suggest_a_piece_of_information('12', 'Unhealthy food 1',
                                      my_suggestions = MY_SUGGESTIONS['unhealthy_food'],
                                      my_value=my_values['my_value_12'],)
get_or_suggest_a_piece_of_information('13', 'Unhealthy food 2',
                                      my_suggestions = MY_SUGGESTIONS['unhealthy_food'],
                                      my_value=my_values['my_value_13'],)
get_or_suggest_a_piece_of_information('14', 'Unhealthy food 3',
                                      my_suggestions = MY_SUGGESTIONS['unhealthy_food'],
                                      my_value=my_values['my_value_14'],)
get_or_suggest_a_piece_of_information('15', 'Unhealthy food 4',
                                      my_suggestions = MY_SUGGESTIONS['unhealthy_food'],
                                      my_value=my_values['my_value_15'],)
get_or_suggest_a_piece_of_information('16', 'Unhealthy food 5',
                                      my_suggestions = MY_SUGGESTIONS['unhealthy_food'],
                                      my_value=my_values['my_value_16'],)
