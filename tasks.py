from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, you will have happy students!"

    def pdf_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Tell me precisely what I need to know from the RAG tool.
            Use this as what I want to lookup: {var1}

            {self.__tip_section()}

            Make sure to be as accurate as possible. 
        """
            ),
            expected_output="Full analysis.",
            agent=agent,
        )

    def teacher_task(self, agent):
        return Task(
            description=dedent(
                f"""
            Take the input from task 1 and explain it clearly.

            {self.__tip_section()}
        """
            ),
            expected_output="Give me an in depth explanation followed by a short summary",
            agent=agent,
        )

    def question_task(self, agent):
        return Task(
            description=dedent(
                f"""
                    Take the input from task 1 and create a short question about it. This question will be used on the upcoming exam.

                    {self.__tip_section()}
                """
            ),
            expected_output="give me one question ",
            agent=agent,
        )

    def answer_task(self, agent):
        return Task(
            description=dedent(
                f"""
                        Take the question from task 3 and find the answer to it.

                            {self.__tip_section()}
                        """
            ),
            expected_output="Give me tne answer to the question",
            agent=agent,
        )

