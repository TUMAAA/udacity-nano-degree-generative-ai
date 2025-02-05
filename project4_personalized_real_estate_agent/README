This is the implementation of the 4th project in the Udacity course "Generative AI" titled "Project: Personalized Real Estate Agent".

The project requires:
- Using LLMs to generate a list of fake property listings
- Using an LLM to recommend listings before using the list of fake property listings
- Using LangChain memory and vector search to provide a list of recommended listings that the LLM can use for providing
real recommendations.

The solution in a nutshell:
- Using Few Shot Prompting to generate realistically looking listings
- Use of ConversationChain with memory buffer to track the conversation history
- Utilizing the LLM to make an accurate summary of the user preferences which are provided in a question-answer set
- Using the generated summary by the LLM to do semantic search in a Chroma DB that has loaded the generated listings
- Enriching the context of the prompt with the closest matches through extending the ConversationBufferMemory
to bypass the ConversationChain limitation of being able to just provide input/question (so one input only) as explained
in this thread https://github.com/langchain-ai/langchain/issues/1800

The notebook HomeFinder.ipynb is the main notebook for this project.
It contains the code for the project and the results of the project.
Just run the requirements.txt installation and be mindful of the comment therein!