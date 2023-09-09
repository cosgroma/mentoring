import json
import sys

def generate_markdown_from_json(json_file, output_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    markdown_content = f"# Knowledge Transfer Plan\n"
    markdown_content += "\n"
    markdown_content += f"- **Mentor:** {data['mentor']}\n\n"
    markdown_content += f"- **Mentee:** {data['mentee']}\n\n"
    markdown_content += "\n"
    
    
    markdown_content += f"## Vision\n\n{data['vision']}\n"
    markdown_content += "\n"
    
    markdown_content += f"## Objectives\n"
    markdown_content += "\n"
    for idx, goal in enumerate(data['mentoring_goals']):
        markdown_content += f"{idx + 1}. {goal['objective']}\n"
    markdown_content += "\n"
    
    markdown_content += f"## Mentoring Goals\n\n"
    for idx, goal in enumerate(data['mentoring_goals']):
        markdown_content += f"### Mentoring Goal {idx + 1}: {goal['name']}\n\n"
        markdown_content += f"**Objective:** {goal['objective']}\n\n"
        markdown_content += f"**Primary Support Person:** {goal['primary_support_person']}\n\n"
        markdown_content += "| Learning Activity | Competency | Beginning Date | Ending Date | Status | Feedback Mechanism | Performance Metrics |\n"
        markdown_content += "|-------------------|------------|----------------|-------------|--------|-------------------|---------------------|\n"
        for activity in goal['activities']:
            feedback = activity.get('feedback_mechanism', 'N/A')
            metrics = activity.get('performance_metrics', 'N/A')
            markdown_content += f"| {activity['name']} | {activity['competency']} | {activity['beginning_date']} | {activity['ending_date']} | {activity['status']} | {feedback} | {metrics} |\n"
        markdown_content += "\n"

    if 'networking_opportunities' in data:
        markdown_content += "## Networking Opportunities\n\n"
        for opportunity in data['networking_opportunities']:
            markdown_content += f"- **Name:** {opportunity['name']}\n"
            markdown_content += f"  - **Date:** {opportunity['date']}\n"
            markdown_content += f"  - **Location:** {opportunity['location']}\n"
            markdown_content += f"  - **Notes:** {opportunity['notes']}\n"
            markdown_content += "\n"
        markdown_content += "\n"
        
    if 'potential_challenges' in data:
        markdown_content += "## Potential Challenges\n\n"
        for challenge in data['potential_challenges']:
            markdown_content += f"- **Challenge:** {challenge['challenge']}\n\n"
            markdown_content += f"  - **Solution:** {challenge['solution']}\n\n"
        markdown_content += "\n"
    
    with open(output_file, 'w') as md_file:
        md_file.write(markdown_content)

def main():
    # Get json file from sys args
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
        output_file = sys.argv[2]
    
    generate_markdown_from_json(json_file, output_file)
    
if __name__ == "__main__":
    main()


