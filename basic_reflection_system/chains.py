from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv
load_dotenv()

generate_prompt=ChatPromptTemplate.from_messages(
    [
        ("system",
        """
        You are expert techie twiteer expert for writting the post.
        Generate the best twitter post  for the user request.
        If user provide critique, respond with a revised verison of our previous attempt.
        """
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

reflection_prompt=ChatPromptTemplate.from_messages(
    [
        ("system",
        """
        You are and expert for grading the viral twitter post.
        Generate the critique and recommendations  for the user's post.
        Always provide recommendation,inculding lenght of post and virality,style etc in well points so that it can we regenerated.
        """
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

llm=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5
)

generate_chain=generate_prompt|llm
reflection_chain=reflection_prompt|llm