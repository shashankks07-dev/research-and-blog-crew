# Research & Blog Crew

Built this as my first CrewAI project. You give it a topic, 
and two AI agents work together — one researches it, 
the other turns it into a blog post. Runs completely local 
using Ollama, no paid APIs needed.

## What it does
- Takes any topic as input
- First agent writes a detailed research report (~2000 words)
- Second agent turns that into a simple, fun blog post (~500 words)

## Stack
- CrewAI for the multi-agent pipeline
- Ollama to run models locally
- Gemma4 as the LLM
- Python 3.11

## Running it
Make sure Ollama is running, then:

cd research_and_blog_crew
crewai run

Enter a topic when prompted and you can see the result.
