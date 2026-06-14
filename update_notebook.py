import json

with open("notebook.ipynb", "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        if "def engineer_features(df):" in source:
            new_source = [
                "def engineer_features(df):\n",
                "    \"\"\"Create new features from existing columns.\"\"\"\n",
                "    data = df.copy()\n",
                "    \n",
                "    # Core interaction features\n",
                "    data['Engagement_Score'] = data['Pages_Viewed'] * data['Products_Viewed']\n",
                "    data['Time_Per_Page'] = data['Time_On_Site'] / data['Pages_Viewed'].clip(lower=1)\n",
                "    \n",
                "    return data\n",
                "\n",
                "full_train = engineer_features(full_train)\n",
                "private_test = engineer_features(private_test_raw)\n",
                "\n",
                "print(\"Features after engineering:\", len(full_train.columns))\n",
                "print(\"New features:\", [c for c in full_train.columns if c not in train.columns])"
            ]
            cell["source"] = new_source

with open("notebook.ipynb", "w") as f:
    json.dump(nb, f, indent=1)
