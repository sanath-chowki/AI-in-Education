import wikipedia
import gradio as gr

# Function to answer user queries using Wikipedia
def chatbot(input):
    try:
        result = wikipedia.summary(input, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple matches found. Please be more specific."
    except wikipedia.exceptions.PageError as e:
        return f"Sorry, I couldn't find any information on that topic."

# Create a Gradio interface for the chatbot
iface = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="Wikipedia Chatbot",
    description="Ask me anything, and I'll try to provide information from Wikipedia.",
)

# Start the Gradio interface
iface.launch()
