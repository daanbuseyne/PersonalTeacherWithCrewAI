from crewai import Agent
from textwrap import dedent
from crewai_tools import PDFSearchTool
from langchain_community.llms import Ollama
from langchain.agents import Tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper




# 2 Tools we will use PDFRAG and WIKI

#Since i want to run this code locally on my macbook I choose the phi3 model and allminilm
pdftool = PDFSearchTool("1406.2661v1.pdf", #name of pdf (studymaterial) you want to upload
            config=dict(
                llm=dict(
                    provider="ollama",  
                    config=dict(
                        model="phi3",
                        temperature=0.0,
                        # top_p=1,
                        # stream=true,
                    ),
                ),
                embedder=dict(
                    provider="ollama",  
                    config=dict(
                        model="all-minilm",
                        #task_type="retrieval_document",
                        # title="Embeddings",
                    ),
                ),
            )
        )


#Wikitool
wiki = WikipediaAPIWrapper()

wiki_tool = Tool(
  name="Wikipedia",
  func=wiki.run,
  description="Useful for search-based queries",
)





class CustomAgents:
    def __init__(self):
        self.Phi3 = Ollama(model = 'phi3')

    def pdf_agent(self):
        return Agent(
            role="Senior PDF Analyst",
            backstory=dedent(f"""You can find anything in a pdf.  The people need you."""),
            goal=dedent(f"""Uncover any information from pdf files exceptionally well."""),
            tools=[pdftool],
            verbose=True,
            llm=self.Phi3,
        )


    def teacher_agent(self):
        return Agent(
            role="Teacher",
            backstory=dedent(f"""You love nothing more then clearly explaining concepts"""),
            goal=dedent(f"""Take the information from the pdf agent and explain it to your students"""),
            tools=[wiki_tool],
            verbose=True,
            llm=self.Phi3,
        )

    def question_agents(self):
        return Agent(
            role="Teacher",
            backstory=dedent(f"""You love nothing more then making exam questions"""),
            goal=dedent(f"""Take the information from the pdf agent and come up with an exam question"""),
            tools = [wiki_tool],
            verbose=True,
            llm=self.Phi3,
        )

    def answer_agents(self):
        return Agent(
            role="domain expert",
            backstory=dedent(f"""You answer every question perfectly"""),
            goal=dedent(f"""Answer the question of the question agent using the information from the pdf agent"""),
            tools = [wiki_tool],
            verbose=True,
            llm=self.Phi3,
        )


