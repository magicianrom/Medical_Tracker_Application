
import streamlit as st

# Define the pages
main_page = st.Page("splash.py", title="Main Page", icon="🏠")
page_2 = st.Page("main_page.py", title="Add Medicine", icon="💊")
page_3 = st.Page("search.py", title="Medicine", icon="🌿")


page_4 = st.Page("intake.py", title="ChatGPT Medical", icon="🤖")

page_5 = st.Page("refill.py", title="My Medicine Tracker", icon="🛒")


# Set up navigation
pg = st.navigation([main_page, page_2, page_3, page_4, page_5])

# Run the selected page
pg.run()
