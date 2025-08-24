# AI Interviewer

An intelligent interview simulation system powered by AutoGen and OpenAI GPT models. This project creates an interactive interview experience with multiple AI agents playing different roles in the interview process.

## 🚀 Features

- **Multi-Agent Interview System**: Three specialized AI agents working together:

  - **Interviewer**: Conducts professional interviews with targeted questions
  - **Candidate** (User): Real person being interviewed
  - **Career Coach**: Provides real-time feedback and career advice

- **Customizable Job Positions**: Configure interviews for any job position (default: Software Engineer)
- **Structured Interview Process**: 3 focused questions covering:
  - Technical skills and experience
  - Problem-solving abilities
  - Cultural fit
- **Real-time Feedback**: Career coach provides constructive feedback during the interview
- **Performance Summary**: Post-interview analysis with actionable advice

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- Internet connection for API calls

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd AI-INTERVIEWER
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🎯 Usage

### Quick Start

Run the interview simulation:

```bash
python main.py
```

### Custom Job Position

To customize the interview for a specific job position, modify the `job_position` variable in `main.py`:

```python
job_position = "Data Scientist"  # or any other position
```

### Using the AI Interview Module

You can also import and use the interview system in your own code:

```python
from AI_interview import team_Config, interview
import asyncio

async def custom_interview():
    job_position = "Product Manager"
    team = await team_Config(job_position)

    async for message in interview(team):
        print(message)

asyncio.run(custom_interview())
```

## 🏗️ Project Structure

```
AI INTERVIEWER/
├── AI_interview.py      # Core interview system with agent configuration
├── main.py             # Main entry point for running interviews
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (create this file)
└── README.md          # Project documentation
```

## 🤖 How It Works

1. **Initialization**: The system creates three AI agents with specific roles and capabilities
2. **Round-Robin Chat**: Agents take turns in a structured conversation flow
3. **Interview Process**:
   - Interviewer asks targeted questions (max 50 words each)
   - Candidate responds via user input
   - Career coach provides feedback (max 100 words)
4. **Termination**: Interview ends after 3 questions or when "TERMINATE" is mentioned

## ⚙️ Configuration

### Agent Customization

You can modify agent behaviors by editing their system messages in `AI_interview.py`:

- **Interviewer**: Adjust question style, topics, and interview flow
- **Career Coach**: Customize feedback style and focus areas

### Model Configuration

The system uses OpenAI's `gpt-4o-mini` model by default. You can change this in the `team_Config` function:

```python
model_client = OpenAIChatCompletionClient(
    model="gpt-4",  # Change to your preferred model
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=20
)
```

## 📊 Example Interview Flow

```
Interviewer: What programming languages are you most proficient in and how have you used them in recent projects?

Candidate: [Your response]

Career Coach: Great answer! You demonstrated specific experience. Consider mentioning any frameworks or tools you've used with those languages to show deeper expertise.

Interviewer: Describe a challenging problem you solved recently and walk me through your approach.

[... continues for 3 questions total]
```

## 🔧 Dependencies

- `autogen-agentchat`: Multi-agent conversation framework
- `autogen-core`: Core AutoGen functionality
- `autogen-ext`: Extended AutoGen features
- `python-dotenv`: Environment variable management
- `openai`: OpenAI API client
- `tiktoken`: Token counting for OpenAI models
- `pydantic`: Data validation

## 🚨 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your OpenAI API key is correctly set in the `.env` file
2. **Module Import Error**: Make sure all dependencies are installed via `pip install -r requirements.txt`
3. **Timeout Issues**: Increase the timeout value in the model client configuration if needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source.

## 🔮 Future Enhancements

- Advanced analytics and scoring
- Multi-language support
- Custom question banks

---

**Happy Interviewing!** 🎤✨
