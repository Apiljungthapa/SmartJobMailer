import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Chain:
    def __init__(self):
        """
        Initialize the Chain class with an instance of the ChatGroq language model.
        """
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),  # Fetch the API key from environment variables
            model_name="llama-3.1-70b-versatile"
        )

    def extract_jobs(self, cleaned_text):

        prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the 
        following keys: `role`, `experience`, `skills` and `description`.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE AND NO STRING STRICTLY..):    
        
        """
        )

        chain_extract = prompt_extract | self.llm 
        res = chain_extract.invoke(input={'page_data':cleaned_text})


        json_parser = JsonOutputParser()
        json_res = json_parser.parse(res.content)

        for i in json_res:
            new_json_file=i

        return new_json_file
           
            


    def write_mail(self, job, links):

        prompt_email = PromptTemplate.from_template(
       
        """
        ### JOB DESCRIPTION:

        {job_description}
        
        ### INSTRUCTION:
        You are Apil, a business development executive at Apil Bussiness Development company. Apil Bussiness Development company is an AI & Software Consulting company dedicated to facilitating
        the seamless integration of business processes through automated tools. 
        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
        process optimization, cost reduction, and heightened overall efficiency. 
        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of Apil Bussiness Development company 
        in fulfilling their needs.
        Also add the most relevant ones from the following links to showcase Apil Bussiness Development company's portfolio: {link_list}
        Remember you are Apil, BDE at Apil Bussiness Development company. 
        Do not provide a preamble.

        ### EMAIL (NO PREAMBLE):
        
        """

        )

        chain_email = prompt_email | self.llm

        res = chain_email.invoke({"job_description": str(job), "link_list": links})

        return res.content
                


if __name__ == "__main__":
   
    chain = Chain()
