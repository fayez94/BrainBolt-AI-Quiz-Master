import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging
from langchain.chains import LLMChain

#imporing necessary packages packages from langchain
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
from langchain.schema.runnable import RunnableSequence
from langchain.schema.runnable import RunnableMap
from langchain.chains import SequentialChain



# Load environment variables from the .env file
load_dotenv()

# Access the environment variables just like you would with os.environ
key=os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(openai_api_key=key,model_name="gpt-3.5-turbo", temperature=0.7)

template="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}

"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=template)

quiz_chain=LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

# quiz_chain = quiz_generation_prompt | llm  # Chain the prompt and LLM directly


template2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""


quiz_evaluation_prompt=PromptTemplate(input_variables=["subject", "quiz"], template=template2)

review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

# review_chain = quiz_evaluation_prompt | llm  # Chain the prompt and LLM directly


# This is an Overall Chain where we run the two chains in Sequence
generate_evaluate_chain=SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                        output_variables=["quiz", "review"], verbose=True,)

# # Remove RunnableSequence and directly chain the components
# generate_evaluate_chain = quiz_chain | review_chain  # Chain the quiz generation and review chains

# Example of invoking the chain
def generate_and_evaluate_quiz(input_data):
    """
    Function to generate and evaluate a quiz using the chain.
    :param input_data: A dictionary containing the input variables for the chain.
    :return: The output of the chain (quiz and review).
    """
    try:
        # Use .invoke() to execute the chain
        result = generate_evaluate_chain.invoke(input_data)
        return result
    except Exception as e:
        logging.error(f"Error while generating and evaluating quiz: {e}")
        traceback.print_exc()
        return None

# Example usage
if __name__ == "__main__":
    input_data = {
        "text": "Sample text for quiz generation.",
        "number": 5,
        "subject": "Science",
        "tone": "formal",
        "response_json": "{}"
    }
    output = generate_and_evaluate_quiz(input_data)
    print(output)