# Next.js Project Setup Script

This Python script automates the creation of a Next.js project base, streamlining the setup process for new projects.

## Prerequisites

- Python 3.x installed on your system
- Node.js and npm (Node Package Manager) installed
- Git installed (optional, but recommended)

## Installation

1. Clone this repository or download the script:
   ```
   git clone https://github.com/yourusername/nextjs_proj_setup.git
   ```
   Or download `nextjs_creator.py` directly.

2. Navigate to the script directory:
   ```
   cd nextjs_proj_setup
   ```

## Usage

1. Create a new directory for your Next.js project:
   ```
   mkdir my-nextjs-project
   ```

2. Get the full path of your new project directory:
   - On Unix-like systems (Linux, macOS):
     ```
     cd my-nextjs-project && pwd
     ```
   - On Windows (Command Prompt):
     ```
     cd my-nextjs-project && echo %cd%
     ```

3. Run the script:
   ```
   python nextjs_creator.py
   ```
   or
   ```
   python3 nextjs_creator.py
   ```

4. When prompted, paste the full path to your new project directory and press Enter.

5. Wait for the script to complete. It will set up your Next.js project with all necessary dependencies and configurations.

## What the Script Does

- Creates a new Next.js project using `create-next-app`
- Installs additional dependencies (if specified in the script)
- Sets up initial project structure and files
- Configures ESLint and other development tools
- Initializes a Git repository (if Git is installed)

## Customization

You can modify the `nextjs_creator.py` script to add or remove features based on your project requirements.

## Troubleshooting

If you encounter any issues, please check the following:
- Ensure all prerequisites are correctly installed
- Verify that you have the necessary permissions to create directories and files in the specified location
- Check your internet connection, as the script needs to download packages

## Contributing

Contributions to improve the script are welcome. Please feel free to submit a pull request or open an issue on the GitHub repository.

## License

[MIT License](LICENSE.md)

