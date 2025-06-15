# AIPI 561 Final Project
The final project is a web-based fashion AI assistant that provides real time fashion trend analysis and a chatbot that can provide fashion suggestions based on current trends. It scrapes websites for latest fashion trends (Vogue is used in the demo) and generates a report with sentiment values.  A simple Flask app is runs the trend pipline and generates AI content. There is a CLI tool to execute the pipeline and interface. There is also a Dockerfile for deployment via App Runner and tests to verify the functionality of the pipeline. 

Note: This project integrates an LLM model, which is unfortunately not working due to compatability issues with my current laptop. I have been on the road with limited access to my PC so I have only been able to work via my laptop which has some restrictions. There is proof of concept in my repository. 


### Integration of Course Topics

1. **Natural Language AI with Bedrock**  
   Implemented a conversational AI assistant interface through Flask routes to generate fashion-related text using a local LLM as a proof of concept.

2. **AI Orchestration Fundamentals**  
   Designed and implemented an orchestrated pipeline that scrapes fashion trends from websites, analyzes sentiment, generates reports, and handles errors.

3. **Advanced Analytics Integration**  
   Developed a data processing pipeline combined with sentiment analysis to produce insights on fashion trends, which are visualized via the web interface and CLI. This is then used to help with responses by the chatbot. 

4. **AWS Generative AI Implementation**  
   Included a generative text service in the assistant using a local LLM, mirroring the text generation APIs built in the mini-project.

5. **CLI and Automation**  
   Created a command-line interface to run the trend analysis and text generation tasks for automation and testing purposes.

6. **Open Source LLM Integration**  
   Deployed a local Llama-based model, wrapped with Python code for inference. 

### User Guide
```
pip install -r requirements.txt
python app.py
```
Go to the [host website](http://localhost:8080/) to interact with the web interface. 
