import os
from textwrap import dedent

from crewai import Crew


from agents import CustomAgents
from tasks import CustomTasks



class CustomCrew:
    def __init__(self, var1):
        self.var1 = var1

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        pdf_agent = agents.pdf_agent()
        teacher_agent = agents.teacher_agent()
        question_agent = agents.question_agents()
        answer_agent = agents.answer_agents()


        # Custom tasks include agent name and variables as input
        task1 = tasks.pdf_task(
            pdf_agent,
            self.var1
        )

        task2 = tasks.teacher_task(teacher_agent)
        task3 = tasks.question_task(question_agent)
        task4 = tasks.answer_task(answer_agent)



        # Define your custom crew here
        crew = Crew(
            agents=[pdf_agent, teacher_agent],
            tasks=[task1, task2],
            verbose=True,
        )
        crew2 = Crew(agents=[pdf_agent, question_agent,answer_agent ],
            tasks=[task1, task3, task4],
            verbose=True,

        )


        result = crew.kickoff()
        return result




# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("Welcome to your personal teacher")
    var1 = input(dedent("""What dont you understand about the material? """))

    custom_crew = CustomCrew(var1)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is a clear explanation")
    print("########################\n")
    print(result)