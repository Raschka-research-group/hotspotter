# Hotspotter script by Sebastian Raschka, 2022
# More details in GitHub repository:
# https://github.com/Raschka-research-group/hotspotter

import argparse
import sys

import numpy as np
import pandas as pd
from joblib import load
from packaging import version


def get_packages(pkgs):
    versions = []
    for p in pkgs:
        try:
            imported = __import__(p)
            try:
                versions.append(imported.__version__)
            except AttributeError:
                try:
                    versions.append(imported.version)
                except AttributeError:
                    try:
                        versions.append(imported.version_info)
                    except AttributeError:
                        versions.append("0.0")
        except ImportError:
            print(f"[FAIL]: {p} is not installed and/or cannot be imported.")
            versions.append("N/A")
    return versions


def check_packages(d):

    versions = get_packages(d.keys())

    for (pkg_name, suggested_ver), actual_ver in zip(d.items(), versions):
        if actual_ver == "N/A":
            continue
        actual_ver, suggested_ver = version.parse(actual_ver), version.parse(
            suggested_ver
        )
        if actual_ver < suggested_ver:
            print(
                f"[FAIL] {pkg_name} {actual_ver}, please upgrade to >= {suggested_ver}"
            )
        else:
            print(f"[OK] {pkg_name} {actual_ver}")


if __name__ == "__main__":

    if version.parse(sys.version.split(" ")[0].strip()) < version.parse("3.8"):
        print(
            "[FAIL] We recommend Python 3.8 or newer but"
            " found version %s" % (sys.version)
        )
    else:
        print("[OK] Your Python version is %s" % (sys.version))

    package_d = {
        "sklearn": "1.1.2",
        "numpy": "1.23.3",
        "joblib": "1.1.0",
        "pandas": "1.4.4",
    }
    check_packages(package_d)

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--csv_path", help="Path to the CSV file", type=str, required=True
    )

    parser.add_argument(
        "--trained_model",
        help="Path to the trained model",
        type=str,
        default="./mlp.joblib",
    )

    parser.add_argument(
        "--trained_model_sequence_only",
        help="Path to the trained model for --sequence_only prediction.",
        type=str,
        default="./mlp_sequence_only.joblib",
    )

    parser.add_argument(
        "--sequence_only", type=str, choices=("true", "false"), default="false"
    )

    parser.add_argument(
        "--print_row_numbers", type=str, choices=("true", "false"), default="false"
    )

    args = parser.parse_args()

    args_d = {"true": True, "false": False}

    args.sequence_only = args_d[args.sequence_only]
    args.print_row_numbers = args_d[args.print_row_numbers]

    df = pd.read_csv(args.csv_path)

    if args.sequence_only:
        feature_list = ["residue", "consurf", "secondary structure"]

    else:
        feature_list = [
            "avg bond number",
            "Hbond",
            "residue",
            "Hphob",
            "consurf",
            "B' side chain",
            "secondary structure",
            "asa",
        ]

    for feature in feature_list:
        if feature not in df.columns:
            raise ValueError(f"Did not find column {feature}")

    df = df[feature_list]

    if args.sequence_only:
        ohe, pipe = load(args.trained_model_sequence_only)
    else:
        ohe, pipe = load(args.trained_model)

    ohe.handle_unknown = "ignore"

    aa_codes = [
        "A",
        "R",
        "N",
        "D",
        "C",
        "E",
        "Q",
        "G",
        "H",
        "I",
        "L",
        "K",
        "M",
        "F",
        "P",
        "S",
        "T",
        "W",
        "Y",
        "V",
    ]

    code_to_int = {c: i for i, c in enumerate(aa_codes)}
    df["residue"] = df["residue"].map(code_to_int)
    df["residue"] = df["residue"].astype("category")

    res_codes = ["H", "S", "T", "-"]
    code_to_int = {c: i for i, c in enumerate(res_codes)}
    df["secondary structure"] = df["secondary structure"].map(code_to_int)
    df["secondary structure"] = df["secondary structure"].astype("category")
    ohe_list = ["residue", "secondary structure"]

    df_ohe = df.drop(columns=ohe_list)
    X_ohe_temp = np.asarray(ohe.transform(df[ohe_list]).todense())
    X_ohe = np.hstack((df_ohe.values, X_ohe_temp))

    results = pipe.predict(X_ohe)

    print("\n==========\nRESULTS\n==========")

    if args.print_row_numbers:
        for idx, i in enumerate(results):
            print(f"{idx:04d}: {i}")

    else:
        for i in results:
            print(i)
