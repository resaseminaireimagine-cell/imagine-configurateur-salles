import streamlit as st

st.set_page_config(page_title="Configurateur — Salle du Conseil", layout="wide")

# -------------------------
# RÈGLES (V1)
# -------------------------
ROOM_NAME = "Salle du Conseil"
CAPACITY = {
    "U": 28,
    "Théâtre": 60,
    "Classe": 30,
}

# -------------------------
# UI
# -------------------------
st.title(f"Configurateur — {ROOM_NAME}")

left, right = st.columns([2, 1])

with right:
    st.subheader("Configuration")
    config = st.selectbox("Disposition", list(CAPACITY.keys()), index=0)
    max_cap = CAPACITY[config]

    pax = st.slider("Nombre de participants", min_value=1, max_value=100, value=min(20, max_cap))

    # Statut capacité
    ratio = pax / max_cap
    if pax <= max_cap:
        if ratio <= 0.85:
            st.success(f"OK — capacité max : {max_cap}")
        else:
            st.warning(f"Ça passe, mais serré — capacité max : {max_cap}")
    else:
        st.error(f"Impossible — capacité max : {max_cap} (tu demandes {pax})")

    st.divider()
    st.subheader("Récap")
    recap = {
        "Salle": ROOM_NAME,
        "Disposition": config,
        "Participants": pax,
        "Capacité max": max_cap,
        "Statut": "OK" if pax <= max_cap else "Dépassement",
    }
    st.json(recap)

    # Export texte (V1)
    recap_txt = "\n".join([f"{k} : {v}" for k, v in recap.items()])
    st.download_button(
        "Télécharger le récap (TXT)",
        data=recap_txt,
        file_name="recap_salle_du_conseil.txt",
        mime="text/plain",
        use_container_width=True
    )

with left:
    st.subheader("Aperçu (plan / photo)")
    st.caption("V1 : mets ici un plan ou une photo de la salle. (Image PNG/JPG)")

    # Option : upload d'une image (plan/photo)
    img = st.file_uploader("Importer une image (plan/photo)", type=["png", "jpg", "jpeg"])
    if img:
        st.image(img, use_container_width=True)
    else:
        st.info("Ajoute un visuel pour que le configurateur soit immédiatement parlant.")
