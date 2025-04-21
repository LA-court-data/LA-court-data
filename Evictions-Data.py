import streamlit as st
import pandas as pd
import matplotlib.pyplot

def wide_space_default():
    st.set_page_config(layout= 'wide')

wide_space_default()
st.title("Louisiana Evictions Court Info")
df = pd.read_excel('evictionscourtdata.xlsx') 
st.set_option('client.showSidebarNavigation', True)
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "More"])
if selection == "Home":
    st.subheader("Data Preview")
    st.write(df.head())
    st.subheader("Parish Lookup")

    parish_names_series = df['Parish Name']
    parish_names_list = parish_names_series.tolist()
    selected_parish = st.selectbox("Select Parish", parish_names_list)
    parish_info = df[df['Parish Name'] == selected_parish]
    transposed_df = parish_info.transpose()
    st.write(transposed_df)


    st.write(" **Relevant case law used in compiling the data:** ")

    st.write("> Justice of the peace and district courts have jurisdiction over evictions of residential tenants and occupants regardless of the amount of monthly or yearly rent, or the rent for the unexpired term of the lease. La. Code Civ. Proc. art. 4912 (A). City and parish courts have jurisdiction over tenants if the monthly rental is less than \$3,000 or the annual rental less than \$36,000. La. Code Civ. Proc. art. 4844. City and parish courts are courts of limited jurisdiction. A jurisdictional oddity exists in that these courts do not have express statutory jurisdiction over evictions of tenants where the lease term is other than a day, week, month or year (pg. 576).")

    st.write("> The parish court, a relatively new limited jurisdiction court, began operation in Jefferson Parish in l964. In l966 an additional parish court was created in Jefferson Parish, and in l976 the Parish Court for the Parish of Ascension was created. Essentially they are similar in jurisdiction to city courts outside Orleans Parish. Between them, the First and Second Parish Courts for the Parish of Jefferson have parishwide jurisdiction, one on the East Bank of the Mississippi and the other on the West Bank. The Parish Court of Ascension Parish has parishwide jurisdiction.")
    #ok
elif selection == "More":
    st.subheader("Making changes")
    st.write("The data for this website is supported by an excel sheet in the github repository")
    st.write("To make changes to this information, you'll need the login information")
    CORRECT_PIN = "1340"

# Ask for user input
    pin_input = st.text_input("Enter the 4 digit PIN. (This is the same as the door code):", type="password")
    st.write("If you run into any issues email me at evjones04@gmail.com or text at 850-597-1088")
    # Check the PIN
    if pin_input == CORRECT_PIN:
        st.success("Access granted.")
        st.write("🎉 Here is the login information.")
        # Add any other elements you want to reveal here
        st.write("Go to github.com")
        st.write("Username: LA-court-data")
        st.write("Password: ")

        st.subheader("Next Steps")
        st.write("1. Click on the repositories tab")
        st.write("2. Click LA-court-data")
        st.write("3. Rename the file evictionscourtdata.xlsx to something else, such as evictionscourtdata-2")
        st.write("      You can edit a files name in Github by clicking on it, then clicking edit this file")
        st.write("      Then type the new name in the textbox (top middle of your screen)")
        st.write("      Then click commit changes, and commit changes again on the pop-up")
        st.write("4. Upload the new excel file. Be sure it is a .xlsx file, and that it is named evictionscourtdata. ")
        st.write("      Upload a new file by clicking add file on the main repository screen")
        st.write("      If you have trouble finding this screen, use the following link:")
        st.write("          https://github.com/LA-court-data/LA-court-data/tree/main")
        st.write("All done!")

    else:
        if pin_input:  # only show error if user entered something
            st.error("Incorrect PIN. Please try again.")
