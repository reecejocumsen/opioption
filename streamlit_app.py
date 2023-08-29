import streamlit as st

opiod_analgesics_to_morphine_data = {
    "Codeine, PO": 10,
    "Diamorphine, IV": 0.33,
    "Diamorphine, SC": 0.33,
    "Dihydrocodeine, PO": 10,
    "Hydromorphone, PO": 0.2,
    "Morphine, IV": 0.5,
    "Morphine, SC": 0.5,
    "Oxycodone, PO": 0.66,
    "Oxycodone, IV": 0.5,
    "Oxycodone, SC": 0.5,
    "Tramadol, PO": 1
}

morphine_to_bup_data = {
    12: 5,
    24: 10,
    36: 15,
    48: 20,
    84: 35,
    126: 52.5,
    168: 70
}

morphine_to_fent_data = {
    30: 12,
    60: 25,
    90: 37.5,
    120: 50,
    180: 75,
    240: 100
}

def morphine_to_patch(morphine_mg_daily, patch_dict, patch_type):
    data_items = list(patch_dict.items())
    for index, data_pair in enumerate(data_items):
        if morphine_mg_daily <= data_pair[0]:
            result_str = f"{patch_type} '{data_pair[1]}' patch is equivalent to {data_pair[0]}mg of morphine"
            if index == 0:
                result_str = f"{result_str}. No smaller option in system."
            else:
                result_str = f"{result_str}. Smaller option, {patch_type} '{data_items[index-1][1]}' patch, is equivalent to {data_items[index-1][0]}mg of morphine"
            return result_str
    return f"Cannot find single {patch_type} patch to correspond to {morphine_mg_daily}mg of morphine"

st.title("Opioptions")
st.header("Equivalent doses of opiod analgesics to oral morphine")
st.markdown("""This table is an **approximate** guide; patients should be 
            carefully monitored after any change in medication and dose 
            titration may be required. Conversion ratios vary in the literature;
            these conversion ratios are based on the Palliative Care Formulary 
            8th edition.""")
oral_morphine_dose = st.number_input("Oral morphine sulfate dose (mg)")

if oral_morphine_dose != 0:
    st.dataframe([{'Analgesic and Route': drug[0], f'Equivalent dose to {oral_morphine_dose}mg of oral morphine sulfate in mg': drug[1]*oral_morphine_dose} for drug in opiod_analgesics_to_morphine_data.items()], use_container_width=True)
    st.caption("PO = by mouth; IV = intravenous; SC = subcutaneous")
    st.caption("**NOTE: 10mg oral oxycodone is approximately equivalent to 6.6mg IV/SC oxycodone.**")
st.divider()

st.header("Medication to patch")

col1, col2 = st.columns(2)
current = col1.selectbox("Current medication and method", options=[None, *opiod_analgesics_to_morphine_data.keys()], index=0, format_func = lambda x: x or "---")
dose = col2.number_input("Daily dose (mg)")

if current and dose:
    current_as_morphine = dose/opiod_analgesics_to_morphine_data[current]
    st.markdown(f"{dose}mg of {current} is equivalent to {current_as_morphine}mg of morphine.")
    st.markdown(f"**Fentanyl patch**: {morphine_to_patch(current_as_morphine, morphine_to_fent_data, 'fentanyl')}")
    st.markdown(f"**Buprenorphine patch**: {morphine_to_patch(current_as_morphine, morphine_to_bup_data, 'buprenorphine')}")
else:
    st.caption("Fill out the two fields above to see calculations.")