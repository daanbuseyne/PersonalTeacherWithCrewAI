# PersonalTeacherWithCrewAI
Project implementing a personal teacher that can clearly explain questions about a certain pdf. Using RAG to find answers related to the material. Teacher also has acces to wikipedia to explain the concepts in more depth.
This is implemented in pdf_agent and teacher_agent in task1 and task2 (run crew). I ran this locally using ollama phi3 model. While using more eleborate llm's would work better, for this simple task phi3 seems sufficient. 

Working on extension that includes the teacher to ask questions about the material to test the knowledge of the student. This is implemented in question_agent and answer_agent and task 3 and task4, but does not work correctly at the moment. I dont think this will be possible using the phi3 model since he seems to get stuck in his own reasoning. 

Have fun and tips/ideas are always welcome (this is one of my first projects)
