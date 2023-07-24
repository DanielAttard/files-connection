import os

if 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
    print("GOOGLE_APPLICATION_CREDENTIALS is set.")
else:
    print("GOOGLE_APPLICATION_CREDENTIALS is not set.")