Simple code project to transform CSV file data into useful information

Requires pandas, fastapi, uvicorn
- uv pip install fastapi uvicorn pandas

To start data server:
- uvicorn export_data:app
- Open http://127.0.0.1:8000/top_products in browser