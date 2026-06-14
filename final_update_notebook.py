import json

with open("notebook.ipynb", "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        
        # 1. Update engineer_features
        if "def engineer_features(df):" in source:
            new_source = [
                "def engineer_features(df):\n",
                "    \"\"\"Create new features from existing columns.\"\"\"\n",
                "    data = df.copy()\n",
                "    \n",
                "    # Core interaction feature\n",
                "    data['Engagement_Score'] = data['Pages_Viewed'] * data['Products_Viewed']\n",
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
            
        # 2. Update models
        if "xgb = XGBClassifier(" in source:
            new_source = [
                "cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)\n",
                "\n",
                "# Calculate class imbalance for XGBoost\n",
                "scale_pos = (y == 0).sum() / (y == 1).sum()\n",
                "\n",
                "# 1. XGBoost (Simple)\n",
                "xgb = XGBClassifier(\n",
                "    n_estimators=100, \n",
                "    max_depth=5, \n",
                "    learning_rate=0.1,\n",
                "    scale_pos_weight=scale_pos,\n",
                "    random_state=42, \n",
                "    eval_metric='logloss'\n",
                ")\n",
                "\n",
                "# 2. Random Forest (Balanced)\n",
                "rf = RandomForestClassifier(\n",
                "    n_estimators=100, \n",
                "    class_weight='balanced', \n",
                "    random_state=42, \n",
                "    n_jobs=-1\n",
                ")"
            ]
            cell["source"] = new_source

with open("notebook.ipynb", "w") as f:
    json.dump(nb, f, indent=1)
