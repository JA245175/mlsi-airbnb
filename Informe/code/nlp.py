target_luxury = (
    "luxury luxe lujo premium exclusive exclusivo high-end alta gama "
    "boutique designer diseño exklusiv "
    "lavish opulent elegant posh prestigious affluent sophisticated "
    "sumptuous elite grand luxurious palatial glamorous chic refined stylish "
    "vintage 'designer brand' 'exclusive access'"
)

target_studio = (
    "studio estudio monoambiente loft microstudio small flat tiny apartment "
    "compact living microapartamento 'espacio reducido' 'estudio funcional' "
    "estudio compacto 'apartamento pequeño' 'mini loft' 'smart apartment' "
    "minimalista 'apartamento de diseño' 'smart living' 'living space' "
    "open-plan 'one-bedroom apartment' 'space-saving' compact apartment "
    "cozy apartment 'minimalist studio'"
)

target_room = (
    "room habitacion quarto chambre cuarto 'private room' 'shared room' "
    "small room dormitorio habitación habitáculo 'habitación privada' "
    "'habitación compartida' estancia 'cuarto pequeño' suite bedroom "
    "'room with a view' 'single room' 'shared space' 'personal space' "
    "'living quarters' 'guest room' 'room for rent' 'co-living space' "
    "'private suite'"
)

# 2. Features NLP mejoradas
df["name"] = df["name"].fillna("").astype(str)
df['name_clean'] = df['name'].str.lower().apply(unidecode.unidecode)

# NPL
# Se intenta identificar conceptos de lujo, studio y room mediante embeddings
model_st = SentenceTransformer('all-MiniLM-L6-v2')
name_embeddings = model_st.encode(df['name_clean'].tolist(), convert_to_tensor=True)

emb_luxury =  model_st.encode(target_luxury, convert_to_tensor=True)
emb_studio = model_st.encode(target_studio, convert_to_tensor=True)
emb_room = model_st.encode(target_room, convert_to_tensor=True)

luxury_sim = util.cos_sim(name_embeddings, emb_luxury).cpu().numpy().flatten()
studio_sim = util.cos_sim(name_embeddings, emb_studio).cpu().numpy().flatten()
room_sim = util.cos_sim(name_embeddings, emb_room).cpu().numpy().flatten()

df["sim_luxury"] = luxury_sim.astype(float)
df["sim_studio"] = studio_sim.astype(float)
df["sim_room"] = room_sim.astype(float)