import json

with open("notebook.ipynb", "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell["cell_type"] == "markdown":
        source = "".join(cell["source"])
        
        # 1. Update Intro
        if "2. Feature engineering (ratios, interactions, binned features)" in source:
            source = source.replace(
                "2. Feature engineering (ratios, interactions, binned features)",
                "2. Feature engineering (Engagement Score interaction)"
            )
            source = source.replace(
                "3. **Ensemble**: Weighted average of tuned XGBoost and balanced Random Forest",
                "3. **Ensemble**: Weighted average of simple XGBoost and balanced Random Forest"
            )
            # Reconstruct source list
            cell["source"] = [line + "\n" if i < len(source.split("\n"))-1 else line for i, line in enumerate(source.split("\n"))]
            
            # Since split drops the \n, let's just do a simpler replacement on the list directly
            
for cell in nb["cells"]:
    if cell["cell_type"] == "markdown":
        for i, line in enumerate(cell["source"]):
            if "2. Feature engineering (ratios, interactions, binned features)" in line:
                cell["source"][i] = "2. Feature engineering (Engagement Score interaction)\n"
            elif "3. **Ensemble**: Weighted average of tuned XGBoost" in line:
                cell["source"][i] = "3. **Ensemble**: Weighted average of simple XGBoost and balanced Random Forest\n"
            elif "Our testing shows that a weighted ensemble of a tuned **XGBoost**" in line:
                cell["source"][i] = "We use a weighted ensemble of a simple **XGBoost** and a balanced **Random Forest**."

with open("notebook.ipynb", "w") as f:
    json.dump(nb, f, indent=1)
