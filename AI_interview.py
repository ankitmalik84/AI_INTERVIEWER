from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
from autogen_agentchat.base import TaskResult
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

async def team_Config(job_position="Software Engineer"):
    """
    This function configures the team for the interview.
    """
    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini",api_key=os.getenv("OPENAI_API_KEY"), timeout=20)

    interviewer = AssistantAgent(
        name="Interviewer",
        model_client=model_client,
        description=f"An AI agent that conducts interviews for a {job_position} position.",
        system_message=f'''
        You are a professional interviewer for a {job_position} position.
        Ask one clear question at a time and Wait for user to respond. 
        Your job is to continue and ask questions, don't pay any attention to career coach response.
        Ask 3 question in total covering technical skills and experience, problem-solving abilities, and cultural fit.
        After asking 3 questions, say 'TERMINATE' at the end of the interview.
        Make question under 50 words.
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
        Make it under 100 words.
        '''
    )

    termination_condition = TextMentionTermination("TERMINATE")

    team = RoundRobinGroupChat(
        participants=[interviewer,interviwee,career_coach],
        termination_condition=termination_condition,
        max_turns=20
    )

    return team

async def interview(team):
    """
    This function conducts the interview.
    """
    async for message in team.run_stream(task='Start the interview with the first question ?'):
        if isinstance(message, TaskResult):
            msg = f'Interview completed with result: {message.stop_reason}'
            yield msg
        else:
            msg = f'{message.source}: {message.content}'
            yield msg

# async def main():
#     job_position = "Software Engineer"
#     team = await team_Config(job_position)
#     async for message in interview(team):
#         print("-"*70)
#         print(type(message))

# if __name__ == "__main__":
#     asyncio.run(main())