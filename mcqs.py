import streamlit as st

st.title("AI Study Assistant 📘")

text = st.text_area("Paste your notes here")
option = st.selectbox("Choose option", ["Summarize", "Generate MCQs"])

if st.button("Run"):
    if option == "Summarize":
        st.write("Summary will appear here")
    elif option == "Generate MCQs":
        if text.strip() == "":
            st.warning("Please enter notes first")
        else:
            mcqs = generate_mcqs(text)
            st.subheader("Generated MCQs:")

            for q, a in mcqs:
                st.write(q)
                st.write("Answer:", a)
                st.write("—")