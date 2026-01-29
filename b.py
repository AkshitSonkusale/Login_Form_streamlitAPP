import streamlit as st

#header
st.header("Student Management System")

#title of the app
st.title("Welcome to the Student Management System App")

#subheader
st.subheader("Manage student records efficiently")


#markdown
st.markdown("-----------------------------------------------------------------")

#text
st.text("This is a simple student management system.")

#write
st.write("Hello !")
st.write({'Name': 'Akshit', 'Age': 20})


#markdown : used to format text
st.markdown("**This is bold text**")
st.markdown("*This is italic text*")
st.markdown("- item 1\n- item 2")
st.markdown("<h3 style='color:red'>BARCELONA</h3>", unsafe_allow_html=True)

#caption
st.caption("This is a caption for additional information.")

#code : used to display code snippets
st.code("""
        def add(a, b):
            return a + b
        """, language='python')


#latex : used to render mathematical expressions 
st.latex(r'''
    a^2 + b^2 = c^2
''')

#divider : visual horzontal line seperator
st.divider() 

#button : to create a button 
if st.button("Click"):
    st.success("Button Clicked!")
    st.balloons()
else:
    st.warning("Button not clicked yet.")

#textInput : to take text input from user
name = st.text_input("Enter your name: ")


#to enter a valid character 
if name == "":
    st.warning("Cannot be empty!")

elif name.isalpha():
    st.write("Hello, ", name)
else:
    st.warning("Please enter a valid name (only alphabetic characters).")

#textarea : to take multiline text input from user
feedback = st.text_area("Enter your feedback: ")
st.write("Your feedback: ", feedback)

#checkbox
if st.checkbox("I agree to the terms and conditions"):
    st.success("Thank you for agreeing!")

#radio button : to select one option from multiple choices
gender = st.radio("Select your gender:", ('Male', 'Female', 'Other'))
st.write(f"You selected: {gender}" )


#selectbox : to select one option from a dropdown menu
country = st.selectbox("Select your country : ", ("India","USA","Australia"))
st.write("You selected: ", country)

#multiselect : to select multiple options from a dropdown menu
skills = st.multiselect("Select your skills:", ['Python', 'Java', 'C++', 'JavaScript'])
st.write("You selected: ", skills)

#slider : to select a value from a range
age = st.slider("Select your age:", 0, 100, 25)

#file_uploader : to upload files
uploaded_file = st.file_uploader("Upload your profile picture:", type=['png', 'jpg', 'jpeg'])
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)


#form : to group multiple input widgets together
with st.form("Form"):
    name = st.text_input("Enter your name:") 
    if name == "":
        st.warning("Name cannot be empty!")
    elif not name.isalpha():
        st.warning("Please enter a valid name (only alphabetic characters).")   
    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=18)  
    submit = st.form_submit_button("Submit")

    if submit:
        st.success(f"Form submitted! Name: {name}, Age: {age}")        
        st.balloons()    
    else:
        st.warning("Please fill out the form and submit.")

st.divider()

#login form : to create a login form
with st.form("Login Form"):
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    login = st.form_submit_button("Login")

    if login:
        if username == "admin" and password == "password":
            st.success("Login successful!")
            st.balloons()
        else:
            st.error("Invalid username or password.")


#columns : to create multiple columns in the app
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Column 1")
with col2:
    st.header("Column 2")
    st.write("This is some text in column 2.")

#container method to create a container
container = st.container()
container.write("This is inside the container.")
container.button("Button in container")


#table : to display data in tabular format
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)

#sidebar : to create a sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Select an option:", ["Home", "Profile", "Settings"])


#cache data : to cache data for performance optimization
@st.cache_data
def load_data():
    return [1,2,3,4]
data = load_data()
st.write(data)
