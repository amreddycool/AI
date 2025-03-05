# Description

We start with basic RAG model - Evaluate the performance. Then move to Advanced RAG with the aim of improving perfromance and accuracy.

llama-index and llama3.2 with PDF read, ingest, index and search.

Loading PDF document about Physics from : `https://en.wikipedia.org/wiki/Physics` 
Similarly there are 17 more PDFs that are links in the above document and it's links.


# Get llama3.2 locally
Refer `https://ollama.com/`

# Deploy dependencies
`pip install -r requirements.txt`

# Run  
`start.sh`

# Examples


What is general revlativity

>> General relativity is a theory of gravitation that explains how masses warp spacetime, resulting in gravitational attraction between them. According to this theory, gravity does not act as a force that pulls objects towards each other, but rather it is the result of the geometry of spacetime itself being curved by massive objects.

What is newton's law of gravity

>> Newton's concept of gravity as a universal force that extends beyond Earth's surface to influence celestial bodies, including the Moon. He hypothesized that this force decreases with distance in an inverse-square proportion, allowing for calculations of celestial orbits. This idea led him to propose "universal gravitation," which posits that the same force responsible for terrestrial gravity also governs the motion of objects in space.

What is higgs boson

>> A particle predicted by a theoretical model to be responsible for conferring mass to subatomic particles, discovered in 1964 through a series of experiments involving high-energy collisions of protons.

# Performance

Basic RAG model kept on failing, but still continuing (Embedding attempt failed: MPS backend out of memory. Suggestion: PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0)

Setting the variable as per suggestion.

export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0

## Parsing Nodes
Took around 2 minutes with 4-5 GB RAM and 100% CPU

## Generating Emeddings

Memory usage seems around 4-6 GB
CPU usage seems 100%
Most of the time 30 minutes around, seems to be spent on Generating Embeddings

Each query took about 30 seconds. 

Using some Advanced RAG techniques,
@todo - increase the performance of read and ingestion
@todo - increase the performance of query  
