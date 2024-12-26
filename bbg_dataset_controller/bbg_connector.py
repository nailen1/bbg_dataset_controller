import pdblp
from dotenv import load_dotenv
import os

load_dotenv()

PORT = os.getenv('PORT')

bcon = pdblp.BCon(debug=False, port=PORT, timeout=5000)
bcon.start()