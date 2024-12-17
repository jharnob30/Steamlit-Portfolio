@echo off

:: Activate virtual environment
call myenv/Scripts/activate

:: Run Streamlit app
streamlit run app.py
