from flask import Flask, request, jsonify, render_template, url_for
import joblib
import numpy as np

app = Flask(__name__, static_url_path='/static')

# Load the trained model
try:
    model = joblib.load("crop_model.pkl")
    print("Crop model loaded successfully!")
except Exception as e:
    print(f"Error loading crop model: {e}")
    model = None # Set model to None if loading fails

@app.route('/')
def index():
    # Make sure index.html is in a 'templates' folder in the same directory as app.py
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if model is None:
        return jsonify({"error": "Machine learning model not loaded. Please check server logs."}), 500

    data = request.get_json()

    required_fields = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    try:
        N = float(data["N"])
        P = float(data["P"])
        K = float(data["K"])
        temperature = float(data["temperature"])
        humidity = float(data["humidity"])
        ph = float(data["ph"])
        rainfall = float(data["rainfall"])
    except ValueError:
        return jsonify({"error": "Invalid data types. Ensure numerical values are provided."}), 400

    features = [N, P, K, temperature, humidity, ph, rainfall]

    try:
        prediction_label = model.predict([features])[0]

        # Dynamic NPK adjustment based on input (simplified thresholds for demo)
        # These are basic rules, a real system would use more refined logic
        recommended_urea_amount = 50 if N < 80 else 40
        recommended_dap_amount = 35 if P < 40 else 25
        recommended_mop_amount = 20 if K < 40 else 15

        # General pH advice (simplified)
        ph_advice_text = ""
        if ph < 6.0:
            ph_advice_text = "Soil is acidic. Consider liming."
        elif ph > 7.5:
            ph_advice_text = "Soil is alkaline. Consider organic matter."
        else:
            ph_advice_text = "Soil pH is balanced."


        response_payload = {
            "recommended_crop": prediction_label,
            "soil_analysis": {
                "Nitrogen (N)": f"{N} kg/ha",
                "pH Level": ph,
                "Phosphorus (P)": f"{P} kg/ha",
                "Potassium (K)": f"{K} kg/ha"
            },
            "fertilizer_advice": {} # Initialize
        }

        # --- Simplified Fertilizer Advisory for Small Farm Holders ---
        if prediction_label.lower() == "rice": # Specific advice for rice crop
            response_payload["fertilizer_advice"] = {
                "main_heading": "Rice Fertilizer Advisory (Small Farms)",
                "general_overview": "Essential tips for efficient rice cultivation.",
                "key_principles": [
                    "1. **Soil Test:** Know your soil's needs.",
                    "2. **Balanced NPK:** Provide NPK as recommended.",
                    "3. **Organic Matter:** Add compost/manure for health.",
                    "4. **Split Application:** Apply in stages."
                ],
                "npk_recommendation": [
                    "**Based on Your Inputs:**",
                    f"- Urea (N): {recommended_urea_amount} kg/acre (Basal & Top-dress)",
                    f"- DAP (P): {recommended_dap_amount} kg/acre (Full basal)",
                    f"- MOP (K): {recommended_mop_amount} kg/acre (Basal & Flowering)"
                ],
                "ph_specific_advice": [
                    "**pH Guidance:**",
                    ph_advice_text
                ],
                "application_timeline": [
                    "**Key Stages for Rice:**",
                    "•   **Basal:** Before planting (all P & K, 1/3 N).",
                    "•   **1st Top-Dressing:** 20-30 days after transplanting (1/3 N).",
                    "•   **2nd Top-Dressing:** 40-60 days after transplanting (1/3 N)."
                ],
                "important_guidelines": [
                    "**Best Practices:**",
                    "-   Apply in moist soil.",
                    "-   Ensure even spreading.",
                    "-   Avoid over-application."
                ],
                "special_considerations": [
                    "**Small Farm Tips:**",
                    "•   Use organic manure/bio-fertilizers.",
                    "•   Manage water efficiently.",
                    "•   Consult local experts."
                ]
            }
        else: # Generic advice for other crops
            response_payload["fertilizer_advice"] = {
                "main_heading": "General Fertilizer Advisory",
                "general_overview": f"For {prediction_label} cultivation, focus on core nutrient management.",
                "key_principles": [
                    "1. **Soil Test:** Always test soil first.",
                    "2. **Balanced NPK:** Provide essential NPK.",
                    "3. **Organic Matter:** Improve soil health.",
                    "4. **Timely Application:** Apply at critical growth stages."
                ],
                "npk_recommendation": [
                    "**Basic NPK Guidance:**",
                    f"- Nitrogen (N): {N} kg/ha",
                    f"- Phosphorus (P): {P} kg/ha",
                    f"- Potassium (K): {K} kg/ha"
                ],
                "ph_specific_advice": [
                    "**pH Guidance:**",
                    ph_advice_text
                ],
                "application_timeline": [
                    "**General Schedule:**",
                    "•   Basal dose at planting.",
                    "•   Top-dressing during active growth.",
                    "•   Foliar application for deficiencies."
                ],
                "important_guidelines": [
                    "**Best Practices:**",
                    "-   Apply in moist soil.",
                    "-   Ensure even distribution.",
                    "-   Avoid over-application."
                ],
                "special_considerations": [
                    "**Small Farm Tips:**",
                    "•   Prioritize organic amendments.",
                    "•   Seek local expert advice.",
                    "•   Consider crop rotation."
                ]
            }

        return jsonify(response_payload)

    except Exception as e:
        print(f"Error during prediction or data generation: {e}")
        return jsonify({"error": "An internal server error occurred. Check server logs."}), 500

if __name__ == "__main__":
    app.run(debug=True)