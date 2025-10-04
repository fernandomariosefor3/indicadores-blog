import pandas as pd
import json

arquivos = [
    "saeb_aprendizado_territorios-23-2015-EM.xlsx",
    "saeb_aprendizado_territorios-23-2017-EM.xlsx",
    "saeb_aprendizado_territorios-23-2019-EM.xlsx",
    "saeb_aprendizado_territorios-23-2021-EM.xlsx",
    "saeb_aprendizado_territorios-23-2023-EM.xlsx"
]

escolas = {}

for arquivo in arquivos:
    df = pd.read_excel(arquivo, sheet_name="municipios")
    for _, row in df.iterrows():
        inep = str(row.get("inep_id", ""))
        if not inep:
            continue
        if inep not in escolas:
            escolas[inep] = {"historico": []}
        escolas[inep]["historico"].append({
            "ano": int(row["ano"]),
            "ideb": row.get("ideb", None),
            "nota_lp": row.get("nota_lp", None),
            "nota_mt": row.get("nota_mt", None)
        })

with open("escolas.json", "w", encoding="utf-8") as f:
    json.dump(escolas, f, ensure_ascii=False, indent=2)
