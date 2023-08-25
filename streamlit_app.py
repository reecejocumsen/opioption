import streamlit as st

opiod_analgesics_to_morphine_data = [
    ("Codeine", "PO", 10),
    ("Diamorphine", "IV", 0.33),
    ("Diamorphine", "SC", 0.33),
    ("Dihydrocodeine",  "PO", 10),
    ("Hydromorphone", "PO", 0.2),
    ("Morphine", "IV", 0.5),
    ("Morphine", "SC", 0.5),
    ("Oxycodone", "PO", 0.66),
    ("Oxycodone", "IV", 0.5),
    ("Oxycodone", "SC", 0.5),
    ("Tramadol", "PO", 10)
]

st.title("Opioptions")
st.header("Equivalent doses of opiod analgesics to oral morphine")
st.markdown("""This table is an **approximate** guide; patients should be 
            carefully monitored after any change in medication and dose 
            titration may be required. Conversion ratios vary in the literature;
            these conversion ratios are based on the Palliative Care Formulary 
            8th edition.""")
oral_morphine_dose = st.number_input("Oral morphine sulfate dose (mg)")

if oral_morphine_dose != 0:
    st.dataframe([{'Analgesic': drug[0], 'Route': drug[1], f'Equivalent dose to {oral_morphine_dose}mg of oral morphine sulfate in mg': drug[2]*oral_morphine_dose} for drug in opiod_analgesics_to_morphine_data], use_container_width=True)
    st.caption("PO = by mouth; IV = intravenous; SC = subcutaneous")
    st.caption("**NOTE: 10mg oral oxycodone is approximately equivalent to 6.6mg IV/SC oxycodone.**")
st.divider()