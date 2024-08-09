from typing import List, Optional
from pydantic import BaseModel
import json
import os
from groq import Groq
import streamlit as st

GROQ_API_KEY= st.secrets["api_key"]

groq = Groq(api_key=GROQ_API_KEY)


class Resume(BaseModel):
    Customer_details: dict[str, str]
    Products: List[str]
    Total_amount: Optional[float] =None


def get_invoice(invoice_text: str) -> Resume:
    prompt = (
        """You are an Invoice extractor that extracts the details from the invoice and provides output in valid JSON object,
           strictly adhering to the following structure: {schema}.
           -Must include product name.
           -HSN/SAC is of 8 digits only. 
           -Must keep this format in mind: if ex-- '7204219089.006,790 KGS'. 
           Then
           -HSN: 72042190, 
           -Rate: 89.00, 
           -Quantity: 6790 KGS.
           
           Extract details from the Invoice text: {invoice_text}"""
    ).format(
        schema=json.dumps(Resume.model_json_schema(), indent=4),
        invoice_text=invoice_text
    )
    
    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        model="llama3-8b-8192",
        temperature=0.0,
    )
    response_text = chat_completion.choices[0].message.content.strip()
    print(response_text)
    try:
        cleaned_llm_response = clean_response_text(response_text)
        transformed_data = transform_resume(cleaned_llm_response)
        return transformed_data
    except json.JSONDecodeError as exc:
            print(f"JSONDecodeError: {exc}")
            return Resume()
    
    
    
def clean_response_text(response_text: str) -> dict:
    """Function to clean the llm response.
       It returns a dict
    """
    json_start = response_text.find("{")
    json_end = response_text.rfind("}") + 1
    if json_start == -1 or json_end == -1:
        raise ValueError("Invalid response format")
    json_str = response_text[json_start:json_end]
    json_data = json.loads(json_str)
    return json_data


def transform_resume(json_data) -> dict:
    """Function to transform the resume JSON data to a desired format."""
    properties = json_data.get("properties", {})

    Customer_details = properties.get("Customer_details", {})
    Products = properties.get("Products", {})
    Total_amount = properties.get("Total_amount", None)
    transformed_data = {
        "Customer_details": Customer_details,
        "Products": Products,
        "Total_amount": Total_amount
    }

    return transformed_data


