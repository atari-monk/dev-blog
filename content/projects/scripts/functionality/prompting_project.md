# Code Functionality Analysis (prompting_project)

## Files Index
- [open_llm.ps1](#open_llmps1)
- [list_md_json.py](#list_md_jsonpy)
- [prompt.ps1](#promptps1)

## Functionality Descriptions

### open_llm.ps1
- **Primary Purpose**: Opens DeepSeek AI chat interface in a web browser
- **Browser Selection**: Supports both Chrome (default) and Firefox via command-line flags
- **Help System**: Displays usage instructions with `-h`, `-help`, or `--help` flags
- **Path Detection**: Automatically locates browser executables in standard installation directories
- **Error Handling**: Throws exceptions if specified browser is not found on the system
- **Cross-Platform Paths**: Handles both 32-bit and 64-bit program file directories
- **Simple Interface**: Single command execution with optional browser preference flag

### list_md_json.py
- **Format Conversion**: Converts between bullet point lists and quoted JSON array formats
- **Clipboard Integration**: Automatically reads from and writes to system clipboard
- **Input Parsing**: Handles both markdown-style bullet points (`- item`) and comma-separated quoted strings
- **Output Formatting**: Generates properly formatted JSON string arrays with trailing comma
- **Debug Mode**: Optional debug flag to display input/output for troubleshooting
- **Text Cleaning**: Removes quotation marks and trailing commas from input strings
- **Line Filtering**: Skips empty lines during conversion process
- **Standalone Utility**: Can be run directly or integrated into other workflows

### prompt.ps1
- **Prompt Management System**: Orchestrates prompt template loading and processing workflow
- **Template Selection**: Provides interactive template selection from JSON files
- **Project Integration**: Links prompts to specific project directories with queue/history systems
- **Data Merging**: Combines template data with queue items, prioritizing queue content
- **Queue Processing**: Automatically processes prompt queue items and moves them to history
- **File Management**: Manages queue and history JSON files for tracking prompt iterations
- **Status Reporting**: Provides color-coded console feedback for each processing step
- **Modular Design**: Leverages multiple imported PowerShell functions for specific tasks
- **Execution Pipeline**: Finalizes by executing the composed prompt through `$prompt.Execute()`