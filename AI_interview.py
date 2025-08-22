from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

model_client = OpenAIChatCompletionClient(model="gpt-4o-mini",api_key=os.getenv("OPENAI_API_KEY"))

job_position = "Software Engineer"

interviewer = AssistantAgent(
    name="Interviewer",
    model_client=model_client,
    description=f"An AI agent that conducts interviews for a {job_position} position.",
    system_message=f'''
    You are a professional interviewer for a {job_position} position.
    Ask one clear question at a time and Wait for user to respond. 
    Ask 5 question in total covering technical skills and experience, problem-solving abilities, and cultural fit.
    After asking 3 questions, say 'TERMINATE' at the end of the interview.
    '''
)

interviwee = UserProxyAgent(
    name="candidate",
    description=f"An agent that simulates a candidate for a {job_position} position.",
    input_func=input,
)

career_coach = AssistantAgent(
    name="career_coach",
    model_client=model_client,
    description=f"An AI agent that provides career advice and feedback to the candidate for a {job_position} position.",
    system_message=f'''
    You are a career coach specializing in preparing candidates for {job_position} interviews.
    Provide constructive feedback on the candidate's responses and suggest improvements.
    After the interview, summarize the candidate's performance and provide actionable advice.
    '''
)

termination_condition = TextMentionTermination("TERMINATE")

team = RoundRobinGroupChat(
    participants=[interviewer,interviwee,career_coach],
    termination_condition=termination_condition,
    max_turns=20
)

stream = team.run_stream(task="Conducting an interview for a Software Engineer position.")

async def main():
    await Console(stream)

if __name__ == "__main__":
    asyncio.run(main())







