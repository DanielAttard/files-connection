import streamlit as st
import pandas as pd
from st_files_connection import FilesConnection

"# Streamlit FilesConnection !"

"""
A simple demo for Streamlit FilesConnection.
"""

df = pd.DataFrame({"Owner": ["jerry", "barbara", "alex"], "Pet": ["fish", "cat", "puppy"], "Count": [4, 2, 1]})

local, gcs = st.tabs(["Local", "GCS"])

with local:
    "### Local Access"
    with st.echo():
        conn = st.experimental_connection("local", type=FilesConnection)
        st.help(conn)

    with st.echo():
        with st.expander("View the repo license with help from FilesConnection"):
            license = conn.read('/Users/Daniel/files-connection/LICENSE', input_format='text')
            license

with gcs:
    "### Reading data from Google Cloud Storage"

    """
    Write some test files to a GCS bucket and read them back. To run this code you need to:
    - Ensure gcsfs is installed (should be already if you did `pip install -r requirements.txt`)
    - Set up credentials to an GCS bucket using `.streamlit/secrets.toml`
      - Alternatively, you can pass a `token=` argument to the connection constructor with a path to your google token file
    - Set your correct bucket in the text input below and hit the checkbox!

    #### Streamlit secrets example

    ```toml
    # .streamlit/secrets.toml
    [connections.gcs]
    type = "..."
    project_id = "..."
    private_key_id = "..."
    private_key = "-----BEGIN PRIVATE KEY-----..."
    client_email = "..."
    client_id = "..."
    auth_uri = "https://accounts.google.com/o/oauth2/auth"
    token_uri = "https://oauth2.googleapis.com/token"
    auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
    client_x509_cert_url = "..."
    ```
    """

    gcs_bucket = st.text_input("GCS Bucket:", value="property-tax-bucket")

    if st.checkbox("Run the GCS code"):
        with st.echo():
            conn = st.experimental_connection("gcs", type=FilesConnection)
            st.help(conn)
        
        with st.expander("Setup code"):
            with st.echo():
                text_file = f"{gcs_bucket}/test3.txt"
                csv_file = f"{gcs_bucket}/test3.csv"
                parquet_file = f"{gcs_bucket}/test3.parquet"
                try:
                    _ = conn.read(text_file, input_format='text')
                except FileNotFoundError:
                    with conn.open(text_file, "wt") as f:
                        f.write("This is a test")
                
                try:
                    _ = conn.read(csv_file, input_format='csv')
                except FileNotFoundError:
                    with conn.open(csv_file, "wt") as f:
                        df.to_csv(f, index=False)
                
                try:
                    _ = conn.read(parquet_file, input_format='parquet')
                except FileNotFoundError:
                    with conn.open(parquet_file, "wb") as f:
                        df.to_parquet(f)

        "#### Text files"
        with st.echo():
            # "gcs://" is optional here, just included for effect
            st.write(conn.read(f"gcs://{gcs_bucket}/test3.txt", input_format='text'))

        "#### CSV Files"
        with st.echo():
            st.write(conn.read(f"gcs://{gcs_bucket}/test3.csv", input_format='csv'))

        "#### Parquet Files"
        with st.echo():
            st.write(conn.read(f"gcs://{gcs_bucket}/test3.parquet", input_format='parquet'))
        
        "#### List operations"
        with st.echo():
            st.write(conn.fs.ls(f"gcs://{gcs_bucket}/"))
