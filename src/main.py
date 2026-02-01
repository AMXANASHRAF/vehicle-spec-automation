import os
from dotenv import load_dotenv
import pandas as pd

from llm.hf_extractor import extract_specs


def main():

    load_dotenv()

    api_key = os.getenv("HF_API_KEY")

    if not api_key:
        raise ValueError("HF_API_KEY not found in .env")

    # ----------------------------
    # Example vehicle text
    # (paste anything here)
    # ----------------------------
    vehicle_text = """
    Engine: 1.5L inline-4 petrol
    Power: 115 hp
    Torque: 145 Nm
    Transmission: CVT
    Drivetrain: FWD
    """

    print("🤖 Extracting specs...")

    specs = extract_specs(vehicle_text, api_key)

    if specs:
        print(specs)

        df = pd.DataFrame([specs])
        df.to_csv("vehicle_specs_output.csv", index=False)

        print("✅ Saved → vehicle_specs_output.csv")


if __name__ == "__main__":
    main()
