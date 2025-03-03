#!/bin/bash
#python -m flask --app api_server run --host=0.0.0.0 --debug &
python ./api_server.py &

echo "API Server is Up"

python -m chainlit run ai_agent.py

echo "AI Agent is Up"

