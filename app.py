import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Contact Manager", page_icon="📞")

file = "contacts.csv"

# Create CSV if not exists
if not os.path.exists(file):
    pd.DataFrame(columns=["Name", "Phone", "Email"]).to_csv(file, index=False)

df = pd.read_csv(file)

st.title("📞 Contact Manager System")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Dashboard",
        "Add Contact",
        "View Contacts",
        "Search Contact",
        "Update Contact",
        "Delete Contact"
    ]
)

# Dashboard
if menu == "Dashboard":

    st.subheader("📊 Dashboard")

    st.metric("Total Contacts", len(df))

    st.write("Recent Contacts")
    st.dataframe(df.tail())

# Add Contact
elif menu == "Add Contact":

    st.subheader("➕ Add Contact")

    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")

    if st.button("Save Contact"):

        if name and phone and email:

            new_contact = pd.DataFrame({
                "Name": [name],
                "Phone": [phone],
                "Email": [email]
            })

            df = pd.concat([df, new_contact], ignore_index=True)
            df.to_csv(file, index=False)

            st.success("✅ Contact Added Successfully!")

        else:
            st.warning("Please fill all fields.")

# View Contacts
elif menu == "View Contacts":

    st.subheader("📋 All Contacts")

    st.dataframe(df)

    st.download_button(
        label="⬇ Download Contacts CSV",
        data=open(file, "rb").read(),
        file_name="contacts.csv",
        mime="text/csv"
    )

# Search Contact
elif menu == "Search Contact":

    st.subheader("🔍 Search Contact")

    search = st.text_input("Enter Name")

    if search:

        result = df[
            df["Name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

        st.dataframe(result)

# Update Contact
elif menu == "Update Contact":

    st.subheader("✏ Update Contact")

    if len(df) > 0:

        contact = st.selectbox(
            "Select Contact",
            df["Name"]
        )

        row = df[df["Name"] == contact].index[0]

        new_name = st.text_input(
            "Name",
            df.loc[row, "Name"]
        )

        new_phone = st.text_input(
            "Phone",
            str(df.loc[row, "Phone"])
        )

        new_email = st.text_input(
            "Email",
            df.loc[row, "Email"]
        )

        if st.button("Update"):

            df.loc[row, "Name"] = new_name
            df.loc[row, "Phone"] = new_phone
            df.loc[row, "Email"] = new_email

            df.to_csv(file, index=False)

            st.success("✅ Contact Updated Successfully!")

    else:
        st.warning("No contacts available.")

# Delete Contact
elif menu == "Delete Contact":

    st.subheader("🗑 Delete Contact")

    if len(df) > 0:

        contact = st.selectbox(
            "Select Contact",
            df["Name"]
        )

        if st.button("Delete"):

            df = df[df["Name"] != contact]

            df.to_csv(file, index=False)

            st.success("✅ Contact Deleted Successfully!")

    else:
        st.warning("No contacts available.")