# Description

llama-index and llama3.2 with REST tool calling

# Tool data
REST API provides exchange rate, using Flask

Current mappings:
``
 "GBPUSD": 1.1111
 "GBPEUR": 1.2222
 "GBPAUD": 1.3333
``

# Get llama3.2 locally
Refer `https://ollama.com/`

# Deploy dependencies
`pip install -r requirements.txt`

# Run  
`start.sh`

# Examples

What is the exachange rate from GBP to EUR?

>> The current exchange rate from GBP to EUR is approximately 1 GBP = 1.2222 EUR.

Can you convert 100 GBP into EUR

>> 100 GBP is approximately equal to 122.22 EUR.

Can you convert 122.22 EUR into GBP

>> 122.22 EUR is approximately equal to 100 GBP.

Can you convert 100 EUR to AUD

>> 100 EUR is approximately equal to 147 AUD.
   Which is wrong !! There is no mapping for this combination .. @todo how can this be done without extra mapping?



