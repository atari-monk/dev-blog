import os

# Define the kebab-case categories and their subfiles (if any)
toolkit_structure = {
    "code-generation-and-conversion": [
        "generate-python-cli-script-modular.md",
        "generate-typescript-scene-implementation.md",
        "convert-javascript-to-typescript-modern.md",
    ],
    "code-analysis-and-optimization": [
        "analyze-code-functionality.md",
        "refactor-code-for-solid-principles.md",
        "component-improvement-pipeline-generator.md",
    ],
    "task-automation-and-workflow": [
        "focus-drone/generate-task-list-from-requirements.md",
        "universal-prompt-generator.md",
    ],
    "text-and-documentation": [
        "rewrite-text-better.md",
        "kebab-case-filename-generator.md",
        "prompt-standardization-instruction.md",
    ],
}

def create_toolkit_folders(base_path="prompt-llm"):
    """Generate the folder structure with empty files, skipping existing items."""
    try:
        os.makedirs(base_path, exist_ok=True)
        
        for category, files in toolkit_structure.items():
            category_path = os.path.join(base_path, category)
            os.makedirs(category_path, exist_ok=True)
            
            for file in files:
                # Handle nested paths (e.g., focus-drone/)
                file_dir = os.path.dirname(file)
                if file_dir:
                    full_dir_path = os.path.join(category_path, file_dir)
                    os.makedirs(full_dir_path, exist_ok=True)
                
                file_path = os.path.join(category_path, file)
                
                # Only create the file if it doesn't exist
                if not os.path.exists(file_path):
                    with open(file_path, "w") as f:
                        f.write("# Auto-generated file. Replace with actual content.\n")
                    print(f"Created: {file_path}")
                else:
                    print(f"Skipped (exists): {file_path}")
                    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_toolkit_folders()
    print("Folder structure generation complete!")